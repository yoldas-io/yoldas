# Is Yoldaş safe?

You should know what an app you install in your car does. On this page, we explain in plain language what data Yoldaş collects, where it sends it, and how it protects it.

Last updated: October 15, 2026

## What data is sent?

Sharing of readings only turns on **with your consent**; location needs a separate consent. If you agree, the following goes to the Yoldaş server:

- Car readings: values such as battery, range, speed, tire pressure, 12 V battery and consumption.
- Events: locking, doors, trunk, switching between parking and driving, start and end of charging.
- Sentry events: time, type, direction, approximate angle, proximity class, Sentry state, model version and file summary.
- Location (with separate consent): for trip routes and "where is my car".
- Car profile: model code and software version.
- For connection diagnostics: the Wi-Fi network name and the car's local network address.

Short diagnostic events such as install, consent, helper and transition steps are sent without waiting for approval, to find the cause of problems. Personal data is filtered out of these events.

## What is not sent?

- **VIN.** It stays in the car. For the license, only a one-way hash created from it is used.
- **Camera recordings.** They stay in the car and are not uploaded to the server on their own. On your phone, only the recording you choose is fetched from the car, when you want.
- **Live video.** It passes through the server but is not stored.
- **Sentry images.** The small images it checks are not written to disk or the cloud; only the event's details go to the server (see the list above). No face, image box or person identity is sent.

## How is data protected?

- All connections are encrypted with HTTPS, and browsers are told to use HTTPS only (HSTS).
- Account passwords are never stored in plain text; they are stored with a strong hashing method (PBKDF2).
- The content of notifications sent to your phone is encrypted with a key unique to your phone.
- The admin panel is closed to the internet; it can only be opened through a secure tunnel to the server.
- Each account sees only its own car's data.

## Live camera and phone commands

- Only the account that owns the car can watch the cameras; one viewing session at a time, for up to 10 minutes.
- For viewing, the car must be connected to the internet, "Phone control" must be on and the license active; the camera and display-over-other-apps permissions must also be granted.
- The red "live view on" sign and the Stop button on the car screen are hidden by default. If you turn them on under Security › Recording and protection, they are drawn while someone is watching.
- Listening to the cabin and talking to the car are each turned on with a separate permission.
- Phone commands are single-use and valid for up to 60 seconds. Every command and its result is logged.
- Phone commands that control the car need a safe-use approval; without it the command is rejected (stop commands are excepted). The approval's version, text summary and time are recorded; deleting history does not delete this record.
- While Phone control and the Yoldaş helper are on, the connection continues after the car is switched off; it is released if the battery or the 12 V battery falls below a lower limit you set (by default there is no limit).
- If System › Phone control is turned off in the car, no phone command works.

## Signed updates

All Yoldaş versions are signed with the same key. Before installing, automatic updates check the file's integrity, package name, version number and signature; an older version is never installed as if it were new. Updates download only over HTTPS and over Wi-Fi or the car's own mobile data (not while roaming). The latest APK is always on the [download page](https://yoldas.io/en/download); you can verify the file's hash with the [SHA-256 guide](https://yoldas.io/en/guides/verify-apk-sha256).

## Permissions the app asks for
PermissionWhat for CameraCamera view, recording, live view and Sentry. MicrophoneOnly if you turn on listening to the cabin or talking to the car; also for dashcam recording with sound. LocationTrip routes and the car's last location. With separate consent. Display over other appsThe live view sign, the turn camera and the info strip. Installing appsInstalling the new version it downloads when it updates itself. Battery optimization exemptionRunning in the background without being cut off. Phone stateSeeing the state of the car's mobile data connection (including roaming) to diagnose connection problems. Start on boot, stay awakeStarting Yoldaş when the car turns on and keeping the device briefly awake while work is in progress. Accessibility services (two)One fixes the automatic start permission that is reset after a car update. The other reads the verification screen on the car and completes the setup only when you start preparing the connection. No credentials are saved or sent. NotificationsA persistent notification showing that the app is running in the background.

You can lock Yoldaş with a PIN on the car screen (System › App lock).

## Deleting your data

In the Account section of the phone app, **"Delete this car's history"** deletes the readings, trip summaries and routes, the car's last status, events and charging records from the server; backup and location consent are also turned off. Your preferences, the command log, notification history, the diagnostic log and approval records are not deleted by this action. To have your account deleted completely, write to us: [iletisim@yoldas.io](mailto:iletisim@yoldas.io). Your rights regarding personal data are on the [privacy page](https://yoldas.io/en/privacy).

If you find a security vulnerability, please report it to us first: [iletisim@yoldas.io](mailto:iletisim@yoldas.io).

## Frequently asked questions

### Does Yoldaş send my car's VIN?

No. The VIN stays in the car. For the license, only a one-way hash created from the VIN is used.

### Does camera video go to the server?

Recordings stay in the car and are not uploaded on their own. During live view, video only passes through the server and is not stored. The small images Sentry Mode checks are not written anywhere.

### How do I delete my data?

In the Account section of the phone app, "Delete this car's history" deletes readings, trips, events and charging records from the server. To have your account deleted completely, write to us.
