import sys; sys.path.insert(0,'/tmp/claude-1002/-home-bohdaq-git/6b5adcb0-31d6-44c8-b201-55c34d7527ea/scratchpad/gen')
from dense_admin_lib import *
T13="font-size: 13px; font-variant-numeric: tabular-nums"
H13="font-size: 13px; font-weight: 500; color: #9198A8"
edit('AdminUsers',[
 ('padding: 22px 16px; display: flex; flex-direction: column; gap: 16px; box-sizing: border-box">','padding: 28px 16px 28px 12px; display: flex; flex-direction: column; gap: 20px; box-sizing: border-box">'),
 ('<button style="height: 42px; padding: 0 14px; border-radius: 12px; border: 1px solid #333846; background: transparent; color: #ECEEF3; font: 500 15px Geist, sans-serif">Import CSV</button>','<button style="height: 40px; padding: 0 16px; border-radius: 12px; border: 1px solid #333846; background: transparent; color: #ECEEF3; font: 500 14px Geist, sans-serif">Import CSV</button>'),
 ('<button style="height: 42px; padding: 0 16px; border-radius: 12px; border: 0; background: {{accent}}; color: #0A0B10; font: 600 15px Geist, sans-serif">Invite people</button>','<button style="height: 40px; padding: 0 18px; border-radius: 12px; border: 0; background: {{accent}}; color: #0A0B10; font: 600 14px Geist, sans-serif">Invite people</button>'),
 ('gap: 14px; padding: 14px 16px; border-radius: 16px; background: #11131A; border: 1px solid #262A35; flex-wrap: wrap">','gap: 16px; padding: 16px 24px; border-radius: 16px; background: #11131A; border: 1px solid #262A35; flex-wrap: wrap">'),
 ("""<span style="font: 500 12px 'Geist Mono', monospace; color: #F5B57A">MIGRATION</span>""","""<span style="font-size: 13px; font-weight: 600; color: #F5B57A">Migration</span>"""),
 ('Importing 1,560 mailboxes from the old mail server','Importing mailboxes from the old mail server'),
 ("""<span style="font: 500 13px 'Geist Mono', monospace; color: #C3C8D4">1,204/1,560 · 2 errors</span>""","""<span style="font-size: 14px; font-variant-numeric: tabular-nums; color: #C3C8D4">1,204 of 1,560 · 2 errors</span>"""),
 ('min-width: 200px; height: 38px; padding: 0 12px; border-radius: 10px;','min-width: 200px; height: 40px; padding: 0 16px; border-radius: 12px;'),
 ('<button style="height: 38px; padding: 0 12px; border-radius: 10px; border: 1px solid #333846; background: transparent; color: #C3C8D4; font: 500 14px Geist, sans-serif">','<button style="height: 40px; padding: 0 16px; border-radius: 12px; border: 1px solid #333846; background: transparent; color: #C3C8D4; font: 500 14px Geist, sans-serif">',2),
 ("""gap: 12px; padding: 10px 16px; border-bottom: 1px solid #1E2129; font: 500 12px 'Geist Mono', monospace; color: #9198A8">
            <span>USER</span><span>ROLE</span><span>STORAGE</span><span>2FA</span><span>LAST ACTIVE</span>""","""gap: 16px; padding: 14px 24px; border-bottom: 1px solid #1E2129; font-size: 13px; font-weight: 500; color: #9198A8">
            <span>User</span><span>Role</span><span>Storage</span><span>2FA</span><span>Last active</span>"""),
 ('gap: 10px; min-width: 0"><span style="width: 32px; height: 32px; flex: none; border-radius: 10px; background: {{u.bg}}; color: #0A0B10; font-size: 12px;','gap: 14px; min-width: 0"><span style="width: 40px; height: 40px; flex: none; border-radius: 13px; background: {{u.bg}}; color: #0A0B10; font-size: 13px;'),
 ('<span style="display: flex; flex-direction: column; min-width: 0"><span style="font-weight: 500">{{u.name}}</span>','<span style="display: flex; flex-direction: column; gap: 2px; min-width: 0"><span style="font-weight: 500">{{u.name}}</span>'),
 ("""<span style="display: flex; flex-direction: column; gap: 4px"><span style="font: 500 12px 'Geist Mono', monospace; color: #9198A8">{{u.used}}</span>""","""<span style="display: flex; flex-direction: column; gap: 6px"><span style="%s; color: #9198A8">{{u.used}}</span>"""%T13),
 ("""<span style="font: 500 13px 'Geist Mono', monospace; color: #9198A8">{{u.last}}</span>""","""<span style="font-size: 14px; color: #9198A8">{{u.last}}</span>"""),
 ("tfaStyle: 'font: 500 12px Geist Mono, monospace; justify-self: start; padding: 3px 8px; border-radius: 7px; '","tfaStyle: 'font-size: 13px; font-weight: 500; justify-self: start; padding: 2px 8px; border-radius: 7px; '"),
 ("gap: 12px; align-items: center; padding: 10px 16px; border-bottom: 1px solid #1A1D25; ' + (sel","gap: 16px; align-items: center; min-height: 64px; box-sizing: border-box; padding: 10px 24px; border-bottom: 1px solid #1A1D25; ' + (sel"),
 ("'Member · starts today'","'Member'"),
 ('max-width: 320px; padding: 22px 16px 22px 0; box-sizing: border-box">','max-width: 336px; padding: 28px 24px 28px 4px; box-sizing: border-box">'),
 ('<div style="padding: 18px; border-radius: 18px; background: #11131A; border: 1px solid #1E2129; display: flex; flex-direction: column; gap: 16px">','<div style="padding: 24px; border-radius: 18px; background: #11131A; border: 1px solid #1E2129; display: flex; flex-direction: column; gap: 24px">'),
 ("""<span style="font: 500 12px 'Geist Mono', monospace; color: #9198A8">ALIASES</span>""",'<span style="%s">Aliases</span>'%H13),
 ("""<span style="font: 500 12px 'Geist Mono', monospace; color: #9198A8">QUOTA · 9.1 OF 10 GB</span>""",'<span style="%s">Quota · 9.1 of 10 GB</span>'%H13),
 ("""<span style="font: 500 12px 'Geist Mono', monospace; color: #9198A8">DEVICES & APPS</span>""",'<span style="%s">Devices and apps</span>'%H13),
 ('<div style="display: flex; flex-direction: column; gap: 8px">','<div style="display: flex; flex-direction: column; gap: 10px">',3),
 ('<button style="height: 26px; padding: 0 8px; border-radius: 7px; border: 1px dashed #333846; background: transparent; color: #9198A8; font: 500 13px Geist, sans-serif">+ alias</button>',''),
 ('          <span style="font-size: 13px; color: #9198A8">Mail 3.8 GB · Drive 5.3 GB</span>\n',''),
 ('<button style="height: 36px; border-radius: 10px; border: 1px solid #333846; background: transparent; color: #ECEEF3; font: 500 14px Geist, sans-serif">Raise to 25 GB</button>','<button style="height: 40px; border-radius: 12px; border: 1px solid #333846; background: transparent; color: #ECEEF3; font: 500 14px Geist, sans-serif">Raise to 25 GB</button>'),
 ('<button style="height: 38px; border-radius: 10px; border: 1px solid #333846; background: transparent; color: #ECEEF3; font: 500 14px Geist, sans-serif">Reset password</button>','<button style="height: 40px; border-radius: 12px; border: 1px solid #333846; background: transparent; color: #ECEEF3; font: 500 14px Geist, sans-serif">Reset password</button>'),
 ('<button style="height: 38px; border-radius: 10px; border: 1px solid rgba(255,122,110,.4);','<button style="height: 40px; border-radius: 12px; border: 1px solid rgba(255,122,110,.4);'),
 ('repeat(2, minmax(0, 1fr)); gap: 8px">\n          <button style="height: 40px; border-radius: 12px; border: 1px solid #333846; background: transparent; color: #ECEEF3; font: 500 14px Geist, sans-serif">Reset password','; gap: 8px; display: flex; flex-direction: column">\n          <button style="height: 40px; border-radius: 12px; border: 1px solid #333846; background: transparent; color: #ECEEF3; font: 500 14px Geist, sans-serif">Reset password'),
])
s=open(P+'AdminUsers.dc.html').read()
a='<div style="display: grid; grid-template-columns: ; gap: 8px; display: flex; flex-direction: column">'
assert s.count(a)==1; s=s.replace(a,'<div style="display: flex; flex-direction: column; gap: 8px">')
open(P+'AdminUsers.dc.html','w').write(s)

edit('AdminSovereignty',[
 ('max-width: 1240px; margin: 0 auto; padding: 24px 16px; box-sizing: border-box; display: flex; flex-direction: column; gap: 18px">','max-width: 1240px; margin: 0 auto; padding: 32px 24px; box-sizing: border-box; display: flex; flex-direction: column; gap: 24px">'),
 ('<button style="height: 42px; padding: 0 16px; border-radius: 12px; border: 1px solid #333846; background: transparent; color: #ECEEF3; font: 500 15px Geist, sans-serif">Export compliance report</button>','<button style="height: 40px; padding: 0 18px; border-radius: 12px; border: 1px solid #333846; background: transparent; color: #ECEEF3; font: 500 14px Geist, sans-serif">Export compliance report</button>'),
 ('repeat(auto-fit, minmax(260px, 1fr)); gap: 12px">','repeat(auto-fit, minmax(260px, 1fr)); gap: 16px">'),
 ('<div style="display: flex; gap: 12px; flex-wrap: wrap">\n      <section aria-labelledby="cls-h"','<div style="display: flex; gap: 16px; flex-wrap: wrap">\n      <section aria-labelledby="cls-h"'),
 ('padding: 16px; border-radius: 18px; background: #11131A; border: 1px solid #1E2129; display: flex; flex-direction: column; gap: 10px">','padding: 24px; border-radius: 18px; background: #11131A; border: 1px solid #1E2129; display: flex; flex-direction: column; gap: 12px">',5),
 ('style="margin: 0; font-size: 15px; font-weight: 600">','style="margin: 0 0 4px; font-size: 16px; font-weight: 600">',5),
 ('gap: 10px; padding: 10px; border-radius: 12px; background: #161922">','gap: 14px; padding: 14px 16px; border-radius: 14px; background: #161922">'),
 ("""<span style="flex: 1; display: flex; flex-direction: column"><span style="font-weight: 500">{{s.n}}</span><span style="font-size: 13px; color: #9198A8">{{s.d}}</span></span>
            <span style="font: 500 12px 'Geist Mono', monospace; color: #9198A8">{{s.r}}</span>""","""<span style="flex: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-weight: 500">{{s.n}}</span><span style="font-size: 13px; color: #9198A8">{{s.d}}</span></span>
            <span style="font-size: 13px; color: #9198A8">{{s.r}}</span>"""),
 ('<span style="font-size: 13px; color: #6FE0D5">No outbound calls to third-party clouds · verified 06:00</span>','<span style="margin-top: 4px; font-size: 13px; color: #6FE0D5">No calls to third-party clouds · verified 06:00</span>'),
 ("""font-size: 14px; min-height: 26px; align-items: center"><span style="color: #C3C8D4">{{k.k}}</span><span style="font: 500 13px 'Geist Mono', monospace">{{k.v}}</span>""","""font-size: 14px; min-height: 36px; align-items: center"><span style="color: #C3C8D4">{{k.k}}</span><span style="font-weight: 500">{{k.v}}</span>"""),
 ('<button style="margin-top: auto; height: 36px; border-radius: 10px; border: 1px solid #333846; background: transparent; color: #ECEEF3; font: 500 14px Geist, sans-serif">Rotate keys (needs 2 of 3 officers)</button>','<button style="margin-top: auto; height: 40px; border-radius: 12px; border: 1px solid #333846; background: transparent; color: #ECEEF3; font: 500 14px Geist, sans-serif">Rotate keys (needs 2 of 3 officers)</button>'),
 ('<span style="font-size: 13px; color: #9198A8">Only these organisations can message, call or share with us.</span>','<span style="font-size: 13px; color: #9198A8">Only these organisations can reach us.</span>'),
 ('gap: 10px; min-height: 28px"><span style="flex: 1; font: 500 13px','gap: 10px; min-height: 36px"><span style="flex: 1; font: 500 13px'),
 ('<button style="margin-top: auto; height: 36px; border-radius: 10px; border: 1px dashed #333846;','<button style="margin-top: auto; height: 40px; border-radius: 12px; border: 1px dashed #333846;'),
 ('grid-template-columns: 170px minmax(0, 1fr); gap: 12px; align-items: center; padding: 8px 10px; border-radius: 12px; background: #161922">','grid-template-columns: 180px minmax(0, 1fr); gap: 16px; align-items: center; min-height: 56px; box-sizing: border-box; padding: 10px 16px; border-radius: 14px; background: #161922">'),
 ('font-size: 14px; min-height: 28px; align-items: center"><span style="color: #C3C8D4">{{r.k}}</span>','font-size: 14px; min-height: 40px; align-items: center"><span style="color: #C3C8D4">{{r.k}}</span>'),
 ('<div style="padding: 10px; border-radius: 12px; background: rgba(245,163,92,.08); border: 1px solid rgba(245,163,92,.3); font-size: 14px; color: #F8C79A">Legal hold active on 3 mailboxes and 1 channel (case 2026-114)</div>','<div style="margin-top: 4px; padding: 14px 16px; border-radius: 14px; background: rgba(245,163,92,.08); border: 1px solid rgba(245,163,92,.3); font-size: 14px; color: #F8C79A">Legal hold active on 3 mailboxes and 1 channel (case 2026-114)</div>'),
 ("""<span style="font: 500 12px 'Geist Mono', monospace; color: #9198A8">AUDIT LOG · 1.2M EVENTS · HASH-CHAINED · LAST CHECK OK</span>""",'<span style="font-size: 13px; color: #9198A8">Audit log · 1.2M events · hash-chained · last check OK</span>'),
 ("r: 'ACTIVE'","r: 'Active'"),("r: 'STANDBY'","r: 'Standby'"),("r: 'AIR-GAPPED'","r: 'Air-gapped'"),
 ("const ok = 'font: 500 12px Geist Mono, monospace; padding: 3px 7px; border-radius: 6px;","const ok = 'font-size: 13px; font-weight: 500; padding: 2px 8px; border-radius: 7px;"),
 ("const ro = 'font: 500 12px Geist Mono, monospace; padding: 3px 7px; border-radius: 6px;","const ro = 'font-size: 13px; font-weight: 500; padding: 2px 8px; border-radius: 7px;"),
 ("l: 'FULL'","l: 'Full'",2),("l: 'MAIL + CHAT'","l: 'Mail + chat'"),("l: 'MAIL ONLY'","l: 'Mail only'"),
 ("{ k: 'Chat & calls', v: 'End-to-end (MLS)' }, { k: 'Last rotation', v: '2026-09-01' }","{ k: 'Chat & calls', v: 'End-to-end (MLS)' }, { k: 'Last rotation', v: '1 Sep 2026' }"),
])
