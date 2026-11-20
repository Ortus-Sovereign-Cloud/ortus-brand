import re,sys
P='/tmp/claude-1002/-home-bohdaq-git/6b5adcb0-31d6-44c8-b201-55c34d7527ea/scratchpad/mailui/project/'
KEEP_MONO=('from:daniel','larger:10M','dmarc report','drive.ministry.example','OFFICIAL-SENSITIVE')
def generic(s):
    out=[]
    for ln in s.split('\n'):
        if 'gap: 3px; text-decoration: none' in ln or any(k in ln for k in KEEP_MONO):
            out.append(ln); continue
        ln=re.sub(r"font: (\d00) 1[123]px '?Geist Mono'?, monospace", lambda m:f"font: {m.group(1)} 13px Geist, sans-serif; font-variant-numeric: tabular-nums", ln)
        ln=re.sub(r"; letter-spacing: \.06em","",ln)
        ln=ln.replace('font-size: 12px','font-size: 13px').replace('font: 500 12px Geist, sans-serif','font: 500 13px Geist, sans-serif').replace('font: 12px Geist, sans-serif','font: 13px Geist, sans-serif')
        out.append(ln)
    return '\n'.join(out)
def edit(name,reps):
    s=open(P+name+'.dc.html').read()
    if '/*dense2*/' in s: print('skip',name); return
    s=generic(s)
    for a,b,*n in reps:
        n=n[0] if n else 1
        assert s.count(a)==n,(name,a[:70],s.count(a))
        s=s.replace(a,b)
    s=s.replace('/*type2*/','/*type2*//*dense2*/') if '/*type2*/' in s else s.replace('<style>','<style>/*dense2*/',1); assert '/*dense2*/' in s
    open(P+name+'.dc.html','w').write(s)
SNIP='''          <span style="font-size: 13px; color: #9198A8; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">'''
edit('MobileInbox',[
 ('NEXT · IN 22 MIN','Next · in 22 min'),
 (SNIP+'Invite: Thu 14:00 · 2 files</span>\n',''),
 (SNIP+'{{m.snippet}}</span>\n',''),
 ('display: flex; gap: 12px; padding: 12px; text-decoration: none; color: #ECEEF3; background: #11131A; transform','display: flex; align-items: center; gap: 12px; padding: 14px 12px; text-decoration: none; color: #ECEEF3; background: #11131A; transform'),
 ('style="display: flex; gap: 12px; padding: 12px; border-radius: 16px; text-decoration: none; color: #ECEEF3">','style="display: flex; align-items: center; gap: 12px; padding: 14px 12px; border-radius: 16px; text-decoration: none; color: #ECEEF3">'),
 ('flex-direction: column; gap: 2px">\n          <div style="display: flex; gap: 8px">','flex-direction: column; gap: 4px">\n          <div style="display: flex; gap: 8px">',2),
 ('height: 34px; padding: 0 14px; border-radius: 12px','height: 36px; padding: 0 14px; border-radius: 12px',3),
 ('padding: 0 8px; gap: 2px">','padding: 0 8px; gap: 4px">'),
])
edit('MobileThread',[
 ('">TL;DR </span>','; font-weight: 600">Summary · </span>'),
 ('">MON</span>','">Mon</span>'),('font-weight: 600">THU</span>','font-weight: 600">Thu</span>'),
 ('font-weight: 600; padding: 2px 7px; border-radius: 6px','font-weight: 500; padding: 2px 8px; border-radius: 7px'),
 ('padding: 10px 12px; border-radius: 12px; background: #161922','padding: 12px 14px; border-radius: 14px; background: #161922'),
 ('height: 34px; padding: 0 12px; border-radius: 12px; border: 1px solid #333846','height: 40px; padding: 0 14px; border-radius: 12px; border: 1px solid #333846',2),
])
edit('MobileSearch',[
 ('">TOP HIT<','">Top hit<'),('">FILES<','">Files<'),('">MESSAGES · 6 MORE<','">Messages · 6 more<'),('">RECENT<','">Recent<'),
 ('''        <span style="font-size: 13px; color: #9198A8">…today’s <mark>gauge</mark> report and…</span>\n''',''),
 ('flex-direction: column; gap: 3px; padding: 10px 12px; border-radius: 14px','flex-direction: column; gap: 4px; padding: 12px; border-radius: 14px'),
 ("font: 500 12px 'Geist Mono', monospace; display: flex; align-items: center\">","font: 500 13px 'Geist Mono', monospace; display: flex; align-items: center\">",3),
 ('padding: 0 12px 12px; overflow: hidden','padding: 0 16px 12px; overflow: hidden'),('padding: 14px 12px 10px;','padding: 14px 16px 10px;'),
 ('<div style="flex: 1; overflow: hidden; padding: 0 12px;','<div style="flex: 1; overflow: hidden; padding: 0 16px;'),
 ("const on = 'height: 34px","const on = 'height: 36px"),("const off = 'height: 34px","const off = 'height: 36px"),
])
edit('MobileCalendar',[
 ('">NOVEMBER 2026<','">November 2026<'),
 ("[['MA', 16, 3], ['TU', 17, 3], ['WE', 18, 3], ['TH', 19, 4], ['FR', 20, 2], ['SA', 21, 0], ['SU', 22, 0]]","[['Mon', 16, 3], ['Tue', 17, 3], ['Wed', 18, 3], ['Thu', 19, 4], ['Fri', 20, 2], ['Sat', 21, 0], ['Sun', 22, 0]]"),
 ('''          <span style="{{e.kindStyle}}">{{e.kind}}</span>\n''',''),
 ("padding: 12px 14px; border-radius: 16px; background: ' + bg","padding: 14px 16px; border-radius: 16px; background: ' + bg"),
 ("flex-direction: column; gap: 3px',","flex-direction: column; gap: 4px',"),
 ('width: 46px; padding-top: 12px;','width: 46px; padding-top: 14px;'),
 ('flex-direction: column; gap: 8px">\n','flex-direction: column; gap: 12px">\n'),
 ('height: 34px; padding: 0 14px; border-radius: 10px; background: {{accent}}','height: 36px; padding: 0 14px; border-radius: 10px; background: {{accent}}'),
 ('height: 34px; padding: 0 12px; border-radius: 10px; border: 1px solid #333846','height: 36px; padding: 0 12px; border-radius: 10px; border: 1px solid #333846'),
])
edit('MobileDrive',[
 ('">WI-FI<','">Wi-Fi<'),('">RECENT<','">Recent<'),('">MY DRIVE<','">My Drive<'),('">OFFLINE<','">Offline<'),
 ('gap: 12px; padding: 6px 0; text-decoration: none','gap: 12px; padding: 10px 0; text-decoration: none'),
 ('flex-direction: column"><span style="font-weight: 500; white-space','flex-direction: column; gap: 2px"><span style="font-weight: 500; white-space'),
])
edit('MobileShare',[('">VIEW ONLY · 30 DAYS<','">View only · 30 days<'),('padding: 12px; border-radius: 16px; background: #0A0B10','padding: 16px; border-radius: 16px; background: #0A0B10')])
edit('MobileChats',[
 ('padding: 2px 5px; border-radius: 5px; background: rgba(245,163,92,.15); color: #F5B57A">EXT<','padding: 1px 7px; border-radius: 7px; background: rgba(245,163,92,.15); color: #F5B57A">External<'),
 ('style="display: flex; gap: 12px; padding: 10px 12px; border-radius: 16px;','style="display: flex; align-items: center; gap: 12px; padding: 12px; border-radius: 16px;'),
 ('flex-direction: column; gap: 2px">\n          <span style="display: flex; gap: 6px; align-items: center">','flex-direction: column; gap: 4px">\n          <span style="display: flex; gap: 6px; align-items: center">'),
 ('height: 34px; padding: 0 14px; border-radius: 12px','height: 36px; padding: 0 14px; border-radius: 12px',3),
 ("nameStyle: 'white-space","nameStyle: 'min-width: 0; white-space"),
])
edit('MobileChannel',[
 ('''<span style="font: 500 12px 'Geist Mono', monospace; color: #F5B57A">OFFICIAL-SENSITIVE · 3 ORGS · E2EE</span>''','''<span style="font-size: 13px; color: #9198A8"><span style="font: 500 12px 'Geist Mono', monospace; color: #F5B57A">OFFICIAL-SENSITIVE</span> · 3 orgs · encrypted</span>'''),
 ('padding: 14px 12px; display: flex; flex-direction: column; gap: 14px','padding: 16px; display: flex; flex-direction: column; gap: 16px'),
 ('padding: 12px; border-radius: 16px; background: #13151C','padding: 16px; border-radius: 16px; background: #13151C'),
 ('flex-direction: column; gap: 8px">\n      <span style="font-weight: 600">Open','flex-direction: column; gap: 12px">\n      <span style="font-weight: 600">Open'),
 ('<div style="padding: 10px 12px 22px;','<div style="padding: 10px 16px 22px;'),
])
edit('MobileNotifications',[
 ('style="display: flex; gap: 12px; padding: 12px; border-radius: 16px;','style="display: flex; align-items: center; gap: 12px; padding: 12px; border-radius: 16px;'),
 ('flex-direction: column; gap: 2px"><span style="font-weight: 500; line-height: 1.35">','flex-direction: column; gap: 3px"><span style="font-weight: 500; line-height: 1.35">'),
 ('padding: 0 8px; display: flex; flex-direction: column; gap: 2px','padding: 0 8px; display: flex; flex-direction: column; gap: 4px'),
])
edit('MobileMore',[])
edit('MobileWelcome',[])
edit('MobileAdmin',[
 ('">MINISTRY OF [NAME]<','">Ministry of [Name]<'),('">NEEDS YOU<','">Needs you<'),('">DMARC · MINISTRY.EXAMPLE<','">DMARC · ministry.example<'),
 ('">MIGRATION · OLD MAIL SERVER<','">Migration · old mail server<'),('">QUICK ACTIONS<','">Quick actions<'),
 ('flex-direction: column; gap: 8px; padding: 14px; border-radius: 16px','flex-direction: column; gap: 10px; padding: 16px; border-radius: 16px',2),
 ('flex-direction: column; gap: 4px; padding: 14px; border-radius: 16px','flex-direction: column; gap: 4px; padding: 14px 16px; border-radius: 16px'),
])
edit('MobileApprovals',[
 ('">SIGN · DUE TODAY<','">Sign · due today<'),('">APPROVE · PURCHASE REQUEST<','">Approve · purchase request<'),('">TASKS DUE TODAY<','">Tasks due today<'),
 ('padding: 14px; border-radius: 18px; background: #11131A; border: 1px solid #262A35; display: flex; flex-direction: column; gap: 10px','padding: 16px; border-radius: 18px; background: #11131A; border: 1px solid #262A35; display: flex; flex-direction: column; gap: 12px',2),
 ('<button style="height: 44px; border-radius: 12px; border: 0; background: {{accent}}; color: #0A0B10; font: 600 14px Geist, sans-serif">Approve</button>','<button style="height: 44px; border-radius: 12px; border: 1px solid #333846; background: transparent; color: #ECEEF3; font: 600 14px Geist, sans-serif">Approve</button>'),
 ('gap: 12px; padding: 10px 12px; border-radius: 14px; background: #11131A','gap: 12px; padding: 12px 16px; border-radius: 14px; background: #11131A'),
 ('flex-direction: column"><span style="font-weight: 500">{{t.t}}','flex-direction: column; gap: 2px"><span style="font-weight: 500">{{t.t}}'),
 ('height: 34px; padding: 0 14px; border-radius: 12px','height: 36px; padding: 0 14px; border-radius: 12px',3),
])
