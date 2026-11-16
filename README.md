# Kwa60 for Android

Phone-first Expo / React Native storefront for Kwamakhi Store. The layout follows the supplied SPAR2U screenshots: a store header, search, aisle cards, two-column products, and bottom navigation for Home, Products, Orders, Profile, and Cart.

## Run on Android

1. Install Node.js and Expo Go on an Android phone (or configure an Android emulator).
2. The supplied Kwa’Sixty logo and the eleven earlier product photos are bundled under `assets/`. Their product crops are in `assets/cropped/`; surrounding promo headlines and price panels are trimmed while packaging labels are kept.
3. Run `npm install` and `npm run android` (or `npm start` and scan the QR code in Expo Go).

The product photos show four clear pack prices: baby wipes R19.99, roll-on R11.99, rose tissue oil R19.99, and the diaper jumbo pack R169 (the image also shows R1.69 per nappy). The other product images do not show a pack price, so those items say “Ask in store” instead of using a guessed price. The cart displays the R100 minimum spend from your reference screen.

The profile form and delivery-address form work in the browser prototype and save details in that browser’s local storage. They do not create a verified customer account or sync to a store server. The Products screen has selectable category chips, a searchable two-column catalogue, and tappable product detail sheets.

Checkout, card settlement and live order dispatch are demonstration flows. A backend connection is needed for real payments, customer accounts, inventory and cross-device driver tracking. The map below uses live foreground device location locally.

## Driver flow and map

Open **Profile → Driver dashboard**. The driver sees the customer’s current basket, checks off picked items, and sees grocery spend separately from the sample R28 delivery pay. The till step is a preview only: no Makhi card is charged. Orders with products whose prices are not visible in the supplied photos cannot be confirmed until their store prices are set.

After the till step, the Android app requests foreground location and opens an in-app map with the driver and delivery address. While Kwa60 is open, the driver marker updates and the customer Orders screen can show that map on the same device. **Cross-device customer tracking and real customer orders require a live dispatch backend**; none is configured in this workspace. Turn-by-turn directions can also open in the phone’s maps app.

The Android map uses the requested [Snazzy Info Window](https://github.com/atmist/snazzy-info-window) on Google Maps when `EXPO_PUBLIC_GOOGLE_MAPS_API_KEY` is configured in `.env` (start from `.env.example`). Snazzy Info Window decorates Google Maps JavaScript markers; it does not provide map tiles or routing. Without a Google key, the app falls back to an OpenStreetMap map.
