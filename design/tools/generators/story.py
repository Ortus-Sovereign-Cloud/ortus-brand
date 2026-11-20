import json
P='/tmp/claude-1002/-home-bohdaq-git/6b5adcb0-31d6-44c8-b201-55c34d7527ea/scratchpad/mailui/project/'
BLOB={'s1':'/_blob/67b5a4943bbbbd98553c88464cb64cf2','s2':'/_blob/4a0e27976e77f6821e8fd42b131ca10c','s3':'/_blob/569169c1c9bdc949c0cd57644ea4127d','s4':'/_blob/174bb87784e043b52ac6a5f3070efcd3'}
MARK='<svg style="flex: none" width="40" height="40" viewBox="0 0 48 48" aria-hidden="true"><path d="M22 30 L4 30 A18 18 0 0 1 22 12 Z" fill="{{accent}}"/><path d="M26 30 L26 12 A18 18 0 0 1 44 30 Z" fill="#6E86FF"/><rect x="4" y="34" width="40" height="5" rx="2.5" fill="#4FD1C5"/></svg>'
REL={'V1':('rgba(79,209,197,.16)','#6FE0D5'),'V2':('rgba(142,162,255,.16)','#A9B6FF'),'Later':('#1E2230','#C3C8D4')}
ST={'New':('rgba(198,240,107,.16)','#D4F28F'),'Missing':('rgba(255,122,110,.16)','#FF9A92')}
mono="font: 500 14px 'Geist Mono', monospace"
def pill(t,bg,c): return f'<span style="{mono}; padding: 4px 10px; border-radius: 8px; background: {bg}; color: {c}">{t}</span>'
STORIES=[
 dict(k='s1',file='Story1',n='Story 1',title='A civil servant’s crisis day',who=('OH','#A9B6FF','Olena Hrytsenko','Head of Logistics'),goal='From a locked laptop to a signed, filed flood plan in one working day, without leaving Ortus.',
  steps=[('S1.1','09:02','Olena','Scans the code on her workstation, picks the matching number, confirms with her face.','WorkstationLogin','V2',''),
   ('S1.2','09:05','Olena','Reads the catch-up card: two mails need a reply, one invite, one alert.','Main','V1',''),
   ('S1.3','10:41','Olena','Gets the gauge alert and opens the channel it came from.','WebNotifications','V1',''),
   ('S1.4','10:47','Olena, Marek, Anna, Jonas','Agree in a thread to close road R-12. The decision is recorded.','WebChat','V1',''),
   ('S1.5','10:50','Olena','Turns the decision into a task for Marek with a due time.','WebTasks','V1',''),
   ('S1.6','11:10','The response team','Join the channel call and fill in the shelter sheet together.','WebCall','V1',''),
   ('S1.7','12:30','Marek, Ana, Olena','Edit the flood plan. Ana suggests a change and Marek accepts it.','WebDocEditor','V1',''),
   ('S1.8','13:30','Marek, then Olena','Marek sends the plan for approval. Olena reviews it by 14:05.','WebReview','V1','New'),
   ('S1.9','16:20','Katarzyna','Signs with her eID on her phone.','MobileApprovals','V1',''),
   ('S1.10','16:21','Ortus','Files the signed PDF to the case and tells the channel.','WebRecordFiled','V1','New'),
   ('S1.11','18:00','Ana, Katarzyna','Run the public town hall.','WebWebinar','Later','')],
  states=[('Sign-in','warn','This code has expired','Codes last 60 seconds. A new one is on the screen now.',['Scan again']),
   ('Sign-in','err','That number didn’t match','The request is blocked and security has been told.',['Try again in 30 s','Call the help desk']),
   ('Mail','info','You’re offline','Showing mail from 10:42. What you send will go out when you’re back online.',['Retry now']),
   ('Chat','err','Not sent','“Agreed. Closing R-12 at 11:30” could not be sent.',['Send again','Delete']),
   ('Docs','info','Marek is editing section 3','You can suggest changes. He’ll see them when he finishes.',['Suggest instead']),
   ('Approvals','err','The eID service isn’t answering','Your signature wasn’t made and nothing was sent.',['Try again','Sign with smart card']),
   ('Mail','load','Getting your mail…','First sync on this device: 1,240 of 8,300 messages. You can already read the newest.',['Show newest']),
   ('Drive','perm','You can’t open this file','It’s OFFICIAL-SENSITIVE and shared with named people only. Anna Kowalska owns it.',['Ask Anna for access'])]),
 dict(k='s2',file='Story2',n='Story 2',title='An IT admin sets up the organisation',who=('TB','#6FE0D5','Taras Bondar','IT administrator'),goal='From an empty install to 1,560 people on managed devices, with mail that other providers accept.',
  steps=[('S2.1','Day 1','Taras','Opens the admin console for the first time and follows the setup checklist.','AdminFirstRun','V1','New'),
   ('S2.2','Day 1','Taras','Adds ministry.example, copies the DNS records, waits for the checks to turn green.','AdminDomains','V1',''),
   ('S2.3','Day 2','Taras','Connects the HR directory and imports users and groups.','AdminUsers','V1',''),
   ('S2.4','Day 2–5','Taras','Imports mailboxes from the old server and fixes two failures from his phone.','MobileAdmin','V1',''),
   ('S2.5','Day 6','Taras','Turns on phone sign-in, smart card and security key. Turns passwords off.','AdminSignIn','V1',''),
   ('S2.6','Day 7','Taras','Writes the laptop policy: updates, USB, screen lock, allowed apps.','AdminPolicy','V2','New'),
   ('S2.7','Day 8','Taras','Enrols laptops and phones and sees the first compliance report.','AdminDevices','V2',''),
   ('S2.8','Day 9','Taras','Sets data location, keys, federation partners and retention.','AdminSovereignty','V1',''),
   ('S2.9','Day 23','Taras','After two clean weeks, switches DMARC to quarantine.','AdminDeliverability','V1',''),
   ('S2.10','Day 24','Taras','Runs a restore test and connects the case-management system.','AdminBackup','V1','')],
  states=[('Domains','info','We can’t see this record yet','DNS changes can take up to an hour. We check every 10 minutes.',['Check now']),
   ('Users','warn','Import paused','The old server is refusing connections. 1,204 of 1,560 done; nothing is lost.',['Resume','See details']),
   ('Sign-in policy','warn','3 people would be locked out','They have no phone, card or key enrolled. Passwords stay on until they do.',['Show the 3','Remind them']),
   ('Devices','warn','Not seen for 30 days','LT-0902 · pool laptop. Its access is already blocked.',['Lock','Mark as retired']),
   ('Backup','err','Restore test failed','Last night’s test could not read the off-site copy. Live data is fine.',['Run again','Open report']),
   ('Sign-in policy','perm','Only the owner can change this','You’re an admin. Sign-in methods need the Owner role: Taras Bondar.',['Ask the owner'])]),
 dict(k='s3',file='Story3',n='Story 3',title='A new employee’s first day',who=('IS','#F5B57A','Iryna Savchenko','Analyst, Logistics'),goal='From a sealed laptop to her first team message in 15 minutes, with no call to the help desk.',
  steps=[('S3.1','Day before','Taras','Invites Iryna and assigns her a laptop.','AdminUsers','V1',''),
   ('S3.2','08:45','Iryna','Installs the Ortus app on her work phone and makes it her key.','MobileWelcome','V1','New'),
   ('S3.3–4','09:00','Iryna','Turns on the laptop, picks her language, scans the enrolment code with her phone.','OSFirstBoot','V2',''),
   ('S3.5','09:08','Iryna','Signs in with the QR code for the first time.','WorkstationLogin','V2',''),
   ('S3.6','09:10','Iryna','Lands on a welcome page: her people and three things to do today.','WebWelcome','V1','New'),
   ('S3.7','09:20','Iryna','Reads and confirms the two must-read policies.','WebMustRead','V1','New'),
   ('S3.8','09:35','Iryna','Says hello in her team channel and accepts her first meeting.','WebChat','V1',''),
   ('S3.9','10:00','Iryna','Installs an approved app from the software centre.','OSStore','V2','')],
  states=[('Phone','warn','That code doesn’t match','Check your welcome letter. 2 tries left, then IT sends a new code.',['Try again']),
   ('Laptop','info','No network yet','Connect to Wi-Fi or plug in a cable. Setup continues by itself.',['Choose a network']),
   ('Laptop','err','This laptop is assigned to someone else','PF3K-0417 belongs to Olena Hrytsenko. IT can reassign it.',['Call the help desk']),
   ('Mail','empty','No mail yet','Your address is iryna@ministry.example. Messages to you will appear here.',['Write a message']),
   ('Drive','empty','Your drive is empty','Files you upload, files shared with you and attachments will appear here.',['Upload a file'])]),
 dict(k='s4',file='Story4',n='Story 4',title='A citizen contacts the government',who=('MP','#C6F06B','Maria Peters','Resident, District 4'),goal='Reports flood damage from her phone, without an account, and gets a human answer and a visit date the same day.',
  steps=[('S4.1','Before','Sam','Builds the “Report flood damage” form and what happens when it’s sent.','WebForms','V2',''),
   ('S4.2','08:05','Maria','Opens the form link on her phone, adds her address and two photos.','MobileCitizenForm','V2','New'),
   ('S4.3','08:06','Maria','Gets a receipt with a case number and what happens next.','MobileCitizenReceipt','V2','New'),
   ('S4.4','08:06','Ortus','Opens a case and puts the report in the support@ queue.','WebRecords','V2',''),
   ('S4.5','08:14','Sam','Takes the report, reads Olena’s internal note, answers from a template.','WebSharedMailbox','V2',''),
   ('S4.5b','08:20','Maria','Reads the answer on her phone and taps the booking link.','MobileCitizenAnswer','V2','New'),
   ('S4.6','08:30','Maria','Books a damage assessment visit.','MobileBooking','V2',''),
   ('S4.7','08:40','Sam','Approves the visit. It appears in the team calendar.','WebAppointments','V2',''),
   ('S4.8','18:00','Maria','Joins the town hall as a guest and asks about Mill Lane.','MobileTownHall','Later','New')],
  states=[('Form','warn','That photo is larger than 20 MB','We can shrink it for you; the detail stays good enough to assess.',['Shrink and add','Choose another']),
   ('Form','info','This form is closed','Reports for the November flood closed on 30 Nov. For new damage call [NUMBER].',['Other services']),
   ('Shared mailbox','info','Sam is already answering this','Opened 2 minutes ago. You can read it but not reply.',['Ask Sam','Take over']),
   ('Booking','info','No free times this week','The next free visit is Mon 23 Nov at 10:00.',['Take Mon 10:00','Tell me if earlier opens']),
   ('Booking','err','We couldn’t approve this visit','The address is outside the flooded districts. You can still claim by post.',['How to claim']),
   ('Form','load','Sending your report…','2 of 3 photos uploaded. Keep this page open; it’s safe to lock your phone.',['Cancel'])]),
]
TONE={'load':('#0F1117','#333846','#C3C8D4'),'perm':('rgba(245,163,92,.10)','rgba(245,163,92,.4)','#F5B57A'),'warn':('rgba(245,163,92,.10)','rgba(245,163,92,.4)','#F5B57A'),'err':('rgba(255,122,110,.10)','rgba(255,122,110,.4)','#FF9A92'),'info':('rgba(142,162,255,.08)','rgba(142,162,255,.35)','#A9B6FF'),'empty':('#0F1117','#333846','#C3C8D4')}
CW,CH,GAP,PAD=440,275,40,60
meta={}
for S in STORIES:
    n=len(S['steps']); W=PAD*2+n*CW+(n-1)*GAP; H=960
    cols=''
    for i,(sid,when,who,cap,board,rel,status) in enumerate(S['steps']):
        if board:
            thumb=f'<a href="{board}.dc.html" aria-label="Open {board}" style="display: block; width: {CW}px; height: {CH}px; border-radius: 16px; overflow: hidden; border: 1px solid #2A2E3A; background: #0D0F15"><img src="{BLOB[S["k"]]}" alt="" style="display: block; height: {CH}px; max-width: none; margin-left: -{i*CW}px"></a>'
        else:
            thumb=f'<div style="width: {CW}px; height: {CH}px; box-sizing: border-box; border-radius: 16px; border: 2px dashed #FF7A6E; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 8px; color: #FF9A92"><span style="font-size: 20px; font-weight: 600">Not designed yet</span><span style="font-size: 16px; color: #C3C8D4">First-run admin with a setup checklist</span></div>'
        arrow=f'<span aria-hidden="true" style="position: absolute; left: {CW+6}px; top: {58+CH//2-14}px; width: {GAP-12}px; text-align: center; font-size: 26px; color: #8A91A1">→</span>' if i<n-1 else ''
        tags=pill(rel,*REL[rel])+(pill(status.upper(),*ST[status]) if status else '')
        cols+=f'''<div style="position: relative; width: {CW}px; flex: none; display: flex; flex-direction: column; gap: 12px">
      <div style="display: flex; align-items: baseline; gap: 10px; height: 34px"><span style="font: 600 22px Geist, sans-serif; color: {{{{accent}}}}">{sid}</span><span style="{mono}; color: #C3C8D4">{when}</span><span style="flex: 1"></span><span style="font-size: 16px; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 250px">{who}</span></div>
      {thumb}{arrow}
      <span style="font-size: 18px; line-height: 1.45; color: #ECEEF3; min-height: 78px">{cap}</span>
      <div style="display: flex; gap: 8px">{tags}</div>
    </div>'''
    cards=''
    for where,tone,t,body,acts in S['states']:
        bg,bd,fg=TONE[tone]
        btns=''.join(f'<span style="height: 38px; padding: 0 14px; border-radius: 10px; display: flex; align-items: center; font-size: 15px; font-weight: {600 if j==0 else 500}; {"background: {{accent}}; color: #0A0B10" if j==0 else "border: 1px solid #333846; color: #ECEEF3"}">{a}</span>' for j,a in enumerate(acts))
        cards+=f'''<div style="width: {CW}px; flex: none; box-sizing: border-box; padding: 18px; border-radius: 18px; background: {bg}; border: 1px {"dashed" if tone=="empty" else "solid"} {bd}; display: flex; flex-direction: column; gap: 10px">
      <span style="{mono}; color: {fg}">{where.upper()} · {"EMPTY" if tone=="empty" else "ERROR" if tone=="err" else "WARNING" if tone=="warn" else "LOADING" if tone=="load" else "NO ACCESS" if tone=="perm" else "NOTICE"}</span>
      <span style="font-size: 20px; font-weight: 600; line-height: 1.25">{t}</span>
      <span style="font-size: 16px; line-height: 1.45; color: #C3C8D4; min-height: 46px">{body}</span>
      <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-top: auto">{btns}</div>
    </div>'''
    i,bg,name,role=S['who']
    body=f'''<div style="width: {W}px; height: {H}px; box-sizing: border-box; padding: 48px {PAD}px; background: #07080C; color: #ECEEF3; font-family: Geist, system-ui, sans-serif; display: flex; flex-direction: column; gap: 30px">
  <div style="display: flex; align-items: center; gap: 22px">
    {MARK}
    <div style="display: flex; flex-direction: column; gap: 4px"><span style="{mono}; color: #A4ABBA; letter-spacing: .08em">{S["n"].upper()} · WEDNESDAY 18 NOVEMBER 2026 · MINISTRY OF [NAME]</span><h1 style="margin: 0; font: 700 44px Unbounded, Geist, sans-serif; letter-spacing: -.02em">{S["title"]}</h1></div>
    <span style="width: 1px; height: 64px; background: #262A35; margin: 0 8px"></span>
    <span style="width: 56px; height: 56px; flex: none; border-radius: 18px; background: {bg}; color: #0A0B10; font-weight: 700; font-size: 18px; display: flex; align-items: center; justify-content: center">{i}</span>
    <div style="display: flex; flex-direction: column; gap: 2px; max-width: 720px"><span style="font-size: 20px; font-weight: 600">{name} · <span style="font-weight: 400; color: #C3C8D4">{role}</span></span><span style="font-size: 18px; color: #C3C8D4; line-height: 1.4">{S["goal"]}</span></div>
    <span style="flex: 1"></span>
    <div style="display: flex; gap: 8px; align-items: center">{pill("V1",*REL["V1"])}{pill("V2",*REL["V2"])}{pill("LATER",*REL["Later"])}{pill("NEW",*ST["New"])}</div>
  </div>
  <div style="display: flex; gap: {GAP}px">{cols}</div>
  <div style="display: flex; flex-direction: column; gap: 14px">
    <span style="{mono}; color: #A4ABBA; letter-spacing: .08em">WHAT CAN GO WRONG · STATES TO BUILD FOR THIS STORY</span>
    <div style="display: flex; gap: {GAP}px">{cards}</div>
  </div>
</div>'''
    html=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{S["n"]}: {S["title"]}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@700&family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
body{{margin:0}}
</style>
</helmet>
{body}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"accent":{{"editor":"color","default":"#8EA2FF","options":["#8EA2FF","#4FD1C5","#C6F06B","#F5A35C"]}},"$preview":{{"width":{W},"height":{H}}}}}'>
class Component extends DCLogic {{
  renderVals() {{ return {{ accent: this.props.accent ?? '#8EA2FF' }}; }}
}}
</script>
</body>
</html>
'''
    open(P+S['file']+'.dc.html','w').write(html); meta[S['file']]=(W,H,S['n']+' · '+S['title'])
c=json.load(open(P+'canvas.json'))
y=0
for f,(W,H,t) in meta.items():
    c['boards'][f+'.dc.html']={"x":0,"y":y,"w":W,"h":H,"title":t,"page":"stories"}
    if f+'.dc.html' not in c['order']: c['order'].append(f+'.dc.html')
    y+=H+160
c['notes']['storiesDoc']={"kind":"link","x":0,"y":y-40,"href":"https://claude.ai/artifact/PsucNKvE4zc5xnQg5gT98W","title":"Ortus user stories","linkKind":"doc","page":"stories"}
c['notes']['storiesHow']={"x":5500,"y":0,"w":460,"size":"m","fill":"blue","page":"stories","text":"How to read the stories\n• One person, one goal, one day; steps left to right\n• Click a thumbnail in Play to open the real screen\n• Tags: V1 / V2 / Later = proposed release; NEW = drawn for this story\n• Bottom row = error, warning and empty states each story needs\n• Acceptance criteria live in the “Ortus user stories” doc (card below the last story)"}
c['launch']={"view":"canvas","page":"stories"}
json.dump(c,open(P+'canvas.json','w'),ensure_ascii=False)
print(meta)
