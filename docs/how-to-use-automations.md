# Automations: what they do and how to use them

An automation is your own rule: "when this happens, under these conditions, do these steps in order". It can turn on the climate each morning, protect the battery on a hill or tell you when charging is done. This guide shows how to set up your first automation and what every option on screen means. The option names are the same as in the app.

Last updated: November 19, 2026

## What are automations for?

You define a routine task once, and Yoldaş does it for you from then on. Automations are set up on your phone or on the car screen and **run in the car**. Each has three parts: **When** (the trigger), **Conditions** (optional) and **Actions** (the steps).

### Climate in cold weather

- **When** When the car turns on.
- **Conditions:** Battery at least 25% and Outside temperature below 5 °C.
- **Actions:** Climate on, Driver temperature 22 °C, Front defrost on.

This routine runs while the car is on. When the car is fully off, only the "Climate on" step works; the temperature and defrost steps are rejected. For climate in a car that is off in the morning, set up a single-step routine ("Climate on") that triggers at a set time. A similar **Morning preparation** is also among the templates.

### Battery protection and mode on a hill

- **When** When slope reaches, threshold 6.
- **Conditions:** Slope, At least, 6.
- **Actions:** Battery protection On with a target of 55%, then Driving mode Normal mode.

For the descent you can set up a separate automation: **When slope drops below**, threshold -5. Steps: Battery protection On, target 70%, Regeneration level High, Driving mode Eco mode.

### Sport mode above 120 km/h

- **When** When speed reaches, threshold 120.
- **Actions:** Driving mode Sport mode.

### Notification when charging is done

- **When** At 100% battery.
- **Actions:** Notify in car. Add Notify phone as well if you want to be told on your phone.

## Where do I find them?

- **On the phone:Account** › **Automations** (in the Yoldaş theme) or **All features** › **Automations**.
- **On the car screen:Yoldaş › System › Automations**.

The phone and the car share one list, which syncs within a few minutes. New features depend on the Yoldaş version in the car: speed, slope and brake triggers need **0.12.56**; car-reading triggers, shadow mode, internet requests and ready-made templates need **0.13.21**; the new editor, steering wheel button triggers and condition groups need **0.13.29**; new car commands need **0.13.40** or later. With an older version the related triggers never reach the car, and the phone shows the note "Works once the Yoldaş app in the car is updated." To update, see the [download page](https://yoldas.io/en/download).

## Set up your first automation

1. **Open the Automations screen**

On your phone, go to **Account › Automations** (in the Yoldaş theme) or **All features › Automations**. On the car screen, open **Yoldaş › System › Automations**.
2. **Start a new automation**

Tap **New automation** or pick one of the **Templates**. The wizard goes through five steps: When, Conditions, Actions, Settings, Summary.
3. **Choose when it should run**

In the **When** step, pick one or more triggers. For triggers with a threshold, such as speed, slope and brake, type the threshold value in the box that appears. For the time trigger, choose the time and the days.
4. **Add conditions if you like**

In the **Conditions** step, pick a condition for the battery, outside temperature, speed, slope, brake pedal or another car reading. You can collect conditions in **If all are true** or **If any is true** groups.
5. **Add the steps in order**

In the **Actions** step, pick a vehicle action, a wait, a notification or another step from a category and add it. Change the order by moving a step up.
6. **Adjust the settings**

In the **Settings** step, set the shortest time that must pass between two runs of the same automation (the repeat interval) and, if you like, shadow mode.
7. **Read the summary and save**

In the **Summary** step, check the readable sentence of the rule, give it a name (60 characters at most) and save. The automation is sent to the car; if the car is not connected, it is applied when it connects.
8. **Try it while parked**

Use **Run now** on the automation's details page to run its steps for real and see the result. **Try on the past** shows what would have happened in the last 7 days. Then turn the automation on.

The options are explained in the glossary below. For other phone commands, see [remote control](https://yoldas.io/en/remote-control).

## Glossary: what does each option mean?

### Triggers: When

You choose what starts the automation. You can pick more than one trigger (up to 6 in one automation); when any of them happens, the automation starts.
OptionWhen does it run? On button pressWhen you start it yourself, from the phone or from the car screen. When car turns onWhen the car is switched on. At 100% batteryWhen the battery is fully charged. At a set timeAt the time and on the days you choose. On arrivalWhen the car enters the area you define. You give the area a **Location name** and enter an **Area radius (m)** (100–5000 m). The **Use current car location** button puts the area where the car is now. On departureWhen the car leaves the area you define. When speed reachesWhen the speed reaches the **Speed threshold (km/h)** you enter. When speed drops belowWhen the speed drops below the threshold. When slope reachesWhen the road slope reaches the **Slope threshold (°; + uphill)** you enter. A positive value is uphill, a negative value is downhill. When slope drops belowWhen the slope drops below the threshold. When brake pedal is pressed toWhen the brake pedal reaches the **Brake threshold (%)** you enter. When brake pedal drops belowWhen the brake pedal drops below the threshold. When the gear is put into PWhen the gear is put into P. When a car reading passes a threshold or changesYou pick one of about 60 car readings, such as battery and charging, tires, 12 V battery, doors and connection. For a numeric reading you enter the threshold; for a state reading (for example, a door open) you choose the new state. When a steering wheel button is pressedWhen the button you choose on the steering wheel is pressed. You find the button's name by pressing it on the **System › Diagnostics › Key discovery** screen (60 seconds, in the car only). The button's own function is not affected.

**For location triggers:** location sharing must be on and the GPS data must be fresh. If the position is uncertain near the edge of the area, the trigger does not fire.

**Fires once on crossing.** Speed, slope and brake triggers do not run continuously; they run at the moment the value crosses the threshold. A "reaches" trigger fires when the value reaches the threshold from below. A "drops below" trigger fires when the value, while at or above the threshold, drops below it. If the value is already past the threshold, it does not fire again and again.

**About the brake pedal:** the pedal is read only as pressed (100%) or released (0%). A 25% and a 35% threshold therefore behave the same.

### Conditions: Which conditions

Conditions are optional. By default the automation runs when all of them are true together. You can use **If all are true** and **If any is true** groups, nested up to three levels deep; for example, "if the battery is low and (the speed is zero or the gear is P)".
OptionMeaning Battery at least (%)The battery level must be equal to or higher than the percentage you enter. Outside temperature below (°C)The outside temperature must be below the value you enter. Speed (km/h)The speed must be **At least** or **Below** the value you enter. Slope (°; + uphill)The slope must be **At least** or **Below** the value you enter. Brake pedal (%)The brake pedal must be **At least** or **Below** the value you enter. A pressed pedal counts as 100% and a released one as 0%. Only at this locationThe car must be inside the area you defined. Another car readingA reading from the catalog, such as a door, tire, 12 V battery or connection, must be at the value or state you choose. For a numeric reading there are also "equal to", "not equal to", "at most" and "above" options.

**At least** means the value must be equal to or greater than your number. **Below** means the value must be smaller than your number. For speed, slope and brake conditions you pick one of the two; for battery and outside temperature the meaning is in the name.

**Stale data fails the condition.** If the vehicle data for a condition is not up to date, the condition counts as not met and the automation stops; the run history says why.

### Steps: Actions

Steps run from top to bottom. You add them with **Add step**.
StepWhat it does Vehicle actionControls the car. The options are in the next table. Wait (seconds)Waits for the time you enter (1–7200 seconds), then moves on to the next step. MediaMutes the media that is playing (or returns it to the previous level), plays, pauses or sets the volume. Stop recordingStops the recording. Mark the recordingMarks the recording now; the clip is protected. Recording modeSets the driving recording mode to Off, Park, Drive or Continuous. Turn Sentry on / offTurns Sentry on or off for parking. Turn another automation on / offTurns another automation you choose on or off. Internet requestSends a request to an address. If you like, it is signed with a secret key; if it fails, it is retried 0–6 times, and the request waits in the queue for up to 24 hours. Do not share the secret key with anyone. Open appOpens the app you choose on the car screen. Notify in carShows the message you write (up to 160 characters) on the car screen. Car screen messageShows the short message you write (up to 140 characters) on the car screen. Notify phoneSends a notification to your phone (up to 160 characters). Turn on automation notifications on the phone under Account › Notifications. Delivery is not always certain; the notification is held while driving and deleted after 10 minutes. IfIf the condition you choose is true, runs the steps up to **Otherwise** or **End condition**. Up to 3 conditions can be nested. OtherwiseOptional. Starts the steps that run when the If condition is not true. End conditionClose every If step with this one. Wait for conditionWaits until the condition you choose is true. It gives up when the time in **Maximum wait (seconds)** runs out.

### Vehicle actions

In a Vehicle action step you pick one of these:
ActionOptions and meaning ClimateClimate on, Climate off, Driver temperature, Passenger temperature and Fan. Front defrostOn or Off. Clears mist and ice from the windshield. Rear defrostOn or Off. Clears mist and ice from the rear window. Air circulationInside or Outside. Recirculates the cabin air or draws it in from outside. Close windows / Vent windowsCloses the windows, or opens them slightly for ventilation. Open trunk / Close trunkOpens or closes the trunk. To open it, the car must be stopped and the driver's door must be unlocked. Driving modeEco mode, Normal mode, Sport mode or Snow mode. Regeneration levelStandard or High. Sets how much energy the car puts back into the battery while slowing down. Brake feelComfort or Sport. Changes the feel of the brake pedal. Power modeEV or HEV. Battery protectionOff or On. If you choose On, you enter the **Target charge (%, 15–70)**. New commands (0.13.40)Wireless charging, steering wheel heating, seat heating and ventilation, ambient light brightness and color, daytime running lights (turn on only), trunk opening height and HUD. For wireless charging and trunk height, the car must be in P and stopped. If the car does not support a command, the step is rejected.

**When the car is off:** only turning the climate on and off works. For this the gear must be P, the speed 0, and the driver's door closed and locked; the battery must be above 20% and the 12 V battery above 12.0 V (with the charging cable plugged in, no battery or 12 V limit is checked). While the car is off, temperature, fan, defrost, air circulation, window and driving mode steps are rejected.

### Other settings and buttons
OptionMeaning Repeat interval (seconds)The shortest time that must pass between two runs of the same automation. The default is 60 seconds; you can choose anything from 1 second to 1 day. Shadow modeWhen on, the automation triggers but does nothing; it only records "would have run". Watch it for a few days and turn it off once you see it works correctly. Try on the pastOn the details page, shows how many times the automation would have run, been skipped or only been watched in the last 7 days. Run nowRuns the automation immediately and really performs its steps. It works even when the automation is switched off. Switch next to the automationThe switch next to each automation in the list. When it is on, the triggers start the automation. When it is off, the automation does not run by itself. TemplatesThere are more than ten ready-made automations (for example Morning preparation, At 100% battery, Don't forget to plug in, Low tire pressure, 12 V battery low). You pick one and edit it. The complex ones start off and in shadow mode. Recent runsShows the latest state of your automations: Running, Completed, Stopped, Could not complete, Skipped (with the reason) or, in shadow mode, Would have run.

### Limits

- An automation can have up to **20 steps**.
- An automation can have up to **6 triggers**.
- An automation name can be up to 60 characters, a phone notification 160 and a car screen message 140.
- You can save up to **50 automations**.
- The total waiting time in one automation can be up to **2 hours**.
- If steps can be nested up to **3** levels deep.
- Only one automation runs at a time.

## Import automations from another app

You can bring an automation file exported from another app into Yoldaş. The import scope is narrow: only speed, slope and brake triggers and the driving mode, regeneration, brake feel, power mode and battery protection actions are recognized; the rest is skipped.

1. **Choose the file**

On the phone, tap **Automations** › **Import from file** and pick the exported .json file. The file can be up to 250 KB and can hold up to 50 automations.
2. **Read the import report**

The report shows how many automations were imported. For each one it says **Fully imported**, **Partly imported** or **Not imported**, with the reason.
3. **Check and turn them on**

Imported automations arrive **switched off**. Look at the steps of each one and turn on the ones that suit you, or tap **Enable all** to turn them all on at once.

If a trigger, condition or action is not supported by Yoldaş, that part is **skipped**; no guessed replacement is made. A block whose condition cannot be applied is skipped as a whole, so the actions inside it never run without the condition. "Equal to" and "or" conditions are not supported. "Greater or equal" and "less or equal" conditions are converted approximately, and the report says so.

## Things to keep in mind

- **Automatic mode changes while driving** (driving mode, regeneration, brake feel, power mode) change how the car behaves. Try a new automation first with **Run now** while parked, then turn it on.
- **The result sometimes says it could not be confirmed.** The result of the new commands cannot always be read back from the car. The command is still sent and written to the command log in the car, and the automation carries on.
- **Only one automation runs at a time.** If another one is triggered while one is running, you see "Another routine is running" and the second one is skipped. Keep automations with frequent triggers, such as speed and brake, short.
- **Older car version.** If the Yoldaş version in the car is older than the one the feature you use needs (see the version list above), that trigger or step does not work.
- **Car that is off.** When the car is fully off, only the climate on/off step works.

You may also want to look at the [Automations feature page](https://yoldas.io/en/automations), the [bottom bar shortcuts](https://yoldas.io/en/bottom-bar) and the [release notes](https://yoldas.io/en/release-notes).

## Frequently asked questions

### What is an automation and what is it for?

It is a rule that says "when this happens, under these conditions, do these steps in order". For example, you can set the climate to 22 °C when the car turns on, or show a notification on the car screen when the battery reaches 100%. Automations run in the car.

### Where do I find automations?

On your phone: Account › Automations (in the Yoldaş theme) or All features › Automations. On the car screen: Yoldaş › System › Automations. The phone and the car share one list; changes sync within a few minutes.

### Why don't some triggers or steps reach my car?

New features depend on the Yoldaş version in the car. Speed, slope and brake triggers need 0.12.56; car-reading triggers, shadow mode, internet requests and ready-made templates need 0.13.21; the new editor, steering wheel button triggers and condition groups need 0.13.29; new car commands need 0.13.40 or later. With an older version, the phone shows the note "Works once the Yoldaş app in the car is updated."

### Does an automation work when the car is off?

When the car is fully off, only the step that turns the A/C on and off works. Temperature, fan, defrost, air circulation, window and driving mode steps are rejected; the car must be on for these.

### The conditions are met but the automation did not run. Why?

There are four possible reasons. If the vehicle data for a condition is not up to date, the condition counts as not met. The repeat interval may not have passed. If another automation is running, the new one is skipped. Speed, slope and brake triggers fire only when the value crosses the threshold; they do not fire again if the value is already past it.

### What happens when the switch next to an automation is off?

The triggers do not run, so the automation does not start by itself. "Run now" still works.

### The result says it could not be confirmed. Was the command not sent?

It was sent. The result of the new driving and energy commands cannot always be read back from the car. The command is still sent and written to the command log in the car, and the automation carries on. You can check the driving mode on the instrument panel.

### Does a brake threshold of 25% differ from 35%?

No. The brake pedal is read only as pressed (100%) or released (0%), so a 25% and a 35% threshold behave the same.

### Can I import automations from another app?

Partly. Choose Automations › Import from file and pick the exported .json file. Only speed, slope and brake triggers and the driving mode, regeneration, brake feel, power mode and battery protection actions are imported. Imported automations arrive switched off; unsupported parts are skipped and listed in the import report.

## Other guides

### [What are BYD DiLink 3, 4 and 5?](https://yoldas.io/en/guides/byd-dilink-3-4-5)

How to find your DiLink generation and software version, and what the first digits of the version decide in Yoldaş.

### [APK not installing on a BYD](https://yoldas.io/en/guides/byd-apk-not-installing)

What the error messages mean, what changed in versions after 2310 and how apps get installed on a locked screen.

### [Installing on Sealion 7 and DiLink 5](https://yoldas.io/en/guides/sealion-7-dilink-5-install-apps)

How to recognize DiLink 5, the two install paths BYD owners use and the settings to turn on after installing.

### [Before and after a BYD update](https://yoldas.io/en/guides/byd-software-update)

What a BYD update can do to installed apps, what to save before you install it and how to bring Yoldaş back afterwards.

### [Does BYD have sentry mode?](https://yoldas.io/en/guides/does-byd-have-sentry-mode)

Which markets have BYD's own sentry mode and which don't; watching your parked car with Yoldaş.

### [Do BYD cameras record?](https://yoldas.io/en/guides/does-byd-record-dashcam)

Which models have BYD's own recorder, why the 360° cameras don't record, and recording with all four cameras without buying a dashcam.

### [BYD screen rotation](https://yoldas.io/en/guides/byd-screen-rotation)

Ways to turn the rotating screen to landscape and portrait, which models have a rotating screen, and a shortcut for cars with no steering wheel button.

### [BYD tyre pressure](https://yoldas.io/en/guides/byd-tyre-pressure)

Recommended cold tyre pressures model by model (bar, kPa, psi) and how to see the pressure on the screen or on your phone.

### [BYD app not connecting](https://yoldas.io/en/guides/byd-app-not-connecting)

What to try against car-adding, connection and service errors in the official BYD app; a phone app independent of BYD.

### [Installing an APK on a BYD from a USB stick](https://yoldas.io/en/guides/install-apk-byd-usb)

Copy the APK to a USB stick on your computer and open it on the car screen. Step by step, with the permission prompt and common problems.

### [How to verify an APK's SHA-256 hash](https://yoldas.io/en/guides/verify-apk-sha256)

Calculate the hash of the APK you downloaded on your computer and compare it with the value on the download page.

### [How to choose a car app for your BYD](https://yoldas.io/en/guides/choose-car-app-byd)

A checklist for recording reliability, where data stays, language, installation and update signing.

### [Charging price and trip cost](https://yoldas.io/en/guides/charging-price-and-trip-cost)

Enter a price for each charge and see trip cost based on what you actually paid.
