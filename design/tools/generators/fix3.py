import glob,os
P='/tmp/claude-1002/-home-bohdaq-git/6b5adcb0-31d6-44c8-b201-55c34d7527ea/scratchpad/mailui/project/'
miss=[]
def sub(f,pairs,base=P,ext='.dc.html'):
    s=open(base+f+ext).read()
    for a,b in pairs:
        if a not in s: miss.append((f,a[:45]))
        s=s.replace(a,b)
    open(base+f+ext,'w').write(s)
sub('MobileBooking',[("['MA', 23, '4 free']","['MO', 23, '4 free']")])
sub('WebBooking',[("dow: ['MA', 'TU'","dow: ['MO', 'TU'")])
sub('WebWebinar',[("['AF', '#C6F06B', 'Interpreter'","['SL', '#C6F06B', 'Interpreter'")])
sub('WebSearch',[('aug 3','tue'),('may 6','mon'),('198 KB · Aug 3','198 KB · Tue'),('204 KB · May 6','204 KB · Mon')])
sub('MobileSearch',[('Aug 3','Tue'),('May 6','Mon'),('Jul 1','Sun')])
# story 4 chain
sub('WebSharedMailbox',[('Road damage on Mill Lane after the flood','Flood damage report: car, 14 Mill Lane'),("'M. Peters'","'Maria Peters'"),
 ('Hello, the road on Mill Lane has a large hole since the water went down. A car was damaged yesterday. Who do I contact?','Sent from the “Report flood damage” form. My car was damaged by a hole in the road on Mill Lane after the water went down. Two photos attached.'),
 ('Dear M. Peters, thank you for reporting this. The roads team has scheduled a repair for Thursday…','Dear Ms Peters, thank you for your report. The roads team repairs Mill Lane on Thursday. For your car, please book an assessment visit: cal.ministry.example/assessment'),
 ('m.peters@mail.example','maria.peters@mail.example'),('Citizen ·','Maria Peters ·')])
sub('WebRecords',[('Citizen complaint · road damage','Citizen report · car damage, Mill Lane'),('Reply due in 4 days','Answer due today 16:05')])
sub('WebAppointments',[("{ dow: 'WED', day: '18', who: 'Maria Peters · District 4', what: 'Damage claim advice', time: '11:30' }","{ dow: 'WED', day: '18', who: 'Park Street school · 2 guests', what: 'Damage claim advice', time: '11:30' }"),
 ("{ dow: 'THU', day: '19', who: 'Park Street school · 2 guests', what: 'Assessment visit · approved', time: '10:00' }","{ dow: 'THU', day: '19', who: 'Maria Peters · District 4', what: 'Assessment visit · needs approval', time: '10:00' }")])
# story 3
sub('OSFirstBoot',[('PF3K-0417 · ThinkPad T14 Gen 6','PF3K-1301 · ThinkPad T14 Gen 6')])
# story 2
sub('AdminUsers',[('42 users · 6 groups','1,560 users · 86 groups')])
sub('MobileAdmin',[('42 of 50 seats','1,560 of 1,600 seats')])
for f in ['AdminDomains','AdminUsers','AdminDeliverability']:
    s=open(P+f+'.dc.html').read(); s=s.replace("['Users & groups', '42'","['Users & groups', '1,560'"); open(P+f+'.dc.html','w').write(s)
# story 1
sub('WebNotifications',[('Marek assigned you “Close road R-12”','Marek accepted “Close road R-12”')])
# volunteer Sam -> Noor
sub('WebSpace',[("['SK', '#F5B57A', 'Sam']","['NB', '#F5B57A', 'Noor']"),('lead Sam','lead Noor'),("who: 'Sam'","who: 'Noor'")])
sub('MobileRoom',[("['SK', '#F5B57A', 'Sam', 'MUTED']","['NB', '#F5B57A', 'Noor', 'MUTED']")])
# storyboards: loading + no-access states
s=open('story.py').read()
s=s.replace("TONE={'warn'","TONE={'load':('#0F1117','#333846','#C3C8D4'),'perm':('rgba(245,163,92,.10)','rgba(245,163,92,.4)','#F5B57A'),'warn'")
s=s.replace('{"EMPTY" if tone=="empty" else "ERROR" if tone=="err" else "WARNING" if tone=="warn" else "NOTICE"}','{"EMPTY" if tone=="empty" else "ERROR" if tone=="err" else "WARNING" if tone=="warn" else "LOADING" if tone=="load" else "NO ACCESS" if tone=="perm" else "NOTICE"}')
s=s.replace("('Approvals','err','The eID service isn’t answering','Your signature wasn’t made and nothing was sent.',['Try again','Sign with smart card'])]","('Approvals','err','The eID service isn’t answering','Your signature wasn’t made and nothing was sent.',['Try again','Sign with smart card']),\n   ('Mail','load','Getting your mail…','First sync on this device: 1,240 of 8,300 messages. You can already read the newest.',['Show newest']),\n   ('Drive','perm','You can’t open this file','It’s OFFICIAL-SENSITIVE and shared with named people only. Anna Kowalska owns it.',['Ask Anna for access'])]")
s=s.replace("('Backup','err','Restore test failed','Last night’s test could not read the off-site copy. Live data is fine.',['Run again','Open report'])]","('Backup','err','Restore test failed','Last night’s test could not read the off-site copy. Live data is fine.',['Run again','Open report']),\n   ('Sign-in policy','perm','Only the owner can change this','You’re an admin. Sign-in methods need the Owner role: Taras Bondar.',['Ask the owner'])]")
s=s.replace("('Booking','err','We couldn’t approve this visit','The address is outside the flooded districts. You can still claim by post.',['How to claim'])]","('Booking','err','We couldn’t approve this visit','The address is outside the flooded districts. You can still claim by post.',['How to claim']),\n   ('Form','load','Sending your report…','2 of 3 photos uploaded. Keep this page open; it’s safe to lock your phone.',['Cancel'])]")
open('story.py','w').write(s)
print('missed',miss)
