import json,re
P='/tmp/claude-1002/-home-bohdaq-git/6b5adcb0-31d6-44c8-b201-55c34d7527ea/scratchpad/mailui/project/'
c=json.load(open(P+'canvas.json'))
V1='Main WebSearch WebCompose WebCalendar WebDrive WebFilePreview WebDocEditor WebChat WebContacts WebNotifications WebPersonal AppSwitcher WebWelcome MobileInbox MobileThread MobileSearch MobileCalendar MobileDrive MobileShare MobileChats MobileChannel MobileNotifications MobileMore MobileWelcome MobileAdmin AdminDomains AdminUsers AdminDeliverability AdminSovereignty AdminSignIn AdminBackup WebTasks WebCall WebApprovals MobileApprovals WebRecordFiled AdminFirstRun WebReview WebMustRead MobileDoc MobileTasks'.split()
LATER='WebSpace WebDiscover MobileRoom WebWebinar WebIntranet MobileTownHall'.split()
SKIP=('Brand','Story')
HEIGHTS={'AdminDomains':999,'AdminSignIn':999,'WebDiscover':949,'WebSearch':900}
nb={'WebRecordFiled':(4560,11940,1440,900,'Web · Record signed and filed',True),'AdminPolicy':(6080,18640,1440,900,'Admin · Device policy',True),
    'WebWelcome':(0,22660,1440,900,'Web · Welcome (first run, empty states)',True),'MobileWelcome':(1520,22660,390,844,'Mobile · Welcome and phone enrolment',False),
    'AdminFirstRun':(0,24000,1440,900,'Admin · First run (setup checklist)',True),'WebReview':(1520,24000,1440,900,'Web · Review before signing',True),'WebMustRead':(3040,24000,1440,900,'Web · Read and confirm',True),
    'MobileDoc':(4560,24000,390,844,'Mobile · Document',False),'MobileTasks':(5030,24000,390,844,'Mobile · Tasks',False),'MobileRecords':(5500,24000,390,844,'Mobile · Case file',False),
    'MobileCitizenAnswer':(5970,24000,390,844,'Mobile · Citizen reads the answer (public)',False),'MobileTownHall':(6440,24000,390,844,'Mobile · Town hall as a guest (public)',False),
    'MobileCitizenForm':(1990,22660,390,844,'Mobile · Citizen form (public)',False),'MobileCitizenReceipt':(2460,22660,390,844,'Mobile · Citizen receipt',False)}
for n,(x,y,w,h,t,fill) in nb.items():
    b={"x":x,"y":y,"w":w,"h":h,"title":t}
    if fill: b['expand']='fill'
    c['boards'][n+'.dc.html']=b
    if n+'.dc.html' not in c['order']: c['order'].append(n+'.dc.html')
c['notes']['osUx']['x']=7600
c['notes']['newRow']={"x":0,"y":22360,"text":"New from the stories · first day & citizen","kind":"title1","maxW":2850}
c['notes']['gapRow']={"x":0,"y":23700,"text":"Gaps closed · 19 Nov","kind":"title1","maxW":2850}
for f,h in HEIGHTS.items(): c['boards'][f+'.dc.html']['h']=h
for f,b in c['boards'].items():
    n=f[:-8]
    if n.startswith(SKIP): continue
    t=re.sub(r'^(V1|V2|Later) · ','',b.get('title',n))
    tag='V1' if n in V1 else 'Later' if n in LATER else 'V2'
    b['title']=f'{tag} · {t}'
c['pages']=[{"id":"screens","name":"Screens"},{"id":"stories","name":"Stories"}]
json.dump(c,open(P+'canvas.json','w'),ensure_ascii=False)
from collections import Counter
print(Counter(b['title'].split(' · ')[0] for f,b in c['boards'].items() if not f.startswith(SKIP)))
