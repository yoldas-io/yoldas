# Release notes

The same notes appear in the app after an update and on [yoldas.io](https://yoldas.io/en/release-notes).


## 0.15.29 (2026-11-22)

- **Your own wallpaper.** In Edit › Scene › Background, pick your own picture instead of the studio. The car appears on top of it from behind, or not at all; the picture is stored only on your car.
- **One tap between Studio and On the road.** The new Scene widget switches to On the road or the studio whenever you like, in P too.
- **Similar cars.** A new card in My car on the phone compares your car with cars of the same model: battery health, consumption, city and highway range, DC charging and what changed this month.
- **Battery certificate and monthly report.** Create a printable battery certificate from Similar cars › Battery. Your monthly report arrives in the first week of each month and your year in review in December; you get an early warning when something needs attention.
- **Steering feel.** Comfort or Sport: a widget on the Home screen, a step in automations and a button in the Driving panel on the phone.
- **You know when recording stops.** If recording is on but cannot save, the car screen warns you and the phone shows the reason and sends a notification. When the card is full, the oldest Yoldaş recordings on the card are deleted first.
- **Internet while parked.** If the car's mobile internet drops while parked, the phone tells you why. If BYD's data control is cutting Yoldaş off, you can turn it off on the car in Settings › Phone › Connection.
- **Front passenger seat in automations.** Whether someone is in the front passenger seat can be used as a trigger and a condition. A flow that was interrupted continues from the step where it stopped.
- **Cars On the road, smoother screen.** Show surrounding cars as Realistic or Simple. While driving, widgets are redrawn only when their values change, so the centre screen works less.
- **DiLink 5.** Experimental "Stay online while parked" setting; the central lock state is learned more reliably.
- Also: the speed limit sign is read more accurately; electric cars no longer show "HEV" on the cluster; the cluster does not reopen by itself after the car turns off; on the Dolphin, venting no longer opens the windows fully first; sentry no longer misses a person right next to the car; charging power shows decimals; the music card keeps the cover when the song changes; cluster designs can show km and consumption since the last charge and a compass; new language: Portuguese (Portugal).

## 0.15.28 (2026-11-21)

- **You can turn the headlights off.** With Settings › Appearance › "Headlights on" off, the headlights on the car on the home screen stay dark from every angle. On Atto 2 and Seal the night headlights are no longer pure white but glow with the lamp's own texture; the grey patches on the bonnet of white cars are gone.
- **A smoother centre screen.** The On the road scene, split screen and the CarPlay picture put less load on the centre screen. The app in a split pane no longer closes when you shift between P and D; it waits in place. The turn signal lamps on the home screen car and the Sentry warning are drawn more lightly.
- **360° recording at full frame rate.** 360° recordings, live view and the turn camera no longer skip every second frame, so recordings are smooth. On some cars the 360° camera no longer stops while opening.
- **The drive mode shows correctly.** In Normal, the cluster and On the road no longer say "ECO"; Eco chosen with the car's own button is recognised too, and the cluster updates as soon as the mode changes.
- **Margins and EV/HEV on the cluster.** The margins in Cluster settings now apply to the Yoldaş cluster too and show up as soon as you move the slider. On hybrids every built-in design shows EV/HEV. Designs can show BYD's Trip A/B and the km page chosen with the stalk button.
- **View for On the road.** In Edit › Scene, choose a Near, Medium or Far view for On the road; the car and the road shrink together. Cars and lorries driving away no longer look like a line.
- **Seek on the music card.** Drag the bar with your finger to move forward or back in a song (in music apps that allow seeking).
- **Petrol use on hybrids.** When you shift to P, the trip summary also shows the petrol used on that trip.
- **More accurate range.** Range is read within the car's own limits: on hybrids the total range no longer drops suddenly with a full tank, and invalid values outside those limits are not shown.
- **Route of combined trips on the phone.** The route of trips you combined shows on the map; older combined trips no longer say "no location", and the time bar no longer slides back by itself. While connecting to the car, the phone no longer says "Not connected to the car" right away.
- Also: with the car off, the cluster no longer reopens by itself and comes back when the car is switched on; a navigation app notification without directions is not treated as a direction; a community cluster design you deleted no longer stays in the car and a built-in design takes its place; after an update Yoldaş prepares itself while the car is off, so the first starts stutter less; the orange dots on command buttons are gone.

## 0.15.26 (2026-11-19)

- **The cluster no longer disappears.** The Yoldaş cluster is now drawn in the cluster's own window with a new method; if something stalls, the window rebuilds itself within seconds and projection is not interrupted. While the cluster is on, a second "Yoldaş" line appears in notifications; this is normal. When the car is switched off and on, the cluster comes back by itself.
- **The music line on the cluster is fixed.** With the cluster size on Automatic, the song, radio and phone line on the cluster no longer turns into Chinese characters or repeated text like "GolGol". If the line is garbled right now, restarting the multimedia unit once is enough.
- **A smoother screen.** On the road and the moving scene are drawn on their own drawing thread; car data, opening the 360° camera and recording files no longer hold up the screen. When the screen is under strain, the scene lightens itself. The screen stutters less while recording; the turn camera opens more smoothly and no longer drops out while driving.
- **Album art on the music card.** Album art now also appears for music apps that only provide it as a link.
- **Bottom bar pop-ups close each other.** With climate, recent apps or the shortcut menu open, pressing another button closes the open window; the recent apps button opens and closes its panel.
- **"Update now" on the phone is fixed.** The button installs the released version again; for a while it asked for a test version by mistake and replied "Test versions are off". If "Show test versions" is on in the car, the phone now sees it too, and tells you when there is no new test version.
- **Mobile data switch in Connections.** Mobile data is now read from the car's SIM; data you turned off with the switch no longer shows as "on" again after a while.
- **Bluetooth on/off in automations.** Cut energy loss while parked, e.g. with a "turn Bluetooth off at home" flow. On the phone, the night and safe-place settings can also be changed under Stay connected while the car is off › Bluetooth.
- **Why did the automation stop?** An automation that stops halfway now shows a short reason instead of "Error" in its history in the car and on the phone: condition not met, no data, command refused, time ran out. Unlock and lock with the key flows no longer stop after unlocking.
- **Sentry warns on the car screen.** With the car off, Sentry can now switch on the car screen and show a warning on all cars; before, most cars skipped this because the system software was not recognised.
- **Your name in the greeting, blind spot on the turn camera.** The home screen greeting uses the name from Settings ("Good morning, Kadir"). On the turn camera, the edge of the picture glows red when that side's blind spot warning is on.
- **Saved home screen layouts.** Edit › Layouts › My saved layouts: save your current home screen with a name and load it back in one tap (up to 6).
- Cluster: Ufuk looks from above, the car is smaller and the cars ahead are visible; choose the viewing angle and car size in Cluster settings. A fuel gauge on cars with a tank; designs can use the Ufuk scene, and you no longer need to be in P to choose a design. CarPlay and Android Auto on the cluster recover by themselves when they stall, and the energy box is no longer cut off in the corner. BYD's ADAS 3D view is hidden during projection too; Ufuk's rear view is drawn with the car's own camera.
- Camera support added for Atto 3 with 49.1.2 software. "Keep rhythm lights steady" now keeps the lights steady while music plays too, and the ambient light no longer blinks off. "Listen to cabin" no longer stops the radio, and what is playing in the car is not interrupted when you press it. On cars without a 360° camera, live view starts with the BYD dash camera.
- Phone: sheets close with the Android back button; long trip routes fit the map, and the full-screen map has a time slider; Sentry no longer shows as "off" while it is on; the car is not called "asleep" while it is online, and if a connection cannot be made the reason is shown.
- Sealion 7: correct door and boot status, "Close boot" works, windows one by one, climate temperature; automation templates with unsupported steps are hidden. On Sealion 7, a camera that does not open is retried only now and then; the blind spot and nearby cars switch says why it does not work.
- Also: Automatic view switches to night as soon as the BYD screen does; the jump when returning to the home screen is gone; the QR code at first setup no longer gets stuck on "Preparing code"; the turn camera is no longer kept open needlessly while the car is off. The On the road scene always looks from above (the view choice is gone); after a long stay at a safe place, Sentry no longer starts there by mistake.

## 0.15.24 (2026-11-15)

- **Every car value on your cluster.** The cluster you design with AI can now also show this drive's consumption, duration and average speed, the pressure and temperature of all four tyres, door and boot warnings, seat belts, blind spot, cabin and climate temperature, the 12 V battery and battery health. The workshop's "What can be added?" section shows them all with examples.
- **Your own photo on the cluster.** Add a photo slot to your design and choose the photo in the car under Driver display › Cluster design › Cluster photo. The photo stays only in your car and is never shared with the design.
- **A tyre screen like BYD's.** A top view of your own car model in its own colour, with the pressures next to the wheels.
- **Fewer AI hiccups.** The workshop and the phone fix the AI's small typing slips themselves and tell the AI what would be right for any errors left. Upload the kit and ask "What can you show?" to get a summary first.
- **Sentry only when the car is off.** Sentry and parking recording now run only when the car is fully off; they no longer slow the screen while the car is on in P.
- **BYD's frame always leaves the cluster.** While something is projected, BYD's strip, speed, power and odometer text, speed limit sign and music line are hidden; no need to switch the car off and on.
- **Merge trips.** Join trips split by a short stop into one, in the car or on the phone, and split them again if you like. With "Ends when the car switches off" selected, the interim summary in P no longer looks finished.
- **Write automations with AI on your phone.** Automations › Write with AI: give the guide to your own AI, paste the answer; Yoldaş checks it and prepares a correction message if anything is wrong.
- DiLink 5: lock and windows on Android 12 Seal U and Seal; more car data on Sealion 7; steadier cluster projection.
- On the road: flat lanes, 30 fps, high view by default, a "Moving road" switch; a pool of light in front of the car when the low beam is on.
- The 360° view on your phone shows doors, windows and lights on Seal U, Atto 2, Atto 3, Dolphin, Han and Sealion 7 too.
- Unlock and lock with the key is more reliable: it unlocks as you approach, locks again if no door is opened, and locks as you walk away. The "When the car turns on" automation no longer misses start-up; when run by hand, the reason is shown if a condition fails.
- Fixes: turn camera stutter, Atto 2 start-up crash, drops while projecting to the cluster, Fill in the CarPlay pane; the small energy summary widget gets tabs; "Don't show again" on the "Make default" banner; SD card problems now show the reason.

## 0.15.22 (2026-11-14)

- **Design your own cluster.** Download the AI kit (yoldas.io/kadran-atolyesi), describe the look you want in plain words, try the resulting file in the workshop or on your phone under Account › Cluster designs, and send it to the car. In the car, choose it in Driver display › Cluster design. Share it with the community if you like; vote on other people's designs and add the ones you like to your car. A design is only a look; it can't send commands to the car.
- **Front camera on the cluster.** When you're approaching a turn and driving slowly, the road ahead shows on the cluster: Panorama (full cluster, gauges on top) or Lens. It never opens in reverse; you choose when it appears.
- **Surrounding vehicles in traffic.** The vehicles ahead and beside you that your car detects, lane lines and the distance to the car ahead, in On the road and on the cluster (Horizon, Wing). In On the road, the road turns with the steering wheel, and there's a top-down view (low, medium, high).
- **CarPlay and Android Auto on the cluster.** In the centre, in three layouts; speed is always visible. A large layout and a Yoldaş speed limit sign; while projecting, BYD's bottom band, the ADAS box and, if you like, its top info are removed.
- **CarPlay on the centre screen.** Works properly full screen and in a pane; touches no longer drift. The screen can also be split top and bottom, and the split can hold three apps.
- **Car transfer.** When selling your car, hand it to the new owner with a transfer code or remove it from your account; a second-hand buyer can request the transfer from the car screen.
- **Screen child lock.** With the widget or a bottom bar shortcut, the screen ignores touches while the picture keeps running; to unlock, press and hold the lock for 2 seconds.
- **Han and Sealion 7.** 3D view, 360°, colours, On the road and the cluster on these models too.
- Notifications arrive instantly, also while driving. The charging finished notification comes without delay.
- On the phone: data left and data used this month in the BYD data plan on your car's SIM.
- Automations: turn mobile data on/off action; "Play a sound" plays without stopping the music; the notification step also shows on screen.
- Smoother turn camera (25 fps). If you like, a trip ends when the car switches off; you can see range based on today or on this drive. "Keep rhythm lights steady" in Settings › My car (in testing).
- Fixes: no more "Movement detected" at night in Sentry when nothing moves; the hard braking template no longer marks a clip on every brake press; Sentry no longer shows as off on the phone; the cluster and On the road no longer heat up and stutter on long drives; clips can be watched from the cloud while the car is off; battery temperature from the hottest cell; district and province in the weather widget.

## 0.15.21 (2026-11-07)

- **New cluster designs.** Wing: two angular gauges that fill in your drive mode's colour. Flow: power lights, giant speed and a sliding speed tape. Minimal: only the essentials. Chronograph and Horizon were re-laid out and no longer clash with the clock, speed limit, warning lights and OK light that BYD shows on the cluster.
- **More of the BYD strip is hidden.** With "Hide BYD bottom strip" on, projecting now also removes BYD's power, speed and odometer readouts along with the battery and range strip; speed always shows on the Yoldaş cluster. Switch the car off and on once after turning it on.
- **You choose test versions.** Anyone who turns on "Show test versions" in Settings › Update gets new features first. A test version is never installed automatically; you start it with "Install" in the car or on your phone.
- **A livelier On the road.** Lane lines flow, road edges can be turned on or off, and in a blind-spot warning the lane on that side lights up red (Edit › Scene › On the road). Shifting to D puts the car on the road without waiting.
- DiLink 5 (Sealion 7 and similar): lock, windows, tailgate, sunroof and shade, and climate temperature, fan, air direction and SYNC. Buttons that don't work on these cars are dimmed.
- Climate air direction has new icons; on cars with seven directions, face, feet and windscreen can be chosen together.
- Live tracking on the phone: continues with network location when GPS goes quiet and warns when the location is old.
- Thai and Chinese added.
- The driving scene in split panes was removed; the driving view is now the home screen's On the road scene. In older layouts that pane is replaced by Yoldaş.
- Fixes: the scene wrongly returning to P at red lights, light and headlight positions on the Seal, Dolphin and Atto 2 rear lights, the scene at night with headlights off, "Hide BYD bottom strip" saying "not supported" on some cars.

## 0.15.20 (2026-11-06)

- **Split screen.** Divide the centre screen into two or three panes: the Yoldaş home screen, the driving scene, the media card, CarPlay / Android Auto or an app you choose, side by side. Separate layouts for parked, driving and charging; drag the divider to change the ratio and open or close the split with the Split button in the bottom bar.
- **Driving scene.** Your car on the road, in the colour set in Settings, with six road designs (Horizon, Light trail, Contour, Daybreak, Glass tunnel, Point cloud). The road follows the weather (rain, snow, fog) and the drive mode (Eco, Normal, Sport, Snow); you can turn this off. Put any widget on the scene, wherever and as large as you like.
- **The car takes to the road in D.** Edit › Scene › On the road: the car on the home screen turns around and settles onto a lit road; in P it returns to the studio or stays on the road. If you use a split while driving, the car settles first and then the panes open.
- **Car screen on your phone.** Watch the car screen live on your phone and control it by touch while the car is in P. Turn it on in the car under Settings › Phone; only the car owner can use it, and a sign stays on the car screen during the session.
- Yoldaş cluster: Yoldaş's own design on the instrument cluster (speed, power, range, navigation, music). The CarPlay and Android Auto map can go to the cluster too; BYD's ADAS box and bottom strip can be hidden while projecting.
- CarPlay and Android Auto on the home screen, as a widget or a pane, used by touch.
- Live tracking on the phone: the car on the map every second, with heading, trail, speed, gear and battery.
- Seat memory: Yoldaş's own 1·2·3. Hold to save the seat, steering wheel and mirrors; tap to bring them back (in P only).
- Cabin engine sound (optional, inside the car only) and ready-made ambient light automations: red when a door opens, colour by the climate temperature.
- Top strip: gear, battery and range can be added; four styles; each item on the left or the right.
- Automations: several conditions in "If" and "Wait until"; the new "Change layout" step opens or closes the split or switches to a preset layout.
- Recordings: the 360° cameras and the BYD dash camera in one video; an immediate warning when the card can't be read; a day filter on the car screen; the dash camera in live view too.
- The trip summary can be turned off (Settings › Appearance › When parked). Spanish, French and Russian added.
- Fixes: Sentry starting by mistake while parking at home, a false "door left open" alert, the cluster freezing, CarPlay falling back to the home screen on first start, garbled radio names.

## 0.15.14 (2026-11-04)

- **Automation widget on the home screen.** Runs the flow you pick with one tap and shows progress and the result. Turn on "show in the bottom bar inside the area" for a flow and its button appears in the bottom bar when you arrive there.
- Saved places in automations (Home, Work…). Flows that use location run while location sharing is on; outside the area a flow does not start and tells you why.
- The web request step is renewed: it also sends to devices on your home network (http://), shows the result and the error reason, and never sends a request twice after a timeout.
- Steering wheel buttons can be linked to automations (volume, mode, voice command and long presses included); a linked button does not trigger the car's own function on that press.
- Community automations: share your flow with personal details removed, and add other people's flows with one tap.
- New actions: Wi-Fi on/off, pause the pedestrian warning sound, close the on-screen message. Ambient light colour is picked from a colour wheel.
- Climate: SYNC changes the car's own setting; ONLY (ventilation without A/C) and air direction can be added to the bottom bar; the climate on/off button uses BYD's own icon.
- In Sentry "on detection" mode the seconds before an event are kept in memory and nothing is written to disk without an event; the event clip is also written to the Yoldas/Sentry folder in the car. Less battery use while parked.
- Recordings: the copy with the info overlay is fixed and also available for continuous recording; recordings open faster on the phone over a slow connection; the car's storage no longer fills up; recordings stay in the list with two cards or USB drives inserted.
- The retrofitted BYD dash camera is supported: watch its recordings on the car screen and the phone; BYD's own recording can be turned off in Settings.
- Recent apps panel: bring recently opened apps to the front or close them from the bottom bar. Split screen also works after the car is switched off and on.
- Repair BYD view: if another app left BYD's bottom bar hidden, fix it with one tap in Settings › Appearance › Launcher.
- The seat memory widget also recalls the driver positions saved in your BYD account (Driving, Rest, Standby). The outside temperature in the top strip is shown even when the Weather widget is on screen.
- On the phone: charging history by period, AC/DC and place (Home, Work); in Türkiye charging stations come from the EPDK list; the car's Wi-Fi status and signal.

## 0.15.10 (2026-10-31)

- **Phone lock renewed.** You pick your phone inside the routine; the car locks as you walk away without waiting for the connection to drop, and unlocks as you approach. It does not lock on brief Bluetooth dropouts or while the car is on (someone inside).
- **Routines are reset once in this version.** Add the ones you use again from Ready-made templates or build them yourself; templates arrive switched on. The old ones were backed up.
- Routines you added from a template and did not change now update themselves when the template is improved; duplicate copies collapse into one.
- New: Backup lock template, seat belt fastened/unfastened triggers, Turn off the car action and routines based on cabin temperature.
- Bluetooth stays on while the car is off and the car calls your phone itself; phone lock is much faster.
- Sentry stays awake longer while parked; a stuck mobile connection recovers by itself.
- Fixed the centre screen staying dark after a long park.
- What's new: after an update the news is shown once; always available in Settings › Update › Release notes.
- ABRP link: drive mode, range, altitude and widget; the token is entered from the phone.
- Ready-made home layouts renewed; altitude in the Weather widget, the music card remembers the last source.
- The bottom bar app picker shows how many slots are left; shortcuts can be removed in Edit.
- Sentry detection area (Draw) screen renewed; SYNC button for climate; recordings are in the Yoldas folder of the car's file manager.
- Drive mode (Eco, Normal, Sport) and EV/HEV buttons now work on more cars.

## 0.15.5 (2026-10-29)

- New diagnostics log: when something goes wrong, Yoldaş keeps a safe record of it in the car, so we can find and fix the issues you report much faster.
- When support is needed, only the records for the affected time range are requested, compressed and passed through a privacy filter.
- Diagnostics now use much less mobile data: a short summary is sent once an hour, and details are requested only when needed.
- The latest records are no longer lost after an unexpected shutdown.

## 0.15.4 (2026-10-29)

- New widget: Energy summary. Odometer, this drive and since charge with consumption, km, kWh, time and cost at a glance; swipe for today and this month.
- Energy recovered by braking is shown on the widget; while driving it says “Charging back” during regeneration.
- Tap for details: comparison with a petrol car and cost per km, where the energy went while driving and parked, battery, comparison with BYD's last 50 km and overall average, list of drives and a monthly chart.
- Cost is calculated the same way as on the phone; prices you enter for a charge on the phone are now used in the car too.
- To add it: on the home screen, Edit › Add widget › Energy summary.

## 0.15.3 (2026-10-28)

- Phone lock renewed: up to 3 phones can be selected. While one of the selected phones is in the car it does not lock; any of them unlocks on approach. Lock on departure also works when the phone disconnects.
- The “Add and enable phone templates” button on the Bluetooth automations page adds both templates enabled right away, with the page’s thresholds. If your old phone automation does not work, tap this button or adjust the thresholds to your car.
- The back button on the bottom bar works again in BYD settings, navigation and other apps. Inside Yoldaş it first closes the open window (clip player, confirmation dialogs), then goes back one page.
- A single slow request no longer drops the connection between the car and the server; reaching the car from the phone is more stable.
- Automations: exported automation files can be imported. Drive mode, EV/HEV, seat belt, blind spot, sunroof and sunshade position added as triggers and conditions; playing a sound file and starting the car added as actions. Waits accept decimals and zones can be set by coordinates.
- Parking: new “Keep Wi-Fi on while the car is off” option. Staying online while parked now uses only the battery and 12 V limits in your park settings.
- Clips: can be downloaded with the info overlay (speed, gear, pedals, indicators) burned into the video. Driving audio no longer stops on slow cards.
- Home screen: cluster mirroring widget (one tap on/off). The recirculation icon matches the car’s own climate screen. Window chips and switches in the Connections window.
- Music: play, pause, next and previous work through the car’s multimedia for sources that provide no media info.
- 3D models update by themselves when a new version is out; Seal U EV gets its own model and four colours. Home layout, bottom bar and 3D colour are included in the settings backup.

## 0.15.2 (2026-10-27)

- Simpler bottom bar: when Yoldaş is the default home screen, the Yoldaş bar is shown on every screen; if another home screen is chosen it never appears and the BYD bar comes back. It only hides for full-screen video.
- YouTube versions that hide the navigation bar on their home page no longer make the bar disappear; the app is pushed above the bar.
- The car’s built-in music streaming app now appears in the music source picker and opens when selected.
- The 26.6 kWh battery of the Seal U DM-i Comfort is recognised automatically; remaining energy and charging estimates use it.
- The info label on recordings (speed, gear, pedals, indicators) is drawn again, with an on/off button above the player.
- In the old look, every page has a “New home screen” button at the top right to switch back with one tap.
- If an update can’t be installed on the car, the reason and the steps to fix it are shown. After uninstalling and reinstalling, settings are restored from the backup when you sign in with the same account.
- Fixes: the PM2.5 indicator no longer flickers and keeps its last value; no gap under Settings and the home screen widgets; the 3D colour choice also changes the car in the driving view.

## 0.15.1 (2026-10-27)

- The 3D car now comes in its own colour: four official BYD colours each for Seal, Seal U DM-i, Atto 2, Atto 3 and Dolphin. Pick one in Settings › My car › Body colour and it is downloaded.
- Sunroof and sunshade widget: Open, Half, Close and Stop at any time. On cars without a sunroof the button is disabled.
- Button size for the bottom bar: Small, Normal (the BYD bar’s size) and Large. Change it with “Aa” in Edit; the bar keeps its height and never covers the map.
- The range widget shows the car’s own range as the big number, with Yoldaş’s “based on your driving” estimate below. Hybrids show electric and fuel range separately.
- Lane assist and speed-limit warning automations now hold after the car starts: if BYD switches the setting back on, Yoldaş reapplies it within a few minutes.
- Fixes: “Install now” no longer stays unresponsive; on some cars the bottom of apps is no longer hidden under the bar; the BYD bar no longer shows through in the day theme; the 3D mirrors no longer fold when the doors lock while driving; the bottom row of the Energy page and the Home/Work buttons in longer languages are no longer cut off.

## 0.15.0 (2026-10-26)

- New Home screen: Yoldaş can now be the car’s Home screen. A 3D car scene you rotate with your finger (Seal, Seal U DM-i, Atto 2, Atto 3 and Dolphin models are optional downloads; other models get a simple drawing), a new glass-style theme, day and night looks and portrait screen support.
- Widgets: drag and resize them in Edit, show them without a card or title. Speed, consumption, power, range, charging, tyres, climate, windows (vent the front 2 or all 4), lock, boot, seat memory, rotate screen, drive mode, music, app shortcut and more.
- The Yoldaş bar sits on top of the BYD bar: back, Home, recent apps, split and rotate screen, climate and favourite apps. Every button can be moved or removed. The BYD bar is no longer hidden, so apps no longer leave a gap at the bottom; the bar steps aside for full-screen video.
- Climate window: temperature, fan, air direction (face, feet, windscreen), recirculation, defrost, seat and steering-wheel heating.
- New Settings (search and categories) and a redesigned automation editor (categorised library, templates). A single switch in Settings turns the Yoldaş Home screen and bar off and takes you back to the BYD screen.
- Listening to the cabin and talking to the car during live view work again; these buttons are off while the car is off.
- The trip summary opens when you shift into P. The music card lets you pick the source; if the chosen app does not start playing, it is opened.
- Phone-proximity and physical-key unlock / lock automations. If no automation uses Bluetooth, Bluetooth is turned off while the car is parked, so your phone no longer connects to the car on its own.
- On cars that do not report an open boot (e.g. Atto 3), Open and Close are offered separately.

## 0.13.72 (2026-10-18)

- Parked-drain measurement: the energy drawn from the battery while the car is off and while it is on but parked in P is measured as the percentage and kWh difference read at the two moments the power state changes. One small record is sent per session; extra battery or data use is negligible. The data appears only in aggregate in the admin summary.

## 0.13.71 (2026-10-18)

- Cabin temperature: on cars that report it while the car is on, it appears in the Climate section in the car and on the phone. If the car does not report it, nothing is shown. The value comes from a single monitoring entry added to the car's data device; it is removed when the car switches off, and no lock or other vehicle command is sent.
- Car Recordings: Select all now also works in lists that are entirely protected, such as Sentry, Sudden brake and Manual. When protected and unprotected clips are mixed, a separate “Select all, including protected” button appears; the delete confirmation states how many protected clips will go.
- Phone: a Today period on the Energy tab and highest and lowest battery temperature rankings. If the car app does not update, the phone now says the car screen may be waiting for a permission prompt.

## 0.13.70 (2026-10-18)

- Phone key: if the car's lock controller is not ready, it retries up to two more times for the same approach. Short reading gaps no longer cancel the unlock. A short log of decisions made while the car is off stays on the car only and is never sent over the network.

## 0.13.69 (2026-10-18)

- New: Phone key (DiLink 3). With the car off, the doors unlock when you approach with your phone and lock when you walk away. In System › Phone key you pick your phone, the unlock and lock distances and the response speed (Fast, Balanced, Safe). It is off by default and asks for confirmation when you turn it on. Classic Bluetooth signal does not measure metres; distances are approximate and work best at 2–3 m. Keeping Bluetooth on after the car switches off uses a new Android (Bluetooth) permission.
- The clip player in the car can go full screen.
- Sentry follows the “only when the car is fully off” option. If Sentry is set not to run in a safe place, parking recording no longer starts there either.
- Phone: when Sentry is on but parking recording is off, the Security summary shows a warning with a one-tap fix. If an automation cannot be saved, the reason now appears inside the window.

## 0.13.68 (2026-10-17)

- Sentry clips: you now choose what to see. Boxes and timeline markers can each be set to Off, Alarm cause, Detected or All. Older clips show only the alarm cause.
- DiLink 3 instrument cluster: “Card layout” is no longer offered on the Seal, where it could leave the cluster in another model’s layout. After a manual size choice, the cluster returns to the car’s own size when the session ends.
- Fixed a generic photo flashing instead of the car when pressing “Rotate” on the home scene.
- Added the Atto 2 car image.
- Power mode and battery protection are not rewritten when the car already has the requested value.
- Improved Sealion 7 camera diagnostics and the USB model-loading instructions.

## 0.13.67 (2026-10-17)

- Sealion 7 (DiLink 5): a new OEM camera path connects live view, recording and sentry. The old built-in camera selection migrates automatically. A failed camera start no longer flashes the recording badge. Unverified hood readings are shown as unknown; diagnostics were expanded. DiLink 3 and external USB selections are preserved. Real-vehicle verification is ongoing.
- Fully close other camera apps before testing. Yoldas does not forcibly stop another camera producer. Download the sentry detection model once or import it from USB; instructions are on the download page.

## 0.13.66 (2026-10-16)

- Download the sentry model once or load it from USB without increasing APK size. The in-app model guide opens step-by-step website instructions.
- Model download, file selection, verification and failures are logged for support. The SL7 preview uses its separate camera path; unverified trunk codes are not shown as Open. Physical validation of remaining SL7 camera and cluster issues continues.

## 0.13.65 (2026-10-16)

- Sealion 7 (DiLink 5): added a step-by-step connection guide in setup and the Yoldaş helper. Android approval and firmware-dependent service menus are explained separately; opening general settings is not treated as a successful connection.
- Existing authorized ADB connections are preserved. OEM preparation was completed; after a failed normal attempt, users can choose classic ADB recovery. This may disable TLS wireless debugging and briefly disconnect other ADB apps; Android approval is still required.
- Setup, TLS/classic mode, system settings, Android authorization and helper launch stages are recorded with a support code. Physical validation on SL7 continues.

## 0.13.64 (2026-10-16)

- Sealion 7 (DiLink 5): added the missing Android debugging activation step during vehicle connection setup. The setting is read back and the result is recorded for support. Camera, sentry and instrument display validation on vehicles continues.

## 0.13.63 (2026-10-16)

- Sealion 7 (DiLink 5): the vehicle connection during setup is fixed. Android now asks for approval only once, the wait is shorter, and the “Prepare connection” button opens the right settings screen. If the connection gets stuck, the step it stopped at is recorded for support.

## 0.13.61 (2026-10-15)

- Recording to a memory card: you can choose the vehicle's internal storage or a memory card / USB as the recording location. A card that drops out when the car switches off reconnects by itself; if there is no card, recording goes to internal storage and the screen tells you.
- Recording safeguards: Sentry, hard-brake and manually marked recordings are no longer lost if the card fails; the event clip is always also produced on the vehicle's internal storage. Short recording gaps seen on slow cards are fixed. Recordings on internal storage and on the card appear in a single list.
- Select and delete recordings: in the car on the Recordings screen, and on the phone under Continuous recordings (the car app must be up to date for selection on the phone).
- Dutch language support added (app and website).
- If the app closes unexpectedly, the cause is written to the diagnostic log for support.
- Camera, Sentry and gauge groundwork plus field diagnostics added for DiLink 5 (Sealion 7); verification in the car is ongoing.

## 0.13.49 (2026-10-15)

- Sentry: a parked car no longer triggers a “vehicle passed” alert because of small movements such as raindrops. A vehicle is reported only if it really moves from its spot or a new one arrives. Person and animal detection are unchanged.
- Sentry: false “person” boxes that fill the whole frame, such as the back of a car very close to the camera, no longer count as a person.
- When you play a clip, the object that triggered the alert is shown with a box and a “Person / Animal / Vehicle” label (four-camera recordings, new clips). The label is for display only and does not affect alerts; the box is not burned into the video.
- Recording and protection: you can choose the recording segment length (15 s, 1 min, 5 min). Longer segments mean fewer files and uninterrupted viewing, but a clip is ready later and if recording is cut off that segment is lost. Default 15 s.
- Find my car: the light-only and horn + light options are now open to every user who is allowed to control their own car.
- Drive mode and regeneration choices are one tap away at the left of the cockpit and on the phone; the old cockpit buttons are back.
- Cluster recovery and network recovery were improved.

## 0.13.40 (2026-10-15)

- BYD account linking and BYD cloud controls have been removed. Lock and unlock use the vehicle’s local Yoldaş connection.
- Remote climate control runs without switching on general vehicle power. Choose 17–33 °C and 10/15/20/25/30 minutes on the phone; status is read back from the car after refresh.
- A separate safe-use agreement is required for new and existing users. Its accepted version and date are recorded. Acceptance on the phone or vehicle syncs to the same account’s vehicle. Pending acceptance does not stop background connectivity or update checks.
- Automations include a guided editor, nested conditions, steering-wheel buttons, signed HTTP calls and retries. Wireless charging, steering-wheel and seat heating/ventilation, ambient brightness/color, daytime-light activation, tailgate opening height and HUD actions are now public. Availability depends on vehicle hardware; results are read back from the car.
- Window controls use the local path while the car is on. No general power-on is used to move windows when the car is off because a safe remote path is not established. Cloud-dependent horn/hazards and sentry light deterrence have been removed.
- The latest APK is available on the website and automatic update channel. Installation restarts the app and may briefly interrupt connectivity; the new agreement does not prevent reconnection.

## 0.13.29 (2026-10-14)

- Automations were redesigned: categories, step-by-step setup, steering-wheel button triggers and new car commands were added.
- A new diagnostic tool that only reads key proximity was added.

## 0.13.26 (2026-10-14)

- Staying connected while the car is off is stronger: if the car loses internet, it is woken every 30 seconds for the first 10 minutes, then every 2 minutes (up to 6 hours), and the screen backlight is kept off. The result is sent to the Yoldaş team as short codes.
- The car’s automatic-start setting is now found even when the app list is long: if Yoldaş’s row is off screen, the list is scrolled.

## 0.13.25 (2026-10-13)

- Sentry: headlight or lamp glare no longer triggers an “other motion” alert (when the Light filter is on). Detection of people, animals and vehicles is not affected.

## 0.13.24 (2026-10-13)

- After an update, the car blocked Yoldaş again in its “Disable automatic start” list, so you had to switch it back by hand every time. Yoldaş now fixes this itself: the car’s settings window opens for a few seconds and closes, and only Yoldaş’s own row changes.
- The helper’s automatic-start result is now also written to the diagnostics log, so cars with problems are easier to investigate.

## 0.13.23 (2026-10-13)

- If something goes wrong during an update (for example the install is rejected), the reason is now shown clearly and sent to the Yoldaş team as a short code. If the safeguard that restarts Yoldaş after an update cannot be set up, the update is postponed and retried later, so the app does not stay silent after updating.

## 0.13.22 (2026-10-13)

- To track down connection problems: when the car loses internet, it records how long and the state (screen, network, signal) as short codes and sends them to the Yoldaş team once it is back online. No personal data.
- “Door left open” and “lock open” notifications now also check the car’s latest reading when a closing message was missed (for example during an update), so a closed door no longer triggers a false alert.

## 0.13.21 (2026-10-13)

- Automations are much more powerful: about 60 car states (door, lock, gear, window, battery, tyre and more) can be a trigger or a condition. Combine conditions as “all” or “any”; gear changes to P, R, N and D come as ready choices.
- If an automation did not run, its history tells you why (for example “Battery had to be below 5%, now 60%”). Before saving a new flow, “Try on the past” shows how many times it would have run in recent days.
- You are warned when you save two automations that do opposite things. Shadow mode only records in the history what an automation would do, without running it. New steps: call a web address, media and sound, on-screen message. Ready-made templates were added.
- Door, lock and gear changes are now caught instantly from the car’s own notification, so automations tied to them run faster.
- Hybrid (DM-i): total km driven on electricity and in hybrid mode now shows on the phone. It stayed empty before because the car did not send it.

## 0.13.16 (2026-10-12)

- Fixed the “Car connection is off” warning and the helper never connecting: a half-written leftover record from an update could silently shut the helper down on every start. A damaged record is now deleted and the helper starts.

## 0.13.15 (2026-10-12)

- After an update finishes, the “Car updated” notification and the version shown on your phone now arrive right away: the car reports as soon as it restarts (no constant polling, a few hundred bytes per update).
- On the phone, the live camera in full screen was shifted down and cropped at the bottom; fixed.

## 0.13.14 (2026-10-12)

- You can now change the update settings from your phone too: “Update settings” in the car version screen (automatic or only me, Wi-Fi/mobile data and car-state choices, install while driving when you start it). The car reports its setting to the phone.

## 0.13.13 (2026-10-12)

- Yoldaş now restarts by itself after an update. When an update arrived while the car was off and parked, the app did not restart and the phone connection stayed down until the next drive; fixed.
- Update settings: automatic, or only when you start it. If automatic, you choose each combination: Wi-Fi or mobile data, with the car off, on and stopped, or driving. You can also allow manual updates while driving. “Silent update” is now called “Install without asking”.
- A “Update now” button in the car version screen on your phone, and an “Car updated” notification. The phone’s out-of-date icon now actually appears when the car’s app is old.
- A small “Send route to car” shortcut in the home screen header.

## 0.13.10 (2026-10-12)

- Sentry: the detection model (4.6 MB) now downloads over the car’s own mobile data as well as Wi-Fi (not while roaming). Cars that are always on mobile data or a phone hotspot could not start Sentry because the model was “not downloaded”.
- If the model is missing when you try to turn Sentry on from your phone, the download now starts by itself; just try again in a few minutes, no need to go to the car screen.

## 0.13.9 (2026-10-12)

- Sentry: the detection area (distance and your “Ignore” zones) now applies to the point where a person or car meets the ground. Nearby people are no longer missed at “Near” distance or with a narrowed area, and a zone drawn on the road ignores passing cars better.
- Update: if Android’s install confirmation never arrives, the screen no longer stays on “Installing…”; it reopens after a short time and says what to do.
- If the car connection (helper) does not start, the reason is recorded in more detail for support.

## 0.13.8 (2026-10-12)

- New: Yoldaş comes to the screen by itself when the car is switched on or the screen wakes. Turn it off in System › “Open on start-up”; it opens at most once every 3 minutes.
- Fixed a car connection (helper) start problem: in version 0.13.5 some cars could not connect.
- If the helper does not start, the reason is now recorded in more detail for support.

## 0.13.4 (2026-10-12)

- Two layouts for the car’s driver-assist card that grows while casting to the screen behind the steering wheel: “Standard” and “Card layout” in System › Cluster. Card layout is experimental; you can mark the result as “Fixed” or “Still large”.
- New “Control cluster” window: see and use the cast app from the centre screen in a small, draggable window without interrupting the cast; it supports touch, two-finger zoom, an address search box and a hide-keyboard button.
- Turn-signal camera: fast left/right changes now work, and the camera stays ready even when app casting is off. “Back to the car’s cluster” is active only while something is really being cast.
- Switching to another app while casting no longer sends the cluster back to the car’s own screen; the new app comes in the same session.
- Better recovery from casting drops: short drops restore by themselves, and repeated quick drops stop.
- When the car connection (helper) starts, a stale helper left on the car is cleaned up; if it cannot start, the reason is recorded for support.

## 0.12.97 (2026-10-11)

- Yoldaş no longer appears in the car’s “recent apps” list, so “clear all” no longer stops Yoldaş, the parked connection or casting. Open Yoldaş from the home screen or the dock.
- On plug-in hybrids the Car tab shows the kilometres driven on electric and on hybrid, and the share driven on electric.

## 0.12.96 (2026-10-11)

- Only the app you cast, the centre screen and the turn-signal camera appear on the screen behind the steering wheel; the car itself shows speed, gear and warnings. Yoldaş’s own speed and gear drawing was removed, so the tablet works less.
- Turn-signal camera: left and right cameras are placed separately, appear at once (15 frames per second) and stay for the time you choose after the signal ends.
- Send a route from your phone to the car: type an address, a place name, coordinates or a map app’s “Share route” link, then choose “Get directions” or “Start”. There is a Paste button; on Android you can also send it from the share menu.
- A button to bring the cast app back to the centre screen to enter a route. “Back to the car’s cluster” keeps the Yoldaş screen in front.
- Margins and cluster size apply as soon as you release the slider. After a temporary error (such as a guard delay) casting restores itself; dialogs like location permission no longer close it.
- If the car has no free space, the update now says what to do. On Atto 3, Dolphin and similar models the cluster can be tried as experimental.

## 0.12.85 (2026-10-11)

- On the car, Recordings › Continuous: continuous-recording parts are grouped into drives, which you can watch and delete group by group (protected clips are kept). The same grouping is on the phone.
- A “Show info label” checkbox in the clip player (off by default), on the car and the phone. On the car, speed, gear, pedals, signals, steering and battery are drawn using your phone settings; it works on newly recorded parts.
- When the car is turned off and on, mirroring to the instrument cluster resumes where it stopped (Settings › Cluster: “Remember last mode when the car starts”, on by default).
- Fixes: video not playing after switching parts in continuous recording, the picture shifting after leaving fullscreen on the phone, and an “Something went wrong” error on some screens.

## 0.12.82 (2026-10-11)

- The boot button is disabled while the car is moving, on both the car screen and the phone (“Off while driving”), so it cannot be pressed by mistake.
- The car now also draws the 360° view for Seal U, Seal U DM-i, Atto 3 and Dolphin (same as on the phone).
- Notifications: “Cable plugged in” and “Charging started” are now separate and both on by default. “Charging started” arrives once you confirm at the station and power actually flows.
- Phone: a large slider, fine-step arrows and zoom on trip charts; an old page left open notices the new version and refreshes itself.

## 0.12.81 (2026-10-11)

- The clip info label is now a visual driving dashboard: next to speed and gear, the accelerator and brake pedals, turn signals and hazards, steering wheel and headlights (and, optionally, the seat belt) are drawn under the video. Switch items on or off in Security › Recordings › Info label on your phone; you can go back to the “Text” style. It works on new recordings; older clips only show speed, gear and battery.
- Charging records: fast charging is now correctly shown as DC (the car could report “AC” even on fast chargers). For each charge you can enter the kWh from the station receipt; if you do not, an estimate with a loss allowance (DC 4%, AC 10%) is used for the energy that reached the battery. Your own ratio is learned as you enter values. Details: charging price guide.
- The steering angle for the info dashboard is read 4 times a second while driving.

## 0.12.80 (2026-10-11)

- Safe places: even when GPS gives no location while the car is off or in a garage, the precise location taken when you parked is used for that whole stop, so Sentry does not switch on needlessly at your safe place. The parking location is cleared when you start driving.
- If the location is not precise enough (worse than half the radius), Sentry stays on the safe side and runs. Leaving a zone has a 20 m margin, so GPS jitter does not turn Sentry on and off. We recommend a safe-place radius of at least 100 m.
- The safe-place location is now tracked at most 5 seconds apart while driving (it used to be once a minute).

## 0.12.79 (2026-10-11)

- While parked, recording automatically switches to the sharpest setting; while driving it uses the quality you chose. Turn it off with “Highest quality when parked” in Recording and protection (on by default).
- If the car heats up, recording while driving steps down one level and returns when it cools. Turn it off with “Lower quality when the car heats up”. You can change both settings from the phone too.
- Recording qualities were retuned: Normal uses less processing (960×720) and High records 1280×960 at a higher bit rate. The aim is to reduce lag on the main screen; results may vary by car.
- The file location of a recorded video in the car is shown under the video, on the car screen and on the phone.
- If a phone call starts while audio recording is on, the microphone is released immediately and taken back when the call ends, so your voice in the call is not affected.
- If a screen in the phone app hits an error it no longer stays black: a “Something went wrong” screen appears and you can retry, switch back to the classic view or clear the cache.

## 0.12.72 (2026-10-10)

- Sealion 7 (DiLink 5): permission errors raised in the background by BYD’s own library no longer close the app; if one happens its cause is logged with a short code. The diagnostic report now runs more safely on these cars and only tries the devices the normal reading path already uses.

## 0.12.71 (2026-10-10)

- Sealion 7 (DiLink 5): the first version that tries to read vehicle measurements through BYD’s own package. If values such as speed, doors and tyres can be read they appear on the phone; battery and range are not guaranteed yet. A value that cannot be read is never shown as 0.

## 0.12.70 (2026-10-10)

- You can now send the car's information to the Yoldaş team: with the “Send to server” button in System › Diagnostics › Compatibility report, or from the phone with Account › Send diagnostic report. Nothing is sent automatically; the report contains no chassis number, location or account details.
- Preparation for the Sealion 7 (DiLink 5): the compatibility report also collects the class list of the BYD packages installed on the car, permissions and connection status. On these cars Camera and Sentry appear inactive on the phone, with the reason shown.

## 0.12.69 (2026-10-10)

- The phone now gets a notification when a new Yoldaş version is released; tapping it opens this page. It is on by default and can be turned off in Account › Notifications.
- If the camera image Sentry receives does not change at all for 2 minutes, one short entry is logged to help investigate problems. It contains no personal data.

## 0.12.68 (2026-10-10)

- Door, boot, bonnet and lock changes reach your phone faster. The phone now has “opened” and “closed” notifications for them; they are on by default and can be turned off in Account › Notifications.
- To help investigate problems, Sentry, recording and phone-connection state changes are logged with short codes. A small entry is sent only at the moment a state changes; it contains no personal data.
- Tapping the “New version available” notification on the phone opens this page.

## 0.12.67 (2026-10-10)

- New: locally generated debug setup codes and automatic entry on supported BYD screens. Setup has a separate permission; a crash when opening BYD permissions was fixed.
- Debug mode and the Yoldaş helper

## 0.12.66 (2026-10-09)

- Tyre pressure recommendations match the vehicle model. Tang also includes the rear pressure for a full load.
- Tyre warnings calculated from recommended values were removed. Pressure and temperature readings from the car remain available.
- Pressure information is clearer in the car and on the phone. Unknown models do not receive another model’s recommendation.
- An incorrect model-specific side-camera description was removed.

## 0.12.65 (2026-10-09)

- **Settings saved on your phone reach the car within half a minute:** Automations, the screen alert and other settings you save on the phone appear in the car within 30 seconds while the phone app is open. This used to take hours.
- **Park monitoring status shows steadily on the phone:** The car reports it more often, so “No park monitoring info” appears much less.
- **“Last 24 hours” and “Last night” count correctly:** On days with heavy detections, the night no longer shows 0.
- **Recordings window in the car:** The “Why it was kept” card and the Protect and Delete buttons fit on screen.
- **Car picture on the phone:** Seal U, Seal U DM-i, Atto 3 and Dolphin pictures fit their frame; the battery percentage no longer overlaps the title.

## 0.12.53 (2026-10-07)

- **Slope now shows its direction:** uphill reads + and downhill reads −; the line tilts to match.
- **Single-camera view is now open on all BYD models:** in live view you can pick front, rear, left and right one by one (except DiLink 5). The layout is verified on the Seal; other models assume the same order.
- **A black live-camera screen now recovers on its own** , and quick back-to-back direction taps are no longer dropped.
- **Rankings renewed:** today, 7 days, 30 days and all time; the top three values show anonymously and you see your own rank in every category. Joining is automatic.
- **Trips and Recordings:** the trip list and charts are fixed, and Recordings gets a Motion filter.
- **Charging notifications:** “Charging started” when you plug in, and “charging finished” with start/end percentage, energy added and duration.
- **Charge summary:** The first time you open the app after a charge, duration, times, energy, power and cost appear on one card.
- **Charging scene:** While the car charges, the My car screen turns green with a fill ring, flowing energy and a live power curve.
- **Model filter in rankings:** Compare only with your own model; high and low consumption are ranked separately.

## 0.12.51 (2026-10-07)

- **Sentry catches brief passes better:** Even when a person or vehicle crosses the camera quickly, seeing it in two frames is enough.
- **Trips screen refreshed:** The list opens on Today, and tapping a day shows that day's trips. The detail now also shows time moving, average speed while moving, climb and descent, brake use and hardest braking; charts now draw at full width.
- **Motion filter in Recordings:** Filter unrecognized movements with one tap.
- **Video starts right away on iPhone:** Tap Play and the clip starts without waiting for the whole file.

## 0.12.50 (2026-10-07)

- **Sentry spots approaching people and vehicles earlier:** Sensitivity levels were retuned on real parking recordings; frames with motion are checked twice a second.
- **Unrecognized movement is reported too:** If something moves but is not recognized as a person, animal or vehicle, you get an instant “movement” notification; the same event does not notify you again and again.
- **Event clips are shorter:** A clip is now cut close to the time you set (before and after the event) instead of keeping whole 15-second recording segments.
- **Slope indicator:** The road slope shows next to the speed in the cockpit tab and on the phone driving screen.

## 0.12.26 (2026-10-06)

- **The warning works on the car screen:** When someone approaches the car, the car screen wakes up and shows the message you have set; you can turn it on or off from the Security summary on your phone.
- Status badges (recording, parked watch, clip transfer) sit in a single strip at the top of the screen and no longer overlap the buttons. When the Yoldaş bottom bar is open, the buttons no longer end up behind the bar.
- **Cluster display:** The transfer you used last continues as it was when the car is switched on again; speed and gear can be turned off separately; margins load at startup. When the turn signal camera is set up for the first time, it is placed in the middle of the screen.
- Phone notifications are simpler, are sent the moment an event happens, and tell you which camera saw it.
- **Recording resilience:** If the microphone disconnects, recording continues silently and the audio is restored; if a segment cannot be closed, recording does not stop. Recording health is written to a log in the car.
- The car screen size is reported, without any personal data, so the app can fit models with small screens.

## 0.12.17 (2026-10-06)

- **The connection continues after the car is switched off:** With remote control and the Yoldaş helper turned on, the link to your phone is not dropped when the ignition goes off. If the battery or the 12 V battery gets too low, the connection is released automatically. Details
- **Event markers in recordings:** Moments when a person, an animal or a vehicle appears in a clip are marked on the timeline; a clip with several events shows all of them.
- Hard-braking detection is more accurate, and unnecessary clips are fewer.
- If a segment cannot be closed during recording, the recording recovers right away.
- The "range at your driving style" on the phone gives the same result as the calculation in the car.
- **Recordings stay in the car:** Recordings are not uploaded to the server on their own; they are taken from the car only when you choose "Send to phone" on your phone. The old "Prepare recordings for the phone" setting has been removed.

## 0.12.7 (2026-10-05)

- Updates can also download over mobile data when you are not roaming.
- Sentry: telling people, animals and vehicles apart is more accurate using the zoomed-in view of the camera where movement is seen; stationary objects that do not move do not create events.
- The radar on the phone shows more accurately which camera an event came from.
- Recordings are uploaded when requested from the car; data use is lower.

## 0.11.12 (2026-10-05)

- **Recording and protection:** Driving and Parked recording modes, hard-braking protection, clip badges and filters, manual marking.
- **Safe places:** choose whether Sentry stays off or runs quietly at home or at work; time ranges; a map and address search on the phone.
- Detection area: choose the region to watch by camera, distance and grid; the car learns your parking spot.
- If recording stops, the reason is shown in the car and on the phone; if the hardware encoder cannot start, recording continues with the software encoder.
- Simpler setup: connecting the car is optional.

## 0.10.14 (2026-10-05)

- Link your account from the phone with a QR code or a code; a single-screen first setup in the car.
- Sentry tells people, animals and vehicles apart; sensitivity setting and a light/shadow filter; clips are protected before and after an event.
- While the car is off, connection limits are set from the phone; recordings are taken in 15-second segments.

## 0.10.5 (2026-10-04)

- Open and close each of the four windows from your phone with a 0–100% target; the shared Stop cancels the movement. Remote control
- Front defrost and rear window heating in the A/C details. 11 themes and a classic look on the phone.
- The turn camera can show on the Centre screen, the Instrument cluster or Both. Turn camera
- The cluster display got better screen and area checks, and margins. Cluster display
- A missing lights reading is no longer shown as "off".

## 0.10.4 (2026-10-04)

- **Connectivity while parked:** with the Yoldaş helper on, CPU and Wi-Fi support is provided on its own; it works within limits set by the car's current state, the battery, the 12 V battery and temperature. Details
- If the app closes unexpectedly, it is restarted under suitable parking conditions.

## 0.10.3 (2026-10-04)

- Automations got triggers for arriving at and leaving a place, and a location condition.
- Vehicle actions in automations: A/C, front and rear defrost, air circulation, windows, trunk, driving mode. An editable morning preparation template. Automations
- Steps can notify your phone; run history shows in the car and on the phone. Automation notifications must be turned on in the phone app.

## 0.10.2 (2026-10-04)

- Sentry events also record which camera the image came from (front, rear, left, right).
- You place the turn camera window anywhere you like by dragging it in the preview.
- **Custom bottom bar:** a Yoldaş bar with your own shortcuts; optional Home app choice. Bottom bar
- The Sentry screen alert is now a separate preference connected to the helper.

## 0.10.1 (2026-10-04)

- Text on secondary screens is easier to read in the dark theme.
- The background connection is more stable.

## 0.10.0 (2026-10-04)

- **Automations:** your own routines that run when the car turns on, at a set time, at 100% battery or at the press of a button. Details
- **Recording preferences:** when to record (in P, while the car is off, while driving, 24/7), quality, storage space and cabin audio. Dashcam
- **Turn camera:** when you signal, the camera on that side opens on the center screen. Details
- Fixed the weather card calculation on hybrid cars.

## 0.9.1 (2026-10-04)

- **Seal U DM-i support:** total range, fuel level percentage and fuel consumption, SAVE status.
- **Compatibility report:** model and software details with one tap; contains no VIN or location.
- **Lighter, smoother performance:** improved how often car data is read and how screens are drawn.
- **Trunk:** opens while the car is stopped; the speed is read from the car before every command.

## 0.9.0 (2026-10-03)

- **New Yoldaş design:** seven tabs (Cockpit, Car, Driving, Security, Energy, Trips, System), ten cockpit styles, and how fresh the data is on every screen.

## 0.8.6 (2026-10-03)

- **Turn Sentry on and off from your phone.** The result is read from the car.

## 0.8.5 (2026-10-03)

- **Live camera:** faster start; switch camera and quality while watching, full screen and 90° rotation.
- A separate step for camera and audio permissions on first launch.

## 0.8.1 (2026-10-02)

- Automatic free license for the pilot; no code to enter.
- Recording while driving, downloading recordings to your phone, person detection while parked, cabin audio and talking to the car.

## 0.7.0 (2026-10-01)

- Moved to the permanent server (api.yoldas.io).

## 0.6.7 (2026-09-30)

- **App lock:** with a PIN.
- **Units:** km/miles, °C/°F, kW/PS/hp, bar/kPa/psi.
- **Car appearance:** color, wheel color, window tint, license plate.
- **Connection test:** checks Wi-Fi and mobile data separately.
- **Welcome:** a greeting based on the time of day, battery and range at startup.
- Messages from the phone to the car screen, V2L status, charging curve and phone notifications.
- Nearby charging stations (OpenStreetMap).

## 0.6.0 (2026-09-30)

- **Cameras:** all four cameras together or one at a time, live.
- **30-second recording:** four cameras in one file, recording health, playback and protection.
- **Remaining energy (kWh):** from the car's own measurement.
- Event feed, charging sessions, and Charges and Events tabs in the car.

## 0.5.3 (2026-09-30)

- **Automatic updates:** downloads the new version; checks integrity, package name, version and signature; installs with one tap.

## 0.4.9 (2026-09-30)

- **Remote control:** windows, trunk, locks and A/C.
- **360° Seal in six official paint colors** , tire pressure card.
- **Pet screen** and driver profiles; preferences sync between the car and your phone.
- Seven languages, range based on your driving, comparison with a gas car, driving score and break reminder.
