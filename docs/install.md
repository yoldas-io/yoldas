# How to install apps on a BYD (APK): step-by-step guide

The BYD DiLink multimedia screen runs on Android. Apps like Yoldaş are installed with an APK file. This guide covers both ways to install and the first settings to make afterwards.

Last updated: November 19, 2026

[Debug mode and the Yoldaş helper](#debug-kurulumu)

## Before you start

- **Find your software version.** The multimedia software version is listed in the system information section of the car settings (e.g. 13.1.33.2606100.1). You will find what the version number means in the [DiLink 3, 4 and 5 guide](https://yoldas.io/en/guides/byd-dilink-3-4-5).
- **Park the car in P.** You will need to tap the screen during installation.
- **Connect the car to Wi-Fi.** The car needs internet to download the APK and for Yoldaş to send data to your phone.
- **Get the file from Yoldaş.** The latest APK is always at [yoldas.io/en/download](https://yoldas.io/en/download). If you want to verify the file's hash, see the [SHA-256 guide](https://yoldas.io/en/guides/verify-apk-sha256).

## Option 1: Open the APK on the car screen

1. **Get the APK into the car**

Open the [download page](https://yoldas.io/en/download) in the car's browser, or copy the APK to a USB stick on your computer and plug it into the car.
2. **Open the file**

Tap the APK in the file manager (Files) on the car screen.
3. **Allow the install**

If you are asked to "Allow installs from unknown sources", allow it, then tap "Install".

This way has a short guide of its own: [install an APK from a USB stick](https://yoldas.io/en/guides/install-apk-byd-usb). If no "Install" button appears, use option 2.

## Option 2: Install from a computer with ADB

You need a computer on the same Wi-Fi network. ADB is Android's official developer tool (Android SDK Platform Tools).

1. **Turn on developer options**

Turn on developer options in the car settings, then turn on "USB debugging" and debugging over the network.
2. **Connect from your computer to the car**

Find the car's address on the network and type `adb connect CAR-ADDRESS:5555` on your computer. If the car screen asks "Allow debugging?", confirm.
3. **Install the APK**

Run `adb install -r your-downloaded-file.apk`. When you see "Success", installation is complete.

## After installation

1. **First-launch permissions**

On first launch, Yoldaş asks for camera and audio permissions separately. Grant the permissions for the features you plan to use.
2. **Background operation**

In Yoldaş, open the **System › Background operation** card and turn on "Battery exemption" and "Automatic start support". If BYD resets the automatic start permission after an update, Yoldaş tries to fix it by itself; if it does not get fixed, check this card. This keeps data coming in without gaps.
3. **Pair your phone**

Open app.yoldas.io on your phone, add it to your home screen and scan the QR code on the car screen.

## Yoldaş helper

The cluster display, the custom bottom bar, the Sentry screen alert and connectivity support while parked work through the Yoldaş helper. You set it up from the car screen, with no computer:

1. **Start it**

In Yoldaş, tap "Start" on the **System › Yoldaş helper** page.
2. **Give permission**

When Android's permission window opens, choose "Always allow" once. When the connection is made, the page says "Connected".
3. **Use it**

Once the helper has been opened, if the connection drops it is retried on its own. "Disconnect" turns it off whenever you like.

The helper only works with Yoldaş's fixed, approved list of commands; it does not accept general commands from outside. If Yoldaş stops or is removed, it undoes the system settings it changed.

### Connectivity while parked and after the car is off

While Phone control and the Yoldaş helper are on, Yoldaş provides CPU and Wi-Fi support on its own so the phone connection keeps going while the car is in P and after it is switched off. By default there is no limit on the battery or the 12 V battery ("No limit"). If you like, you can set a lower limit in the "Stay connected while the car is off" section in Yoldaş: 10% to 60% for the battery, 11 to 13 V for the 12 V battery. When the value falls below the limit, the connection stops by itself. With the charging cable plugged in, no limit is checked.

The connection also stops when the gear is not P or the speed is not zero, when the system is too hot, or when car data cannot be read. The reason for stopping is written in Yoldaş. If the car loses internet, Yoldaş tries to wake the car: every 30 seconds for the first 10 minutes, then every 2 minutes, for up to 6 hours.

If the app closes unexpectedly, the Yoldaş helper tries to restart it; this also applies while the car is on and while driving, with at most 6 attempts in 10 minutes. Even if you force-stop the app, the helper restarts it as long as it is connected. It is not restarted when you choose "Disconnect", or when the app is uninstalled or updated.

## Common problems

### "App not installed" error

The file may not have downloaded completely; download the APK again from the [download page](https://yoldas.io/en/download). If an app with the same name was installed earlier from another source, uninstall it first.

### No "Install" button

Install from a computer with ADB (option 2).

### Data on the phone is not updating

Complete the "Background operation" step above and check that the car is connected to the internet. In Yoldaş, the "Connection test" on the **System › Connection** card checks Wi-Fi and mobile data separately.

### The app disappeared after a BYD update

Reinstall Yoldaş and pair it with your phone again. Your history and preferences backed up to the server stay where they are. What to do before and after a BYD update: [BYD software update guide](https://yoldas.io/en/guides/byd-software-update).

If you have a question about your car, write to [iletisim@yoldas.io](mailto:iletisim@yoldas.io).

## Frequently asked questions

### Does a BYD have Google Play?

BYD multimedia screens do not have Google Play. Apps are installed as APK files.

### Do I need to reinstall Yoldaş after a BYD update?

Some BYD updates remove apps you installed yourself. If that happens, reinstall Yoldaş and pair it with your phone again. Your history and preferences backed up to the server stay where they are. When Yoldaş updates, BYD's automatic start permission may be reset; Yoldaş tries to fix this by itself.

### How do Yoldaş updates arrive?

Yoldaş downloads the new version by itself over Wi-Fi or the car's own mobile data and checks its signature; it does not use mobile data while roaming. If "Install without asking" is on, you don't have to touch anything; if it is off, you tap Android's "Install" once on the car screen. Yoldaş then restarts by itself; if the update resets the automatic start permission, Yoldaş tries to fix it by itself.

### How long does installation take?

Installing from the car screen takes a few minutes. Including pairing with your phone, you are done in about 10 minutes.

## Debug mode and the Yoldaş helper

From Yoldaş 0.12.67, supported BYD screens can receive a code calculated in the car. Follow these steps after installing Yoldaş. Park before setup.

1.

Open System → Yoldaş helper and tap Prepare connection.
2.

If permissions open, enable Yoldaş connection setup. Return and tap Prepare connection again. This permission reads and fills only the BYD setup you start.
3.

The BYD screen IMEI is read and the code is calculated locally. Neither is sent to the server. A rejected code is not retried automatically.
4.

In TestTools, check Wireless adb debug switch. Also enable Debug mode when USB is connected and read and accept any Android prompt. On first connection, select Always allow and approve.
5.

Return to Yoldaş and check Connected. If needed, tap Start or Reconnect. Yoldaş automatic start is separate and is managed after the helper connects.

### If automatic sign-in fails

Use Generate code in the helper. Enter the last 6 IMEI digits from BYD and type the Now code into its password field. The car clock must be correct. Do not repeatedly retry rejected codes; contact support. Labels vary by firmware.

### Removing permission

In BYD Settings → Accessibility services, turn off Yoldaş connection setup. This does not turn off debugging. Other installed apps also appear; you do not need to change them.
