# What are BYD DiLink 3, 4 and 5? Which version is on which model?

DiLink is the name of the Android-based platform on BYD's car screen. "3", "4" and "5" are generations of this platform. This guide explains what the generations mean, how to find your version and what Yoldaş does depending on the version number, with sources.

Last updated: November 19, 2026

## First, know this: the model name does not settle the version

BYD's official DiLink support page does not publish a table matching generations to models; the page only lists the platform's general features and the models that have DiLink. Community sources also list different generations for the same model depending on production year. So this guide does not look at a model name and say "this model has this version". The right way is to read your own car's software version, and you will find how below. Each model's own page has the platform and screen information Yoldaş has for that model.

## What is DiLink?

DiLink is the software platform of the touchscreen multimedia display in BYD cars. It is built on Android; car settings, apps, camera views and BYD's cloud services all go through this platform. BYD's own support page presents the platform under headings such as an Android-based smart system, a split-screen app view, light and dark themes and vehicle control over the cloud. Yoldaş is also an Android app that is installed on this screen.

## 3, 4 and 5: the generations

According to a community table, the generations break down as follows. Because there is no official table, read this as a guide to the direction rather than as an exact answer.
GenerationAndroid versionInterface version DiLink 3.0Android 104.0 and 5.0 DiLink 4.0Android 104.0 DiLink 5.0Android 12L5.0

It is worth noticing that 3.0 and 4.0 use the same Android version in the table: the difference between the two generations is mostly in the interface and the processor. Yoldaş looks not at the generation name but at the beginning of the software version: a version starting with 13 is recognized as DiLink 3, and one starting with 51 as DiLink 5. There is no separate path for DiLink 4.

## How do you find your version?

There are two separate numbers, and they are often confused:

- **Generation (3, 4, 5):** BYD's name for the platform. It is often not written anywhere on the car's screen.
- **Software version:** the long number in the system information section of the car settings. Example format: `13.1.33.2606100.1`. The first digits show the platform group; the last digits carry the build date and the release order.

Yoldaş's install guide also asks you to find your software version first: [Install apps on a BYD](https://yoldas.io/en/install). If Yoldaş is installed, the Compatibility report under **System › Diagnostics and logging** gathers the platform, the software version and the screen details in one place. The report contains no VIN, serial number or location.

## What do the first digits of the version number decide in Yoldaş?

Yoldaş decides the platform first by looking at the beginning of the software version. Observed examples:

- **Starting with 13.1.33:** the group read on the BYD Seal that Yoldaş is developed on (13.1.33.2606100.1).
- **Starting with 13.1.32:** this group appears in a published technical study of the Dolphin (13.1.32.2507250.1). Atto 3 and Dolphin owners are mostly in this group.
- **Starting with 51:** Yoldaş recognizes this as DiLink 5 and uses the DiLink 5 path. The Sealion 7 and some newer cars are on this platform.
Version numberCameras, dashcam, Sentry ModeWindow and other remote commandsCluster display Starts with 13 (DiLink 3)YesYesYes Starts with 51 (DiLink 5)YesYesYes

Features can differ slightly with the car's hardware and software version. If something does not work as you expect, write to us.

## Details for your model

The platform, software group, screen and supported features are written separately on each model page:

- [BYD Seal](https://yoldas.io/en/byd-seal), [Seal U EV](https://yoldas.io/en/byd-seal-u-ev) and [Seal U DM-i](https://yoldas.io/en/byd-seal-u-dm-i)
- [Atto 3](https://yoldas.io/en/byd-atto-3), [Atto 2](https://yoldas.io/en/byd-atto-2) and [Dolphin](https://yoldas.io/en/byd-dolphin)
- [Han](https://yoldas.io/en/byd-han) and [Tang](https://yoldas.io/en/byd-tang)
- [Sealion 7](https://yoldas.io/en/byd-sealion-7)

To see what the cluster feature does, see the [Cluster display](https://yoldas.io/en/cluster-display) page. If you are ready to install the app, the [guide to installing from a USB stick](https://yoldas.io/en/guides/install-apk-byd-usb) and the [download page](https://yoldas.io/en/download) are the next steps.

## Sources

- BYD's official DiLink support page (platform overview; no generation table): [byd.com/en-ma/support/dilink](https://www.byd.com/en-ma/support/dilink)
- A community table of DiLink generations (Android and interface versions): [bydhack.com/en/systems](https://bydhack.com/en/systems)
- A technical study of the Dolphin multimedia unit (DiLink 3.0, Android 10, an example software version): [github.com/wheregoes/byd-dolphin-hacking](https://github.com/wheregoes/byd-dolphin-hacking)
- Measurements taken from Yoldaş's development car (Seal, software 13.1.33.2606100.1).

## Frequently asked questions

### Are DiLink 3, 4 and 5 the same thing?

No. All three are generations of BYD's Android-based multimedia platform. The generation number affects the interface, the Android version and the processor. The same model name can come with a different generation depending on production year and market, so the exact answer is in your car's own system information.

### Where do I see the DiLink version on my BYD?

The multimedia software version is listed in the system information section of the car settings (for example in the form 13.1.33.2606100.1). Menu names can differ by model and software. In Yoldaş, the Compatibility report under System › Diagnostics and logging also shows the platform and the software version.

### My software version starts with 13. Will Yoldaş work?

Yes. On versions starting with 13, Yoldaş uses the DiLink 3 path: cameras, dashcam, Sentry Mode, cluster display and phone control all work.

### My software version starts with 51. What happens?

Yoldaş recognizes this version as DiLink 5 and uses the DiLink 5 path. Cameras, dashcam, Sentry Mode, cluster display and phone control work on this platform too.

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
