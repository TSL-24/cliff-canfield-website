<?php
/**
 * Settings for the website quote form (send-lead.php).
 *
 * HOW TO INSTALL (one time):
 *   1. In cPanel, open File Manager and go to your HOME folder (the one that CONTAINS public_html,
 *      not public_html itself).
 *   2. Create a new file named:  lead-config.php
 *   3. Paste this whole file into it, fill in the values below, and save.
 *
 * Never put this file inside public_html and never commit the filled-in version to GitHub.
 */
return [
    // Pushover (https://pushover.net) - push notifications to your phone
    'pushover_user'     => 'PASTE_YOUR_USER_KEY',        // shown on your Pushover dashboard
    'pushover_token'    => 'PASTE_YOUR_APP_API_TOKEN',   // from "Create an Application/API Token"
    'pushover_priority' => 0,      // 0 = normal, 1 = high (alerts even during quiet hours)
    'pushover_sound'    => '',     // optional, e.g. 'cashregister'; blank = your default sound

    // Email copy of each lead (optional - leave email_to blank to turn off)
    'email_to'          => '',     // where leads are sent, e.g. 'cliff@example.com'
    'email_from'        => '',     // an address ON YOUR DOMAIN, e.g. 'leads@yourdomain.com'
    'email_from_name'   => 'Website Leads',

    // Spam protection: max form submissions per visitor per hour
    'rate_limit_per_hour' => 5,
];
