<?php
/**
 * Cliff Canfield Plumbing — quote form handler.
 *
 * Receives the website quote form, blocks spam, then:
 *   1) sends a Pushover push notification to your phone, and
 *   2) (optional) emails you a copy of the lead.
 *
 * Your private keys are NOT in this file. They live in lead-config.php, which goes in your
 * cPanel home folder (one level ABOVE public_html) so it is never public or on GitHub.
 * See site-tools/lead-config.sample.php for the template.
 */

header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');
header('Cache-Control: no-store');

function respond(int $code, array $body): void {
    http_response_code($code);
    echo json_encode($body);
    exit;
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    header('Allow: POST');
    respond(405, ['ok' => false, 'error' => 'method_not_allowed']);
}

// ---------------------------------------------------------------- config
$configPaths = array_filter([
    getenv('LEAD_CONFIG') ?: null,                                         // local testing only
    !empty($_SERVER['DOCUMENT_ROOT']) ? dirname($_SERVER['DOCUMENT_ROOT']) . '/lead-config.php' : null,
    dirname(__DIR__) . '/lead-config.php',
]);
$config = null;
foreach ($configPaths as $path) {
    if (is_readable($path)) { $config = require $path; break; }
}
if (!is_array($config)) {
    error_log('send-lead.php: lead-config.php not found');
    respond(500, ['ok' => false, 'error' => 'not_configured']);
}

// ---------------------------------------------------------------- helpers
function field(string $name, int $max): string {
    $v = isset($_POST[$name]) && is_string($_POST[$name]) ? $_POST[$name] : '';
    $v = strip_tags($v);
    $v = preg_replace('/[\x00-\x09\x0B-\x1F\x7F]/u', '', $v);   // drop control chars (keep newlines)
    $v = trim(preg_replace("/\r\n?/", "\n", $v));
    return mb_substr($v, 0, $max);
}
function one_line(string $v): string {
    return trim(preg_replace('/\s+/u', ' ', $v));
}

// ---------------------------------------------------------------- spam checks
// Honeypot: a hidden field people never see. Bots fill it in. Pretend success so they move on.
if (field('company_website', 200) !== '') {
    respond(200, ['ok' => true]);
}
// Too fast to be a person (form filled in under 3 seconds).
$elapsed = (int) field('formElapsed', 12);
if ($elapsed > 0 && $elapsed < 3000) {
    respond(200, ['ok' => true]);
}

// ---------------------------------------------------------------- validate
$name    = one_line(field('fullName', 80));
$phoneD  = preg_replace('/\D/', '', field('phone', 30));
if (strlen($phoneD) === 11 && $phoneD[0] === '1') { $phoneD = substr($phoneD, 1); }
$zip     = preg_replace('/\D/', '', field('zip', 10));
$type    = one_line(field('projectType', 80));
$details = field('projectDetails', 1000);
$source  = one_line(field('sourcePage', 80)) ?: 'Website';

$errors = [];
if (mb_strlen($name) < 2)      $errors[] = 'fullName';
if (strlen($phoneD) !== 10)    $errors[] = 'phone';
if (strlen($zip) !== 5)        $errors[] = 'zip';
if ($details === '')           $errors[] = 'projectDetails';
if ($errors) {
    respond(422, ['ok' => false, 'error' => 'invalid', 'fields' => $errors]);
}
$phonePretty = sprintf('(%s) %s-%s', substr($phoneD, 0, 3), substr($phoneD, 3, 3), substr($phoneD, 6));

// ---------------------------------------------------------------- rate limit (per visitor)
$limit  = (int) ($config['rate_limit_per_hour'] ?? 5);
$ipHash = hash('sha256', ($_SERVER['REMOTE_ADDR'] ?? 'unknown') . '|ccp-leads');
$rlFile = rtrim(sys_get_temp_dir(), '/') . '/ccp-lead-' . substr($ipHash, 0, 32) . '.json';
$now    = time();
$hits   = [];
if (is_readable($rlFile)) {
    $hits = json_decode((string) file_get_contents($rlFile), true) ?: [];
    $hits = array_values(array_filter($hits, fn($t) => is_int($t) && $t > $now - 3600));
}
if (count($hits) >= $limit) {
    respond(429, ['ok' => false, 'error' => 'rate_limited']);
}
$hits[] = $now;
@file_put_contents($rlFile, json_encode($hits), LOCK_EX);

// ---------------------------------------------------------------- build the message
$firstName = explode(' ', $name)[0];
$lines = [
    "Name: $name",
    "Phone: $phonePretty",
    "ZIP: $zip",
    'Project: ' . ($type !== '' ? $type : 'Not specified'),
    "Page: $source",
    '',
    $details,
];
$message = implode("\n", $lines);
$sent = [];

// ---------------------------------------------------------------- 1) Pushover notification
if (!empty($config['pushover_token']) && !empty($config['pushover_user'])) {
    $payload = [
        'token'     => $config['pushover_token'],
        'user'      => $config['pushover_user'],
        'title'     => 'New lead: ' . ($type !== '' ? $type : $name),
        'message'   => $message,
        'url'       => 'tel:+1' . $phoneD,
        'url_title' => "Call $firstName",
        'priority'  => (int) ($config['pushover_priority'] ?? 0),
    ];
    if (!empty($config['pushover_sound'])) { $payload['sound'] = $config['pushover_sound']; }
    $ch = curl_init($config['pushover_url'] ?? 'https://api.pushover.net/1/messages.json');
    curl_setopt_array($ch, [
        CURLOPT_POST           => true,
        CURLOPT_POSTFIELDS     => $payload,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_TIMEOUT        => 10,
    ]);
    $resp   = curl_exec($ch);
    $status = (int) curl_getinfo($ch, CURLINFO_HTTP_CODE);
    curl_close($ch);
    if ($status === 200) {
        $sent[] = 'push';
    } else {
        error_log("send-lead.php: Pushover failed (HTTP $status): " . substr((string) $resp, 0, 300));
    }
}

// ---------------------------------------------------------------- 2) email copy (optional)
if (!empty($config['email_to']) && !empty($config['email_from'])) {
    $subject = 'New website lead: ' . $name . ($type !== '' ? " - $type" : '');
    $subject = '=?UTF-8?B?' . base64_encode($subject) . '?=';
    $headers = [
        'From: ' . ($config['email_from_name'] ?? 'Website Leads') . ' <' . $config['email_from'] . '>',
        'Content-Type: text/plain; charset=UTF-8',
        'X-Mailer: send-lead.php',
    ];
    $body = $message . "\n\nCall: tel:+1$phoneD\nReceived: " . date('D, M j Y g:i a T');
    if (@mail($config['email_to'], $subject, $body, implode("\r\n", $headers), '-f' . $config['email_from'])) {
        $sent[] = 'email';
    } else {
        error_log('send-lead.php: mail() failed');
    }
}

if (!$sent) {
    respond(502, ['ok' => false, 'error' => 'delivery_failed']);
}
respond(200, ['ok' => true]);
