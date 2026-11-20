# How to verify the SHA-256 hash of an APK file

A SHA-256 hash is a fingerprint of a file. Yoldaş publishes the hash of every version on the download page. If you calculate the same hash from the file you downloaded and compare the two, you know that the file you have is identical to the one that was published.

Last updated: October 6, 2026

## Why verify it?

- **A damaged download:** if the file downloaded only partly or with errors, the hash comes out different, so you notice before an install error appears.
- **A different file:** you confirm that a file you brought in on a USB stick or in some other way is the published file.

The current hash value is published only on the [download page](https://yoldas.io/en/download). We do not write it in this guide so that it never goes out of date.

## Step by step

1. **Find the published hash**

In the "File fingerprint (SHA-256)" box on the [download page](https://yoldas.io/en/download) you will see a 64-character hash. You can copy it with the Copy button.
2. **Download the APK to your computer**

Download the APK only with the download button on that same page, and note where the file is saved.
3. **Calculate the hash**

Run the command that fits your computer (the commands are in the table below). The command prints a 64-character value.
4. **Compare the two values**

The calculated value and the value on the page must match letter for letter. Some tools print capital letters; ignore upper and lower case.
5. **Go on based on the result**

If the values match, you can install the file. If they differ, delete the file and download it again; if they still differ, do not install it and write to us.

## Commands to calculate the hash

Replace the file name in the command with the name of your own file. Run the command in the folder where the APK is.
SystemCommand Windows (PowerShell)`Get-FileHash .\your-downloaded-file.apk -Algorithm SHA256` Windows (Command Prompt)`certutil -hashfile your-downloaded-file.apk SHA256` macOS`shasum -a 256 your-downloaded-file.apk` Linux`sha256sum your-downloaded-file.apk`

## What the hash shows and what it does not

- **It shows:** that the file is the same as the file on the page where the hash is published.
- **It does not show:** that the page itself is genuine. That is why you should get the APK and the hash only from yoldas.io, over HTTPS.

## Updates also have their signature checked

All Yoldaş versions are signed with the same key. When Yoldaş updates itself, it checks the file's integrity, package name, version number and signature before installing; it never installs an older version as if it were new. Details are on the [security page](https://yoldas.io/en/security).

Advanced users who want to can compare the signing certificate of two versions with the `apksigner verify --print-certs` command from the Android SDK Build-Tools; because they are signed with the same key, the certificate information should come out the same.

## Next step

Once the hash matches, you can install the file in the car: [install an APK from a USB stick](https://yoldas.io/en/guides/install-apk-byd-usb) or the [guide to installing apps on a BYD](https://yoldas.io/en/install).

## Frequently asked questions

### What is a SHA-256 hash?

It is a 64-character fingerprint calculated from the contents of a file. If even a single byte in the file changes, the hash changes completely. The same file always gives the same hash.

### What should I do if the hashes do not match?

Do not install the file. Delete it and download it again from the download page. If they still do not match, check your connection and that the address is yoldas.io; if the problem continues, write to us.

### Can I verify the hash on the car screen?

The commands in this guide are for a computer. The easiest way is to download the APK on your computer, verify it there and then take it to the car on a USB stick.

### Is there a hash for the phone app too?

No. The phone side is a web app, so there is no file to install. The hash is only for the car APK.

## Other guides

### [Do BYD cameras record?](https://yoldas.io/en/guides/does-byd-record-dashcam)

Which models have BYD's own recorder, why the 360° cameras don't record, and recording with all four cameras without buying a dashcam.

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

### [Installing an APK on a BYD from a USB stick](https://yoldas.io/en/guides/install-apk-byd-usb)

Copy the APK to a USB stick on your computer and open it on the car screen. Step by step, with the permission prompt and common problems.

### [How to choose a car app for your BYD](https://yoldas.io/en/guides/choose-car-app-byd)

A checklist for recording reliability, where data stays, language, installation and update signing.

### [Automations: what they do and how to use them](https://yoldas.io/en/guides/how-to-use-automations)

Learn what triggers, conditions and steps mean, how to set up your first automation and how to import one from a file.

### [Charging price and trip cost](https://yoldas.io/en/guides/charging-price-and-trip-cost)

Enter a price for each charge and see trip cost based on what you actually paid.
