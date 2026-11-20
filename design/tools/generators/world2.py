import glob,re,os
P='/tmp/claude-1002/-home-bohdaq-git/6b5adcb0-31d6-44c8-b201-55c34d7527ea/scratchpad/mailui/project/'
H=os.path.dirname(os.path.abspath(__file__))+'/'
miss=[]
def sub(f,pairs,base=P,ext='.dc.html'):
    p=base+f+ext; s=open(p).read()
    for a,b in pairs:
        if a not in s: miss.append((f,a[:50]))
        s=s.replace(a,b)
    open(p,'w').write(s)
ROSTER_WEB=('<span style="color: #ECEEF3; font-weight: 600">Sandbag shifts · District 4 · Wed 18 Nov</span>'
 '<span>12:00 – 15:00 &#160; Mill Lane &#160;&#160;&#160;&#160;&#160; crew A · 8 people · lead Lena</span>'
 '<span style="background: rgba(142,162,255,.12); margin: 0 -20px; padding: 0 20px">15:00 – 18:00 &#160; Park Street &#160;&#160; crew B · 6 people · 2 more needed</span>'
 '<span>18:00 – 21:00 &#160; Depot 2 &#160;&#160;&#160;&#160;&#160;&#160; crew C · 5 people · lead Sam</span>'
 '<span style="color: #6E7585">Pick-up: depot 2, gate B. Bring gloves and boots.</span>')
ROSTER_MOB=('<span style="color: #ECEEF3; font-weight: 600">Sandbag shifts · District 4</span>'
 '<span>12–15 &#160; Mill Lane &#160;&#160; crew A · 8</span>'
 '<span style="background: rgba(142,162,255,.12)">15–18 &#160; Park Street &#160; crew B · 2 more needed</span>'
 '<span>18–21 &#160; Depot 2 &#160;&#160;&#160; crew C · 5</span>')
def block(f,start,end,new):
    p=P+f+'.dc.html'; s=open(p).read()
    i=s.find(start)
    if i<0: miss.append((f,start[:40])); return
    i+=len(start); j=s.index(end,i); open(p,'w').write(s[:i]+new+s[j:])
block('WebSpace',"<div style=\"padding: 18px 20px; font: 13px/1.8 'Geist Mono', monospace; color: #C3C8D4; display: flex; flex-direction: column\">",'</div>',ROSTER_WEB)
block('MobileRoom',"font: 11px/1.8 'Geist Mono', monospace; color: #C3C8D4; display: flex; flex-direction: column\">",'<span style="position: absolute; left: 10px; bottom: 10px',ROSTER_MOB+'\n    ')
sub('WebSpace',[('src/smtp/queue.rs','sandbag-shifts.xlsx'),('what happens if all MX hosts time out?','where do we pick up sandbags for Mill Lane?'),('it goes back to the queue with backoff, 5 min → 4 h','depot 2, gate B. Bring gloves.'),('dropping the diagram here','dropping the map here'),('queue-diagram.png','district-4-map.png'),("['showcase', 0]","['shifts', 0]")])
sub('MobileRoom',[('what happens if all MX hosts time out?','where do we pick up sandbags for Mill Lane?')])
sub('WebDiscover',[('Ask a tax advisor','Ask about damage claims')])
sub('WebAppointments',[('People book you from a link. Slots come from your calendar’s free/busy; confirmations go out from your own mail domain.','Residents book a time from a public link. Slots come from the team’s calendars; confirmations go out from the ministry’s own mail domain.'),
 ("name: 'Intro call', slug: '30min'","name: 'Damage claim advice', slug: 'advice'"),('A quick first conversation. Video link added automatically.','Fifteen minutes with an adviser about a flood damage claim.'),("['30 min', 'video', 'no approval']","['15 min', 'video or phone', 'no approval']"),
 ("name: 'Migration consult', slug: 'migration'","name: 'Damage assessment visit', slug: 'assessment'"),('Moving mailboxes from another provider. Asks for domain and mailbox count.','An assessor visits the property. Asks for the address and what was damaged.'),
 ("what: 'Intro call'","what: 'Damage claim advice'"),('Fabrikam · 2 guests','Park Street school · 2 guests'),('Migration consult · approved','Assessment visit · approved'),('Litware · Mia Chen','R. Novak · District 2'),('Request from Tailspin','Request from L. Ortiz'),('Migration consult · needs approval','Assessment visit · needs approval'),
 ('>YO</a>','>SK</a>')])
sub('WebBooking',[('>YO<','>M<'),('[Your name] · [Company]','Ministry of [Name] · Citizen services'),('>Intro call<','>Damage claim advice<'),('30 minutes','15 minutes'),('A first conversation about moving your team’s mail. Bring your domain and rough mailbox count.','Talk to an adviser about a flood damage claim. Have your address and photos ready.'),('mia@litware.example','maria.peters@mail.example')])
sub('MobileBooking',[('>YO<','>M<'),('[Your name] · [Company]','Ministry of [Name] · Citizen services'),('Migration consult','Damage assessment visit'),('How many mailboxes?','What was damaged?'),('about 40','Car and garage'),('Mia Chen','Maria Peters'),('mia@litware.example','maria.peters@mail.example'),('>VIDEO<','>AT YOUR ADDRESS<')])
sub('WebChat',[("['OH', '#A9B6FF', 'Olena H.', '', true]","['AF', '#C6F06B', 'Ana Ferreira', '', true]")])
sub('WebDocEditor',[('<strong style="color: #ECEEF3">Olena</strong> suggested','<strong style="color: #ECEEF3">Ana</strong> suggested'),('justify-content: center">OH</span></span>','justify-content: center">AF</span></span>')])
sub('MobileNotifications',[('Olena suggested an edit in Flood plan','Ana suggested an edit in Flood plan'),('Sign: Flood response plan v12','Review: Flood response plan v12')])
sub('WebNotifications',[('Olena suggested an edit in Flood plan','Ana suggested an edit in Flood plan'),('Sign: Flood response plan v12','Review: Flood response plan v12'),('Approval · due 17:00','Approval · due 14:00')])
sub('MobileMore',[('Sign the flood plan by 17:00','Review the flood plan by 14:00')])
sub('WebCall',[("['OH', '#A9B6FF', 'Olena', false, true]","['AF', '#C6F06B', 'Ana', false, true]"),('Open school shelter — Olena, 18:00','Open school shelter — you, 18:00')])
sub('WebSharedMailbox',[("'YO', '#DDE3F8', true, true]","'§', '#DDE3F8', true, true]"),("'SAM', 'DUE IN 5 h', 'SK', '#DDE3F8'","'OLENA', 'DUE IN 5 h', 'OH', '#A9B6FF'"),("'§'","'SK'"),('Sam is viewing this too','Ana is viewing this too'),('Sam Kim covers my mail and approvals','Olena Hrytsenko covers my mail and approvals'),('Meeting invites go to Sam','Meeting invites go to Olena'),('SLA 8 h','TARGET 8 h'),('>YO</a>','>SK</a>')])
sub('WebApprovals',[("['Marek Nowak', 'Head of Operations', 'Signed 18 Nov 08:12', true]","['Marek Nowak', 'Head of Operations', 'Signed 18 Nov 13:30', true]"),("['Legal Department', 'Reviewer', 'Approved 18 Nov 08:40', true]","['Olena Hrytsenko', 'Logistics review', 'Approved 18 Nov 14:05', true]"),("m: 'Marek Nowak · 08:12'","m: 'Marek Nowak · 13:30'"),("t: 'Legal review', m: 'Any of 3 lawyers · approved 08:40'","t: 'Logistics review', m: 'Olena Hrytsenko · approved 14:05'"),('>YO</a>','>KL</a>'),('<span>Flood response plan 2026 · v12</span>','<span>Flood response plan 2026 · v12 · Director’s view</span>')])
sub('MobileApprovals',[('From Marek · Legal approved 08:40 · you are step 3 of 3','From Marek · Olena approved 14:05 · you are step 3 of 3')])
sub('AdminUsers',[("['YO', '#DDE3F8', 'You', 'admin@ministry.example', 'Owner'","['TB', '#DDE3F8', 'Taras Bondar (you)', 'taras@ministry.example', 'Owner'"),("['JW', '#F5B57A', 'Jonas Weber', 'jonas@ministry.example', 'Member · importing'","['IS', '#F5B57A', 'Iryna Savchenko', 'iryna@ministry.example', 'Member · starts today'")])
sub('AdminDevices',[('WS-0291 · Jonas Weber','WS-0291 · Sam Kim'),("'Dell Latitude 7450', 'Jonas Weber'","'Dell Latitude 7450', 'Sam Kim'"),("'ThinkPad T14', 'S. Kim'","'ThinkPad T14', 'Pool laptop'")])
sub('AdminSignIn',[("who: 'Jonas Weber'","who: 'Sam Kim'"),('Help desk for S. Kim','Help desk for Iryna Savchenko')])
sub('WebDrive',[('font-weight: 500">Clients</a>','font-weight: 500">Emergency</a>'),('<span>Regional office</span>','<span>Shelters</span>'),("['DIR', 'Contracts'","['DIR', 'Agreements'"),("['DIR', 'Invoices'","['DIR', 'Gauge reports'")])
sub('MobileDrive',[("['DIR', 'Clients'","['DIR', 'Emergency'")])
sub('AdminBackup',[('“Contracts”','“Agreements”')])
sub('os2',[("('Contracts','Mon','—',0),('Invoices','Today','—',0)","('Agreements','Mon','—',0),('Gauge reports','Today','—',0)")],H,'.py')
sub('os',[('Sign: Flood response plan v12','Review: Flood response plan v12'),('Due 17:00 · tap to sign with your phone','Due 14:00 · open in Ortus Docs'),('Sign flood plan by 17:00','Review flood plan by 14:00'),('Sign the plan','Review the plan')],H,'.py')
# avatars: admin boards = Taras, everything else = Olena
for p in sorted(glob.glob(P+'*.dc.html')):
    n=os.path.basename(p); s=open(p).read(); o=s
    who='TB' if n.startswith('Admin') else 'OH'
    s=s.replace('>YO</a>','>'+who+'</a>').replace('>YO</button>','>'+who+'</button>').replace('>YO</div>','>'+who+'</div>').replace('>YO</span>','>'+who+'</span>').replace("'YO'","'"+who+"'")
    if s!=o: open(p,'w').write(s)
print('missed:',miss)
