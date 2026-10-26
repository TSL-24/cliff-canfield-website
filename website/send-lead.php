<?php
/**
 * Cliff Canfield Plumbing — quote form handler.
 *
 * Receives the website quote form, blocks spam, and emails the lead to LEAD_EMAIL_TO.
 * Uses your hosting's built-in mail, so no outside service or account is needed.
 */

const LEAD_EMAIL_TO   = 'leads@cliffcanfieldplumbing.com';   // where leads are delivered
const LEAD_EMAIL_FROM = 'leads@cliffcanfieldplumbing.com';   // must be an address on your domain
const LEAD_FROM_NAME  = 'Cliff Canfield Plumbing Website';
const RATE_LIMIT_PER_HOUR = 5;                               // max submissions per visitor per hour

date_default_timezone_set('America/New_York');

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
$ipHash = hash('sha256', ($_SERVER['REMOTE_ADDR'] ?? 'unknown') . '|ccp-leads');
$rlFile = rtrim(sys_get_temp_dir(), '/') . '/ccp-lead-' . substr($ipHash, 0, 32) . '.json';
$now    = time();
$hits   = [];
if (is_readable($rlFile)) {
    $hits = json_decode((string) file_get_contents($rlFile), true) ?: [];
    $hits = array_values(array_filter($hits, fn($t) => is_int($t) && $t > $now - 3600));
}
if (count($hits) >= RATE_LIMIT_PER_HOUR) {
    respond(429, ['ok' => false, 'error' => 'rate_limited']);
}
$hits[] = $now;
@file_put_contents($rlFile, json_encode($hits), LOCK_EX);

// ---------------------------------------------------------------- email the lead
$subject = 'New website lead: ' . $name . ($type !== '' ? " - $type" : '');
$body = implode("\n", [
    'New quote request from the website',
    '',
    "Name:     $name",
    "Phone:    $phonePretty",
    "ZIP:      $zip",
    'Project:  ' . ($type !== '' ? $type : 'Not specified'),
    "Page:     $source",
    '',
    'Details:',
    $details,
    '',
    '---',
    "Call back: tel:+1$phoneD",
    'Received: ' . date('D, M j, Y g:i a T'),
]);
$headers = implode("\r\n", [
    'From: ' . LEAD_FROM_NAME . ' <' . LEAD_EMAIL_FROM . '>',
    'MIME-Version: 1.0',
    'Content-Type: text/plain; charset=UTF-8',
    'Content-Transfer-Encoding: 8bit',
    'X-Mailer: send-lead.php',
]);
$encodedSubject = '=?UTF-8?B?' . base64_encode($subject) . '?=';

if (!@mail(LEAD_EMAIL_TO, $encodedSubject, $body, $headers, '-f' . LEAD_EMAIL_FROM)) {
    error_log('send-lead.php: mail() failed');
    respond(502, ['ok' => false, 'error' => 'delivery_failed']);
}
respond(200, ['ok' => true]);
