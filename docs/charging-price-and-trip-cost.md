# Charging price and trip cost: how to use

Every charge costs something different: cheap at home, expensive at a fast charger. In Yoldaş you can enter your own price per kWh for each charge, and trip cost is calculated from those prices.

Last updated: October 11, 2026

## What is it for?

A cost based on one electricity price is not realistic: home charging is cheap and fast charging is expensive. When you enter each charge’s own price, trip cost follows the real average cost of the energy in your battery, so Yoldaş’s estimate gets close to what you actually spend.

## Where to find it

**Statistics** tab › **Charging sessions**: a price line under each charge. Default price: **Account › Electricity price**. Trip cost: **Estimated cost** in the trip details.

1. **Enter your default electricity price**

On your phone, tap the profile icon at the top right, then fill in **Electricity price** on the **Account** page. Charges without their own price use it.
2. **Open the charging sessions**

In the **Statistics** tab, scroll down to the **Charging sessions** list.
3. **Tap the price line under a charge**

Each charge has a price line, for example “3 ₺/kWh · ₺180”. Tap it to open the editor.
4. **Type the price and save**

Enter the price per kWh for that charge (for example **3.25** or **12.50**) and tap **Save**. The amount on the line updates too.
5. **Enter the receipt kWh if you like**

If you type the energy the station printed in the **kWh on the receipt** field, the amount is calculated with exactly that energy. If you leave it empty, an estimate with a loss allowance is used.
6. **Check the trip cost**

Open a trip. Under **Estimated cost** you will see which price was used. The period cost in **Statistics** is calculated the same way.
7. **Go back to the default price if you like**

Tap **Use default price** in the editor and that charge uses the default electricity price again.

## Things to know

- A charge price is saved against the moment the charge started, so a charge is never priced twice.
- A charge without a price does not distort the average: the default price is used if it exists, otherwise it is left out of the mix.
- Prices and currency are estimates; this is not an invoice.

Related pages: [Charging and consumption](https://yoldas.io/en/charging), [release notes](https://yoldas.io/en/release-notes).

## Frequently asked questions

### What is a weighted average?

The battery is treated as a mix of energy bought at different prices. If a 60 kWh battery was filled at home at 3 ₺/kWh, the average is 3 ₺. If you then add 30 kWh at a fast charger for 12 ₺/kWh to a half-full battery, the mix is (30×3 + 30×12) ÷ 60 ≈ 7.5 ₺/kWh. Later trips use that average.

### What if I do not enter a price?

A charge without a price uses the default electricity price. If there is no price at all, no cost is shown, only the energy (kWh).

### Can I enter prices for old charges?

Yes. You can set a price on any charge in the list; trip cost uses the charges before that trip. Prices for the latest 200 charges are kept.

### Where are the prices stored?

In your account, together with your vehicle preferences. The same prices appear on every phone you sign in to with that account.

### Why is the cost an “estimate”?

Charging losses, station fees and the car’s energy measurement mean the real amount can differ slightly. Yoldaş uses the energy reported by the car and the prices you entered.

### How do I change the currency?

Use the currency option on the **Account** page. The prices you enter are in the selected currency.

### What is the kWh on the receipt for?

The station shows the energy it drew from the grid on the receipt or in its app. That is a few kWh more than what reached the battery (charger and cable losses, and the car notices the start a few seconds late). If you enter the receipt kWh, the amount is calculated with exactly that energy. If you do not, Yoldaş adds a loss allowance of 4% for fast (DC) charging and 10% for slow (AC) charging to the energy that reached the battery; this is an estimate. As you enter receipt values, Yoldaş learns your own ratio and uses it for later estimates.

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

### [How to verify an APK's SHA-256 hash](https://yoldas.io/en/guides/verify-apk-sha256)

Calculate the hash of the APK you downloaded on your computer and compare it with the value on the download page.

### [How to choose a car app for your BYD](https://yoldas.io/en/guides/choose-car-app-byd)

A checklist for recording reliability, where data stays, language, installation and update signing.

### [Automations: what they do and how to use them](https://yoldas.io/en/guides/how-to-use-automations)

Learn what triggers, conditions and steps mean, how to set up your first automation and how to import one from a file.
