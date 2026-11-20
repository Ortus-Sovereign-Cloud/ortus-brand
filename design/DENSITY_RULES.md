# Density pass "dense2" — rules (pilot: Main.dc.html, see gen/dense_main.py for the exact edits)

Goal: calmer, roomier screens. Boards are fixed size (web 1440x900, phone 390x844), so room comes from
removing and enlarging, never from shrinking type.

1. Mono caps only for: classification labels (PUBLIC / INTERNAL / OFFICIAL-SENSITIVE / SECRET), IDs, serials,
   case numbers, DNS records, code, kbd "Ctrl K". Everything else in Geist, sentence case: section headers,
   table column headers, status chips ("Active" not "ACTIVE"), dates ("Wed 18 Nov"), labels like TL;DR -> "Summary",
   "NEXT · IN 22 MIN" -> "Next · in 22 min". Times and numbers: Geist 13px with `font-variant-numeric: tabular-nums`.
   No `text-transform: uppercase`, no letter-spacing on labels.
2. Type floor: 13px everywhere (rail/app-bar labels 11–12px exempt). Secondary text 13–14px #9198A8, body 15px.
3. Sizes: nav items 40px high; buttons 40px (36px min inside cards); icon buttons 40px; avatars 40px;
   list rows padding 14px 16px (>= 60px tall); table rows >= 60px; chips 13px text, padding 2px 8px.
   Phone: rows >= 64px, gutter 16px, tap targets 44px.
4. Spacing scale 8 / 12 / 16 / 20 / 24 / 32. Card padding 20–24px (web), 16px (phone). Gap between cards 16px.
   Page padding 24–32px.
5. One secondary line per row, at most 3 facts per row. Cut the rest (snippets under subjects, extra meta lines).
6. One filled accent button per screen. Other actions outlined or text.
7. Remove duplicate or tertiary chrome: header account avatar and "Live" dot when the rail already has them,
   keyboard hint letters (keep "Ctrl K"), promo/tertiary side cards. If rows no longer fit, drop rows, not size.
8. Must fit: web h <= 900 (the three fluid boards may keep or grow their height, report it), phone h = 844 and the last
   list row must end above y = 748 (bottom nav) — look at the screenshot, measure.py does not catch clipping
   inside `overflow: hidden` lists.
9. Do not change: the sample world, names, times, case numbers, links (href), the rail markup, `{{accent}}`,
   data-props, the `/*type2*/` marker (append `/*dense2*/` right after it when a board is done).
