# APK not installing on a BYD: causes and fixes

Did you get a message like "install blocked" when installing an app on your BYD screen? This guide explains what the messages mean, what changed in which software version and the ways BYD owners install apps on a locked screen.

Last updated: November 20, 2026

## In short: the problem is not the file but the software version

Since software 2310, released at the end of 2023, BYD has restricted installing apps from outside on the DiLink screen. On 2307 and earlier, an APK is opened from the file manager and installs directly. On later versions BYD's installer refuses the install; even if the file is fine, another path is needed.

First find your multimedia software version: the long number in the system information section of the car settings, for example `13.1.33.2606100.1`. The first four digits of the fourth group (here 2606) are the software's date. Details in the [DiLink 3, 4 and 5 guide](https://yoldas.io/en/guides/byd-dilink-3-4-5). If your software starts with 51, go to the [Sealion 7 and DiLink 5 guide](https://yoldas.io/en/guides/sealion-7-dilink-5-install-apps).

## Depending on the message you see

### "For your driving safety and system stability, please do not install third party apps"

BYD's own installer is refusing the install. There is nothing wrong with the file; your software has closed installs from outside. Go to the "Install paths for a locked screen" section below.

### "App not installed"

The file may not have downloaded completely, or an app with the same name but a different signature is already installed. Download the APK again from the [download page](https://yoldas.io/en/download), [verify its SHA-256 hash](https://yoldas.io/en/guides/verify-apk-sha256), and if there is an old copy installed from another source, uninstall it first.

### "No app in the allow list" when trying the USB folder

The password was accepted, but your country's allow list does not include this app. According to BYD owners, on newer DiLink 3 versions the USB folder path mostly gets stuck here. In that case, switch to the service menu path.

### The download does not start in the car's browser

On some versions (reported example: the 2507 group), files downloaded in the car's browser are silently blocked. Copy the APK to a USB stick on a computer.

### No "Install" button, or it is greyed out

This also shows that the installer is refusing the install. Go to the install paths for a locked screen.

## What works on which software version?

BYD does not publish an official table on this. The table below was compiled from what BYD owners have reported on forums and in guides; it may be different on your car.
Software (DiLink 3/4)USB stick, file managerUSB folder and passwordADB from the service menu 2307 and earlierWorksNot neededNot needed 2310 – 2501RefusedMostly worksWorks 2503 and laterRefusedVaries by market, mostly blocked by the allow listWorks; some cars ask for QR approval

## Install paths for a locked screen

### 1. USB folder and password

In the root of the USB stick, a folder named with your country code is created (for Türkiye "Third Party Apps 90") and the APK is put inside it. When the stick is plugged in, the car asks for a password and installs the apps in the folder. The password is BYD service information; we do not publish it on the site. On newer versions this path may be blocked by the allow list.

### 2. Wireless debugging (ADB) from the service menu

This is the path BYD owners use most:

1. **Open the service menu**

BYD's developer tools open with a service code entered on the car's phone keypad.
2. **Enter the password**

The menu asks for a password tied to the car's IMEI number and clock. The car clock must be correct. On some cars (mostly for the Chinese market) a QR code appears on the screen instead of a password, and remote approval is needed.
3. **Turn on wireless ADB**

On the Test Tools screen that opens, turn on the wireless ADB and USB debugging switches.
4. **Install from a computer**

With the computer and the car on the same Wi-Fi, run the commands `adb connect CAR-ADDRESS:5555` and `adb install yoldas-arac.apk`. Details in the [install guide](https://yoldas.io/en/install).

Do not give your IMEI to people or websites you do not know. Once Yoldaş is installed, it generates this password inside the car by itself and prepares the helper connection; the IMEI and the password are not sent anywhere ([Debug mode and the Yoldaş helper](https://yoldas.io/en/install#debug-kurulumu)).

### 3. Downgrading

Some BYD owners roll the car back to older software from USB, install the apps and then update again. During this process the screen may not come on and the multimedia settings are reset; some USB sticks cannot start a rollback from newer versions. Yoldaş does not recommend this path. If the other paths did not work, write to us first.
**Install it once, let Yoldaş do the rest**

Once installed, Yoldaş downloads and installs its own new versions, so you don't have to go through these paths with every update. Home screen, Sentry, four-camera recording and the phone app, all in one app.

[Download Yoldaş](https://yoldas.io/indir/yoldas-arac-321.apk) [All features](https://yoldas.io/en/features)

## After installation

- In the BYD settings, the settings that block background operation and automatic start for Yoldaş must be off; Yoldaş fixes this by itself on most cars.
- BYD updates mostly leave installed apps in place but may close the install path. What to do before an update is in the [BYD software update guide](https://yoldas.io/en/guides/byd-software-update).
- Yoldaş downloads and installs its later versions by itself; you do not need to repeat these paths for every update.

If you are stuck, write to [iletisim@yoldas.io](mailto:iletisim@yoldas.io) with your multimedia software version and the message you see.

## Sources

- BYD Club Italia install guide (the 2307/2310 boundary): [byd-club-italia.github.io](https://byd-club-italia.github.io/byd-club-italia-guides/generale.html)
- A technical study of the Dolphin multimedia unit (browser block, allow list): [github.com/wheregoes/byd-dolphin-hacking](https://github.com/wheregoes/byd-dolphin-hacking)
- A BYD owners' forum (installing on the Sealion 7 and DiLink 5): [byd.forum](https://byd.forum/topic/8-sealion-7-installing-apps/)

## Frequently asked questions

### Why won't an APK install on my BYD?

Since software 2310, BYD has restricted installing apps from outside on the DiLink screen. On 2307 and earlier, an APK installs straight from the file manager; on later versions BYD's installer refuses the install and another path is needed.

### Is "sha256 is invalid" a BYD error?

No such message has been reported from BYD's installer; the phrase appears online in the install tools of other devices. To make sure the Yoldaş file you downloaded is not corrupted, verify its hash as shown in the SHA-256 guide.

### Do I need to downgrade the car's software to install?

Usually not. Some BYD owners downgrade, but the screen can get stuck during this process and the multimedia settings are reset. Yoldaş does not recommend this path; try the other paths below first, or write to us.

### Do the apps I installed stay after a BYD update?

According to BYD owners, installed apps mostly stay after regular updates; they can be removed in major version changes and in updates done at the dealer. The install path can also close. Details are in the BYD software update guide.

### Is it safe to give my IMEI to someone else?

The service menu password is tied to the IMEI. Do not give your IMEI to people or websites you do not know. Once Yoldaş is installed, it generates this password inside the car by itself; the IMEI and the password are not sent anywhere.

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
