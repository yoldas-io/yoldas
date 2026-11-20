# Installing apps on Sealion 7 and DiLink 5 (APK)

On the BYD Sealion 7, Tang 2025 and newer cars with DiLink 5, the way to install apps is different from DiLink 3. This guide explains how to recognize DiLink 5, the two install paths BYD owners use and the settings you need to turn on after installing.

Last updated: November 20, 2026

## Is your car DiLink 5?

Look at the multimedia software version in the system information section of the car settings:

- **If it starts with 51** (for example 51.1.2.2411280.1): DiLink 5. The Sealion 7 and Tang 2025 are in this group.
- **If it starts with 23:** the DiLink 5 group seen on some Seal and Seal U cars built in 2025.
- **If it starts with 13:** DiLink 3; see the [APK not installing guide](https://yoldas.io/en/guides/byd-apk-not-installing).

Depending on the model, DiLink 5 cars use Android 11 or 12. Yoldaş works in both groups; it chooses the DiLink 5 path by itself from the version number ([DiLink 3, 4 and 5 guide](https://yoldas.io/en/guides/byd-dilink-3-4-5)).

## Path 1: USB folder (no computer)

According to BYD owners, this is the path that works on Global and Turkish software starting with 51:

1. **Prepare the folder**

In the root of a USB stick, create a folder named with your country code: for Türkiye "Third Party Apps 90". Get the Yoldaş APK from the [download page](https://yoldas.io/en/download) and put it in this folder.
2. **Plug in the stick**

Plug in the stick while the car is on and in P. The car asks for a password; the password is BYD service information, and we do not publish it on the site. If you do not know it, write to us.
3. **Wait for the install**

Once the password is accepted, the car installs the apps in the folder. Open Yoldaş and grant the first-launch permissions.

It is reported that a permanent unlocker cannot be installed on DiLink 5; so you install other apps from the same folder too.

## Path 2: Hidden developer page and wireless ADB

A Sealion 7 owner in Australia reported that tapping repeatedly on the factory reset text on the software version screen opens a hidden developer page. The same menus were also seen on cars in Morocco and Germany. From this page, wireless ADB can be turned on and apps can be installed from a computer with `adb install`.
**Do not touch the reset buttons**

The two blue reset buttons on the hidden page return the car to factory settings. Use only the debugging switches.

According to the same report, on that car wireless ADB turns off by itself after parking, and installs from the screen are refused as an "unknown source"; ADB has to be turned on again each time.
**Yoldaş works on DiLink 5 too**

On the Sealion 7 and other BYDs with DiLink 5, Yoldaş brings Sentry, recording with the car's cameras, a map on the instrument cluster and control from your phone together in one app.

[Download Yoldaş](https://yoldas.io/indir/yoldas-arac-321.apk) [Yoldaş and the Sealion 7](https://yoldas.io/en/byd-sealion-7)

## Settings to turn on after installing

- **Background operation:** in the BYD settings, the options that disable background apps and automatic start for Yoldaş must be off. In Yoldaş, check the **System › Background operation** card.
- **Sleep:** the DiLink 5 head unit goes to sleep about 10 minutes after the car is switched off; after that, no app runs.
- **Mobile data:** on some DiLink 5 software, mobile data is restricted for apps installed later. If the phone connection does not come through, connect the car to Wi-Fi, try again and write to us.
- **Phone:** open app.yoldas.io and scan the QR code on the car screen.

## European software (OTA 3.3)

We have not found a reliable install report for Sealion 7 cars sold in Europe with OTA 3.3. If your car is in this group and you have tried a path or got stuck, write to [iletisim@yoldas.io](mailto:iletisim@yoldas.io); we will update the guide together with you.

## Sources

- A BYD owners' forum, installing apps on the Sealion 7: [byd.forum](https://byd.forum/topic/8-sealion-7-installing-apps/)
- Developer page notes for the Sealion 7 in Australia: [github.com/jasoisjaso/byd-sealion7](https://github.com/jasoisjaso/byd-sealion7)

## Frequently asked questions

### Can apps be installed on a Sealion 7?

Yes. According to BYD owners, on Sealion 7 and Tang cars with software starting with 51 (Global and Turkish versions), apps are installed without a computer through the USB folder path.

### Do I need ADB on DiLink 5?

Not for the USB folder path. A hidden developer page that turns on wireless ADB has also been reported; but the reset buttons on that page return the car to factory settings, so be careful.

### How does Yoldaş get updates on DiLink 5?

Yoldaş downloads its new versions by itself. If your car's software refuses installs from the screen, you also do the update through the same USB folder path: put the new APK in the folder and plug in the stick.

### Can apps be installed on a Sealion 7 with European software?

We have not found a reliable install report for European cars with OTA 3.3. If your car is in this group, write to us with your software version.

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
