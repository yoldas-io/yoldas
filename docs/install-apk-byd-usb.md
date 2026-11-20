# How to install an app (APK) on a BYD from a USB stick

The BYD multimedia screen runs on Android, and apps are installed with an APK file. The easiest way is to copy the APK to a USB stick on your computer and open it on the car screen. This guide walks you through that way step by step.

Last updated: November 19, 2026

## Before you start

- **A computer and a USB stick.** You copy the APK to the stick on the computer.
- **The latest APK.** The file is always at [yoldas.io/en/download](https://yoldas.io/en/download). Do not install a file you got from another source.
- **Your car's software version.** Yoldaş recognizes your platform from the first digits of the version. To find out how to see it, read the [DiLink guide](https://yoldas.io/en/guides/byd-dilink-3-4-5).
- **The car in P.** You will need to tap the screen during installation.

## Step by step

1. **Download the APK to your computer**

From the [download page](https://yoldas.io/en/download), download the latest version of the Yoldaş car APK to your computer. If you like, [verify its SHA-256 hash](https://yoldas.io/en/guides/verify-apk-sha256).
2. **Copy the file to a USB stick**

Copy the APK file to a USB stick. When copying is done, safely eject the stick from your computer.
3. **Put the car in P and plug in the stick**

Keep the car in park (P) and plug the stick into the car's USB port. You will need to tap the screen during installation.
4. **Open the APK in Files**

In the file manager on the car screen (Files), find the USB stick and tap the APK file.
5. **Allow the install**

If you are asked to "Allow installs from unknown sources", allow it, then tap "Install".
6. **Open Yoldaş and grant permissions**

On first launch, Yoldaş asks for camera and audio permissions separately. Grant the permissions for the features you plan to use.
7. **Pair your phone**

Open app.yoldas.io on your phone, add it to your home screen and scan the QR code on the car screen.

## If the "Install" button does not appear

If the install window does not open when you tap the APK, or the "Install" button does not show, use the second way: installing from a computer with ADB. The developer settings and commands you need are in the [guide to installing apps on a BYD](https://yoldas.io/en/install) (option 2). The same page also covers the first settings after installation.

## After installation

- **Background operation:** in Yoldaş, open the **System › Background operation** card and turn on "Battery exemption" and "Automatic start support". This keeps data coming in without gaps.
- **Yoldaş helper:** for the cluster display, the custom bottom bar and the Sentry screen alert, it is set up from the car screen, with no computer. [Details](https://yoldas.io/en/install#yardimci)
- **Which features are on?** Your model's page tells you: [Seal](https://yoldas.io/en/byd-seal), [Atto 3](https://yoldas.io/en/byd-atto-3), [Dolphin](https://yoldas.io/en/byd-dolphin), [Seal U DM-i](https://yoldas.io/en/byd-seal-u-dm-i) and others.

## Common problems

### "App not installed" error

The file may have been copied or downloaded only partly. Download the APK again from the download page and copy it to the stick again. If an app with the same name was installed from another source, uninstall it first.

### The car does not see the stick

Remove the stick and plug it in again, or try a different USB stick. If that still does not work, use the ADB way.

### The app disappeared after a BYD update

Some BYD updates remove apps you installed yourself. Reinstall Yoldaş and pair it with your phone again. Your history and preferences backed up to the server stay where they are.

## Frequently asked questions

### Does installing from a USB stick work on every BYD?

It depends on the car's software version. If no "Install" button appears when you tap the APK in Files, you need to install from a computer with ADB; the steps are in the [app install guide](https://yoldas.io/en/install).

### Why is there no Google Play on a BYD?

The multimedia screen of BYD cars sold in Türkiye does not have Google Play. Apps are installed as APK files.

### How long does installation take?

Installing from the car screen takes a few minutes. Including pairing with your phone, you are done in about 10 minutes.

### How do updates arrive after a USB install?

Yoldaş downloads the new version by itself over Wi-Fi or the car's own mobile data and checks its signature; it does not use mobile data while roaming. If "Install without asking" is on, you don't have to touch anything; if it is off, you tap Android's "Install" once on the car screen. Yoldaş then restarts by itself. You do not need to plug the USB drive in again.

## Other guides

### [Do BYD cameras record?](https://yoldas.io/en/guides/does-byd-record-dashcam)

Which models have BYD's own recorder, why the 360° cameras don't record, and recording with all four cameras without buying a dashcam.

### [Best apps for BYD](https://yoldas.io/en/guides/best-apps-for-byd)

Apps that are useful on the BYD screen for maps, music, video, dashcam and control from your phone.

### [YouTube, Netflix, Google Maps on a BYD](https://yoldas.io/en/guides/byd-youtube-netflix-google-maps)

Which apps are built into the BYD screen and which you install; Google Maps on the instrument cluster, YouTube while charging.

### [BYD CarPlay and Android Auto](https://yoldas.io/en/guides/byd-carplay-android-auto)

Which BYDs connect wired or wireless, how to connect, and putting the CarPlay map on the cluster behind the steering wheel.

### [Does BYD have sentry mode?](https://yoldas.io/en/guides/does-byd-have-sentry-mode)

Which markets have BYD's own sentry mode and which don't; watching your parked car with Yoldaş.

### [APK not installing on a BYD](https://yoldas.io/en/guides/byd-apk-not-installing)

What the error messages mean, what changed in versions after 2310 and how apps get installed on a locked screen.

### [Before and after a BYD update](https://yoldas.io/en/guides/byd-software-update)

What a BYD update can do to installed apps, what to save before you install it and how to bring Yoldaş back afterwards.

### [BYD 360 camera](https://yoldas.io/en/guides/byd-360-camera)

Ways to open the 360° camera, the transparent chassis view, and watching and recording all four cameras from your phone.

### [BYD 12 V battery dead](https://yoldas.io/en/guides/byd-12v-battery)

What happens when the 12 V battery dies, how to get in, when BYD charges it on its own, and keeping an eye on the voltage.

### [BYD tyre pressure](https://yoldas.io/en/guides/byd-tyre-pressure)

Recommended cold tyre pressures model by model (bar, kPa, psi) and how to see the pressure on the screen or on your phone.

### [BYD app not connecting](https://yoldas.io/en/guides/byd-app-not-connecting)

What to try against car-adding, connection and service errors in the official BYD app; a phone app independent of BYD.

### [Installing on Sealion 7 and DiLink 5](https://yoldas.io/en/guides/sealion-7-dilink-5-install-apps)

How to recognize DiLink 5, the two install paths BYD owners use and the settings to turn on after installing.

### [What are BYD DiLink 3, 4 and 5?](https://yoldas.io/en/guides/byd-dilink-3-4-5)

How to find your DiLink generation and software version, and what the first digits of the version decide in Yoldaş.

### [BYD screen rotation](https://yoldas.io/en/guides/byd-screen-rotation)

Ways to turn the rotating screen to landscape and portrait, which models have a rotating screen, and a shortcut for cars with no steering wheel button.

### [How to verify an APK's SHA-256 hash](https://yoldas.io/en/guides/verify-apk-sha256)

Calculate the hash of the APK you downloaded on your computer and compare it with the value on the download page.

### [How to choose a car app for your BYD](https://yoldas.io/en/guides/choose-car-app-byd)

A checklist for recording reliability, where data stays, language, installation and update signing.

### [Automations: what they do and how to use them](https://yoldas.io/en/guides/how-to-use-automations)

Learn what triggers, conditions and steps mean, how to set up your first automation and how to import one from a file.

### [Charging price and trip cost](https://yoldas.io/en/guides/charging-price-and-trip-cost)

Enter a price for each charge and see trip cost based on what you actually paid.

[Debug mode and the Yoldaş helper](https://yoldas.io/en/install#debug-kurulumu)
