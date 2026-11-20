# BYD software update: what happens to your installed apps?

BYD sends software updates (OTA) to your car from time to time. They can remove apps you installed yourself or reset their settings. This guide explains what to save before an update and how to bring Yoldaş back in a few minutes afterwards.

Last updated: November 20, 2026

## Two different version numbers

Two numbers on a BYD are often confused:

- **OTA version:** the package name shown in the update notice (such as V2.0 or V2.2). It describes the car's whole software package.
- **Multimedia software version:** the long number in the system information section of the car settings, for example `13.1.33.2606100.1`. The first four digits of the fourth group (here 2606) show when the software was built; BYD owners usually refer to versions by these four digits.

The multimedia software version is the one that decides how apps behave. What its first digits mean is explained in the [DiLink 3, 4 and 5 guide](https://yoldas.io/en/guides/byd-dilink-3-4-5).

## What can an update do to installed apps?

What BYD owners report, and what we also see among Yoldaş users:

- **The app is removed.** An app you installed yourself disappears from the screen.
- **Permissions are reset.** Auto-start and background permissions go back to default, so the app no longer starts by itself when the car is switched on.
- **Debugging is switched off.** Developer options and wireless debugging can be turned off, which disconnects the Yoldaş helper.
- **The install route changes.** According to BYD owners, some updates made it harder to install apps from outside.

Not every update does all of this. BYD's release notes don't mention these points, so being prepared is the safest approach.

## Before the update: five minutes of preparation

1. **Write down your software version**

Note the multimedia software version from the system information section of the car settings, or take a photo of it. The Compatibility report under **System › Diagnostics and logging** in Yoldaş shows it too.
2. **Copy important recordings to your phone**

Camera recordings stay in the car. Open any recording you want to keep in the phone app and download it as MP4.
3. **Check that your phone is paired**

Open app.yoldas.io on your phone and check that your car's data is arriving. That way your trips, charging sessions and preferences are backed up on the server.
4. **Keep Yoldaş up to date**

Make sure Yoldaş is on the latest version. The current APK is always on the [download page](https://yoldas.io/en/download); you can also copy the file to a USB stick.

## After the update: bring Yoldaş back

1. **Is Yoldaş still there?**

If Yoldaş opens, check the **System › Background operation** card. Yoldaş tries to fix a reset auto-start permission by itself; if it didn't, switch it on there.
2. **If it's gone, reinstall it**

Get the APK from the [download page](https://yoldas.io/en/download) and install it as in the [installation guide](https://yoldas.io/en/install). Step-by-step instructions are in the [USB installation guide](https://yoldas.io/en/guides/install-apk-byd-usb).
3. **Pair your phone again**

Scan the QR code on the car screen with your phone. Your history and preferences on the server come back with the same account.
4. **Check the Yoldaş helper**

If **System › Yoldaş helper** doesn't say "Connected", repeat the [helper steps](https://yoldas.io/en/install#yardimci) in the installation guide. Cluster display and the custom bottom bar work through the helper.

If you can't reinstall it, write to [iletisim@yoldas.io](mailto:iletisim@yoldas.io) with your multimedia software version. We'll tell you which way works for your version.

## Yoldaş's own updates

New Yoldaş versions are separate from BYD updates. Yoldaş downloads its own version over Wi-Fi or the car's mobile data, checks its signature and installs it; it does not touch the car's software. Details are on the [download page](https://yoldas.io/en/download) and changes in the [release notes](https://yoldas.io/en/release-notes).

## Frequently asked questions

### Does a BYD update delete Yoldaş?

It can. Some BYD updates remove apps installed afterwards or reset their permissions. If Yoldaş disappears, reinstall it and pair it with your phone again.

### Will I lose my trip and charging history after an update?

No. If your phone is paired, your trips, charging sessions and preferences are backed up on the server. They come back when you reinstall Yoldaş and pair it with the same account.

### Will my camera recordings be deleted?

Recordings stay in the car, in Yoldaş's own folder, and are not uploaded to the server automatically. BYD does not say what an update does to that folder, so copy important recordings to your phone before updating.

### Are the OTA version and the multimedia software version the same?

No. The OTA version shown in the update notice (such as V2.2) is the name of the car's whole package. The multimedia software version is the long number in the system information (such as 13.1.33.2606100.1). The second one decides how apps behave.

### I can't reinstall Yoldaş after the update. What should I do?

Write to us with your multimedia software version. We'll tell you which way works for your version.

### Is Yoldaş's own update the same as a BYD update?

No. Yoldaş downloads and installs its own new versions and does not touch the car's software. A BYD update changes the car's own software.

## Other guides

### [What are BYD DiLink 3, 4 and 5?](https://yoldas.io/en/guides/byd-dilink-3-4-5)

How to find your DiLink generation and software version, and what the first digits of the version decide in Yoldaş.

### [APK not installing on a BYD](https://yoldas.io/en/guides/byd-apk-not-installing)

What the error messages mean, what changed in versions after 2310 and how apps get installed on a locked screen.

### [Installing on Sealion 7 and DiLink 5](https://yoldas.io/en/guides/sealion-7-dilink-5-install-apps)

How to recognize DiLink 5, the two install paths BYD owners use and the settings to turn on after installing.

### [Installing an APK on a BYD from a USB stick](https://yoldas.io/en/guides/install-apk-byd-usb)

Copy the APK to a USB stick on your computer and open it on the car screen. Step by step, with the permission prompt and common problems.

### [How to verify an APK's SHA-256 hash](https://yoldas.io/en/guides/verify-apk-sha256)

Calculate the hash of the APK you downloaded on your computer and compare it with the value on the download page.

### [How to choose a car app for your BYD](https://yoldas.io/en/guides/choose-car-app-byd)

A checklist for recording reliability, where data stays, language, installation and update signing.

### [Automations: what they do and how to use them](https://yoldas.io/en/guides/how-to-use-automations)

Learn what triggers, conditions and steps mean, how to set up your first automation and how to import one from a file.

### [Charging price and trip cost](https://yoldas.io/en/guides/charging-price-and-trip-cost)

Enter a price for each charge and see trip cost based on what you actually paid.
