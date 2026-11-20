# Ortus design

The screens Ortus is built to match. Each board is one screen at 1440 x 900 (web) or 390 x 844 (phone), dark theme, with one sample world: the Ministry of [Name] during a flood on Wednesday 18 November 2026.

- `boards/` the boards as HTML, the source of truth. Open one in a browser to see it.
- `screens/` a PNG of every board, rendered from `boards/`.
- `stories/` the four user stories as storyboard strips (S1 crisis, S2 admin, S3 new hire, S4 citizen).
- `DENSITY_RULES.md` the type, spacing and density rules every screen follows.
- `tools/render.sh <Board>` renders a board again; `tools/generators/` are the scripts that wrote the boards and the stories (`story.py` holds every story step and the board it uses).

The live design canvas is https://claude.ai/artifact/DvR1bLwSezFgqvuq8RPBPy and the stories document is https://claude.ai/artifact/PsucNKvE4zc5xnQg5gT98W. Where they differ from this folder, the canvas wins; copy changes here.

## Boards by release

| Release | Board | Screen |
| --- | --- | --- |
| V1 | `AdminBackup` | Admin · Backup, API & integrations |
| V1 | `AdminDeliverability` | Admin · Deliverability |
| V1 | `AdminDomains` | Admin · Domains & DNS |
| V1 | `AdminFirstRun` | Admin · First run (setup checklist) |
| V1 | `AdminSignIn` | Admin · Sign-in policy & devices |
| V1 | `AdminSovereignty` | Admin · Sovereignty & compliance |
| V1 | `AdminUsers` | Admin · Users & quotas |
| V1 | `AppSwitcher` | Web · App rail + all apps |
| V1 | `Main` | Web · Inbox + agenda |
| V1 | `MobileAdmin` | Mobile · Admin |
| V1 | `MobileApprovals` | Mobile · Approvals & tasks |
| V1 | `MobileCalendar` | Mobile · Calendar |
| V1 | `MobileChannel` | Mobile · Channel |
| V1 | `MobileChats` | Mobile · Chats |
| V1 | `MobileDoc` | Mobile · Document |
| V1 | `MobileDrive` | Mobile · Drive |
| V1 | `MobileInbox` | Mobile · Inbox |
| V1 | `MobileMore` | Mobile · More (all apps) |
| V1 | `MobileNotifications` | Mobile · Notifications |
| V1 | `MobileSearch` | Mobile · Search |
| V1 | `MobileShare` | Mobile · Share sheet |
| V1 | `MobileTasks` | Mobile · Tasks |
| V1 | `MobileThread` | Mobile · Thread + RSVP |
| V1 | `MobileWelcome` | Mobile · Welcome and phone enrolment |
| V1 | `WebApprovals` | Web · Approval + e-signature |
| V1 | `WebCalendar` | Web · Calendar (week) |
| V1 | `WebCall` | Web · Call + shared doc |
| V1 | `WebChat` | Web · Chat (channels + thread) |
| V1 | `WebCompose` | Web · Compose |
| V1 | `WebContacts` | Web · Directory & contacts |
| V1 | `WebDocEditor` | Web · Document editor |
| V1 | `WebDrive` | Web · Drive |
| V1 | `WebFilePreview` | Web · File preview + share |
| V1 | `WebMustRead` | Web · Read and confirm |
| V1 | `WebNotifications` | Web · Notification centre |
| V1 | `WebPersonal` | Web · Apps, offline, language, AI |
| V1 | `WebRecordFiled` | Web · Record signed and filed |
| V1 | `WebReview` | Web · Review before signing |
| V1 | `WebSearch` | Web · Search |
| V1 | `WebTasks` | Web · Tasks & projects |
| V1 | `WebWelcome` | Web · Welcome (first run, empty states) |
| V2 | `AdminDevices` | Admin · Devices (MDM) |
| V2 | `AdminPolicy` | Admin · Device policy |
| V2 | `AdminSecurity` | Admin · DLP & threat protection |
| V2 | `MobileApproveLogin` | Mobile · Approve sign-in |
| V2 | `MobileBooking` | Mobile · Book appointment |
| V2 | `MobileCitizenAnswer` | Mobile · Citizen reads the answer (public) |
| V2 | `MobileCitizenForm` | Mobile · Citizen form (public) |
| V2 | `MobileCitizenReceipt` | Mobile · Citizen receipt |
| V2 | `MobileRecords` | Mobile · Case file |
| V2 | `MobileScanQR` | Mobile · Scan QR |
| V2 | `OSApps` | Ortus OS · Classic layout + real apps |
| V2 | `OSControl` | Ortus OS · Search & control centre |
| V2 | `OSDesktop` | Ortus OS · Desktop shell |
| V2 | `OSDialogs` | Ortus OS · System dialogs |
| V2 | `OSFirstBoot` | Ortus OS · First boot & enrolment |
| V2 | `OSLock` | Ortus OS · Lock screen |
| V2 | `OSOverview` | Ortus OS · Overview & app switcher |
| V2 | `OSSecurity` | Ortus OS · Settings: privacy & security |
| V2 | `OSStore` | Ortus OS · Software centre |
| V2 | `WebAppointments` | Web · Appointments |
| V2 | `WebBooking` | Public booking page |
| V2 | `WebForms` | Web · Forms & surveys |
| V2 | `WebRecords` | Web · Case files & records |
| V2 | `WebRooms` | Web · Rooms & resources |
| V2 | `WebSharedMailbox` | Web · Shared mailbox & delegation |
| V2 | `WorkstationLogin` | Ortus OS · QR sign-in (greeter) |
| Later | `MobileRoom` | Mobile · Drop-in room |
| Later | `MobileTownHall` | Mobile · Town hall as a guest (public) |
| Later | `WebDiscover` | Web · Discover & join spaces |
| Later | `WebIntranet` | Web · Intranet, wiki & news |
| Later | `WebSpace` | Web · Space with rooms |
| Later | `WebWebinar` | Web · Webinar / town hall |
