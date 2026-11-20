# Eight gap boards from the stories (S2.1, S1.8, S3.7, S4.5, S4.8 + phone Docs/Tasks/Records). Drawn in dense2 rules.
import re,sys
sys.path.insert(0,'/tmp/claude-1002/-home-bohdaq-git/6b5adcb0-31d6-44c8-b201-55c34d7527ea/scratchpad/gen')
S='/tmp/claude-1002/-home-bohdaq-git/6b5adcb0-31d6-44c8-b201-55c34d7527ea/scratchpad/'
P=S+'mailui/project/'; BK=S+'backup_pre_dense/'
def rail_of(f,avatar=None):
    s=open(BK+f+'.dc.html').read(); i=s.index('<nav aria-label="Apps"'); j=s.index('</nav>',i)+6; r=s[i:j]
    if avatar: r=re.sub(r'>(OH|TB|SK|KL)</a>','>'+avatar+'</a>',r)
    return r
def page(title,body,w,h):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&family=Source+Serif+4:wght@400;600&display=swap" rel="stylesheet">
<style>/*type2*//*dense2*/
body{{margin:0;background:#0A0B10;color:#ECEEF3;font-family:Geist,system-ui,sans-serif}}
a{{color:#A9B6FF}}a:hover{{color:#C9D1FF}}
</style>
</helmet>
{body}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"accent":{{"editor":"color","default":"#8EA2FF","options":["#8EA2FF","#4FD1C5","#C6F06B","#F5A35C"]}},"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
  renderVals() {{ return {{ accent: this.props.accent ?? '#8EA2FF' }}; }}
}}
</script>
</body>
</html>
'''
def web(rail,inner): return f'<div style="display: flex; flex-wrap: wrap; min-height: 900px; background: #07080C">\n{rail}\n<div style="flex: 999 1 560px; min-width: 0; display: flex; flex-direction: column; min-height: 900px; background: #0A0B10; color: #ECEEF3; font-family: Geist, system-ui, sans-serif; font-size: 15px">{inner}</div>\n</div>'
def phone(inner,bg='#0A0B10'): return f'<div style="width: 390px; height: 844px; position: relative; overflow: hidden; background: {bg}; color: #ECEEF3; font-family: Geist, system-ui, sans-serif; font-size: 16px; display: flex; flex-direction: column">{inner}</div>'
G='#9198A8'
cls=lambda t='OFFICIAL-SENSITIVE': f'<span style="font: 500 12px \'Geist Mono\', monospace; padding: 3px 8px; border-radius: 7px; background: rgba(245,163,92,.15); color: #F5B57A">{t}</span>'
def chip(t,tone='grey'):
    bg,c={'grey':('#1E2230','#C3C8D4'),'ok':('rgba(79,209,197,.14)','#6FE0D5'),'warn':('rgba(245,163,92,.15)','#F5B57A'),'acc':('rgba(142,162,255,.15)','#A9B6FF')}[tone]
    return f'<span style="flex: none; font-size: 13px; font-weight: 500; padding: 2px 8px; border-radius: 7px; background: {bg}; color: {c}">{t}</span>'
def btn(t,p=False,href=None,extra='',h=40):
    st=f'height: {h}px; padding: 0 18px; border-radius: 12px; box-sizing: border-box; display: inline-flex; align-items: center; justify-content: center; text-decoration: none; font: {"600" if p else "500"} 15px Geist, sans-serif; {"border: 0; background: {{accent}}; color: #0A0B10" if p else "border: 1px solid #333846; background: transparent; color: #ECEEF3"}; {extra}'
    return f'<a href="{href}" style="{st}">{t}</a>' if href else f'<button style="{st}">{t}</button>'
def hdr(crumbs,right=''):
    c=f'<span style="color: {G}">/</span>'.join(crumbs)
    return f'<header style="display: flex; align-items: center; gap: 12px; height: 64px; padding: 0 32px; border-bottom: 1px solid #1E2129; box-sizing: border-box">{c}<span style="flex: 1"></span>{right}</header>'
card='padding: 24px; border-radius: 20px; background: #11131A; border: 1px solid #1E2129; box-sizing: border-box'
def av(i,bg,s=40): return f'<span style="width: {s}px; height: {s}px; flex: none; border-radius: {s//3}px; background: {bg}; color: #0A0B10; display: flex; align-items: center; justify-content: center; font-weight: 600; font-size: 13px">{i}</span>'
out={}

# 1 · Admin first run (S2.1)
def step(n,t,m,state,href='#'):
    if state=='done': dot=f'<span style="width: 36px; height: 36px; flex: none; border-radius: 12px; background: rgba(79,209,197,.15); color: #6FE0D5; display: flex; align-items: center; justify-content: center; font-weight: 600">✓</span>'; act=chip('Done','ok')
    elif state=='now': dot=f'<span style="width: 36px; height: 36px; flex: none; border-radius: 12px; background: {{{{accent}}}}; color: #0A0B10; display: flex; align-items: center; justify-content: center; font-weight: 600">{n}</span>'; act=btn('Add domain',True,href)
    else: dot=f'<span style="width: 36px; height: 36px; flex: none; border-radius: 12px; background: #1E2230; color: {G}; display: flex; align-items: center; justify-content: center; font-weight: 600">{n}</span>'; act=f'<a href="{href}" style="font-size: 14px; color: {G}; text-decoration: none">Later</a>'
    bg='background: #161922; box-shadow: inset 0 0 0 1px #333846' if state=='now' else ''
    return f'<div style="display: flex; align-items: center; gap: 16px; min-height: 72px; padding: 0 20px; border-radius: 16px; {bg}">{dot}<span style="flex: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-weight: 600">{t}</span><span style="font-size: 14px; color: {G}">{m}</span></span>{act}</div>'
fact=lambda k,v: f'<div style="display: flex; justify-content: space-between; gap: 12px; min-height: 40px; align-items: center; font-size: 14px"><span style="color: {G}">{k}</span><span style="font-weight: 500; text-align: right">{v}</span></div>'
out['AdminFirstRun']=('Admin first run',1440,900,web(rail_of('AdminUsers','TB'),hdr(['<span style="font-weight: 600">Admin</span>','<span>Set up</span>'],f'<span style="font-size: 14px; color: {G}">Signed in as Taras Bondar · owner</span>')+f'''
  <div style="flex: 1; display: flex; flex-wrap: wrap; gap: 24px; padding: 40px 32px; align-items: flex-start; justify-content: center">
    <section style="flex: 999 1 560px; max-width: 760px; display: flex; flex-direction: column; gap: 24px">
      <div style="display: flex; flex-direction: column; gap: 8px">
        <span style="font-size: 14px; color: {G}">Day 1 · Ministry of [Name]</span>
        <h1 style="margin: 0; font-size: 32px; font-weight: 600; letter-spacing: -.02em">Welcome, Taras. Six steps to go live.</h1>
        <span style="color: #C3C8D4">Do them in order or come back later. Nothing is sent to staff until step 3.</span>
      </div>
      <div style="display: flex; align-items: center; gap: 16px"><span style="flex: 1; height: 8px; border-radius: 4px; background: #1E2230; overflow: hidden"><span style="display: block; width: 16.6%; height: 100%; background: #4FD1C5"></span></span><span style="font-size: 14px; color: {G}">1 of 6 done</span></div>
      <div style="{card}; padding: 12px; display: flex; flex-direction: column; gap: 4px">
        {step(1,'Save the recovery kit','Printed codes and the owner key, kept in the safe.','done')}
        {step(2,'Add your domain','ministry.example. We give you the DNS records and check them.','now','AdminDomains.dc.html')}
        {step(3,'Bring in your people','Connect the HR directory or import a CSV.','todo','AdminUsers.dc.html')}
        {step(4,'Choose how people sign in','Phone, smart card, security key. Passwords can go.','todo','AdminSignIn.dc.html')}
        {step(5,'Decide where data lives','Data centre, keys, partners and retention.','todo','AdminSovereignty.dc.html')}
        {step(6,'Test a restore','Backup is on. Prove that it comes back.','todo','AdminBackup.dc.html')}
      </div>
    </section>
    <aside style="flex: 1 1 300px; max-width: 360px; display: flex; flex-direction: column; gap: 16px">
      <div style="{card}; display: flex; flex-direction: column; gap: 4px">
        <span style="font-weight: 600; margin-bottom: 8px">This installation</span>
        {fact('Runs on','Your servers · 3 nodes')}{fact('Health','<span style="color: #6FE0D5">All healthy</span>')}{fact('Version','Ortus 1.0')}{fact('Outbound calls','None')}
      </div>
      <div style="{card}; display: flex; flex-direction: column; gap: 12px">
        <span style="font-weight: 600">Not alone</span>
        <span style="font-size: 14px; line-height: 1.5; color: #C3C8D4">Add a second owner before you go live, so one lost phone cannot lock the ministry out.</span>
        <div>{btn('Add a second owner')}</div>
      </div>
    </aside>
  </div>'''))

# 2 · Olena's review (S1.8)
route=lambda n,t,m,st: f'<div style="display: flex; align-items: center; gap: 14px; min-height: 60px"><span style="width: 32px; height: 32px; flex: none; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-weight: 600; font-size: 14px; {"background: rgba(79,209,197,.15); color: #6FE0D5" if st=="done" else "background: {{accent}}; color: #0A0B10" if st=="now" else "background: #1E2230; color: #9198A8"}">{"✓" if st=="done" else n}</span><span style="flex: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-weight: {"600" if st=="now" else "500"}">{t}</span><span style="font-size: 14px; color: {G}">{m}</span></span></div>'
chg=lambda who,t: f'<div style="display: flex; gap: 12px; align-items: baseline; font-size: 14px; line-height: 1.5"><span style="flex: none; width: 52px; color: {G}">{who}</span><span style="color: #D6D9E1">{t}</span></div>'
out['WebReview']=('Review before signing',1440,900,web(rail_of('WebApprovals','OH'),hdr(['<a href="WebApprovals.dc.html" style="font-weight: 600; text-decoration: none; color: #ECEEF3">Approvals</a>','<span>Flood response plan 2026 · v12</span>'],cls())+f'''
  <div style="flex: 1; display: flex; flex-wrap: wrap; gap: 24px; padding: 24px 32px; justify-content: center">
    <article style="flex: 999 1 480px; min-width: 0; max-width: 700px; background: #FBFBF9; color: #1B1D22; border-radius: 8px; padding: 48px 56px; box-sizing: border-box; font-family: 'Source Serif 4', Georgia, serif; font-size: 17px; display: flex; flex-direction: column; gap: 16px; line-height: 1.6">
      <h1 style="margin: 0; font-size: 28px">Flood response plan 2026</h1>
      <h2 style="margin: 8px 0 0; font-size: 20px">3. Shelters</h2>
      <p style="margin: 0">Each district opens at least one shelter when the river gauge passes 4.0 m. District 4 uses the <span style="background: #D9F2E6">school on Park Street</span> as the second site.</p>
      <p style="margin: 0"><span style="background: #D9F2E6">Buses leave from the central depot under police escort.</span></p>
      <table style="border-collapse: collapse; font: 15px Geist, sans-serif; margin-top: 8px"><tr style="text-align: left; color: #4B5262"><th style="padding: 10px 12px; border-bottom: 1px solid #D5D8DE; font-weight: 500">District</th><th style="padding: 10px 12px; border-bottom: 1px solid #D5D8DE; font-weight: 500">Shelter</th><th style="padding: 10px 12px; border-bottom: 1px solid #D5D8DE; font-weight: 500">Beds</th></tr><tr><td style="padding: 10px 12px; border-bottom: 1px solid #E6E8EC">3</td><td style="padding: 10px 12px; border-bottom: 1px solid #E6E8EC">Town hall</td><td style="padding: 10px 12px; border-bottom: 1px solid #E6E8EC">140</td></tr><tr><td style="padding: 10px 12px">4</td><td style="padding: 10px 12px">School, Park Street</td><td style="padding: 10px 12px">160</td></tr></table>
      <span style="margin-top: auto; font: 14px Geist, sans-serif; color: #6B7080">Page 6 of 14 · the two marked places changed since you last read it</span>
    </article>
    <aside style="flex: 1 1 340px; max-width: 420px; display: flex; flex-direction: column; gap: 16px">
      <div style="{card}; display: flex; flex-direction: column; gap: 16px; border-color: #333846">
        <div style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 14px; color: {{{{accent}}}}; font-weight: 600">Your turn · step 2 of 4</span><span style="font-size: 20px; font-weight: 600; letter-spacing: -.01em">Marek asks you to check the logistics</span><span style="font-size: 14px; color: {G}">Sent 13:30 · the Director signs after you, by 17:00</span></div>
        <label for="rc" style="position: absolute; left: -9999px">Comment</label>
        <textarea id="rc" placeholder="Comment (optional)" style="height: 72px; padding: 12px 14px; border-radius: 12px; border: 1px solid #333846; background: #0A0B10; color: #ECEEF3; font: 15px Geist, sans-serif; resize: none; box-sizing: border-box"></textarea>
        <div style="display: flex; gap: 8px">{btn('Approve',True,'WebApprovals.dc.html','flex: 1')}{btn('Send back')}</div>
      </div>
      <div style="{card}; display: flex; flex-direction: column; gap: 12px">
        <span style="font-weight: 600">Changed since v10</span>
        {chg('Ana','“sports hall” is now “school on Park Street”')}
        {chg('Marek','Buses now leave from the central depot')}
      </div>
      <div style="{card}; padding: 12px 24px; display: flex; flex-direction: column">
        {route(1,'Author signs','Marek Nowak · 13:30','done')}{route(2,'Logistics review','You · now','now')}{route(3,'Director signs','Katarzyna Lis','next')}{route(4,'File and tell the channel','Automatic','next')}
      </div>
    </aside>
  </div>'''))

# 3 · Read and confirm (S3.7)
pol=lambda n,t,m,st: f'<div style="display: flex; align-items: center; gap: 14px; min-height: 64px; padding: 0 16px; border-radius: 14px; {"background: #161922; box-shadow: inset 0 0 0 1px #333846" if st=="now" else ""}"><span style="width: 32px; height: 32px; flex: none; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-weight: 600; font-size: 14px; {"background: {{accent}}; color: #0A0B10" if st=="now" else "background: #1E2230; color: #9198A8"}">{n}</span><span style="flex: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-weight: {"600" if st=="now" else "500"}">{t}</span><span style="font-size: 14px; color: {G}">{m}</span></span></div>'
out['WebMustRead']=('Read and confirm',1440,900,web(rail_of('WebWelcome','IS'),hdr(['<a href="WebWelcome.dc.html" style="font-weight: 600; text-decoration: none; color: #ECEEF3">Welcome</a>','<span>Read two short policies</span>'],f'<span style="font-size: 14px; color: {G}">Policy 1 of 2</span>')+f'''
  <div style="flex: 1; display: flex; flex-wrap: wrap; gap: 24px; padding: 24px 32px; justify-content: center">
    <article style="flex: 999 1 480px; min-width: 0; max-width: 720px; {card}; padding: 48px 56px; display: flex; flex-direction: column; gap: 16px; font-size: 17px; line-height: 1.65; color: #D6D9E1">
      <span style="font-size: 14px; color: {G}">Handbook · owner: Data protection officer · updated Oct 2026</span>
      <h1 style="margin: 0; font-size: 30px; font-weight: 600; letter-spacing: -.02em; color: #ECEEF3; line-height: 1.2">Data protection policy</h1>
      <p style="margin: 0">Three rules cover most of your day.</p>
      <p style="margin: 0"><strong style="color: #ECEEF3">1. Look at the label.</strong> Every mail, file and channel carries one. It tells you who may see it and whether it may leave the ministry.</p>
      <p style="margin: 0"><strong style="color: #ECEEF3">2. Share from Ortus, not around it.</strong> Send a link instead of an attachment. Do not move work files to private mail or private phones.</p>
      <p style="margin: 0"><strong style="color: #ECEEF3">3. Say it early.</strong> If something went to the wrong person, tell the service desk within the hour. Nobody is punished for reporting.</p>
      <div style="margin-top: auto; display: flex; align-items: center; gap: 16px; padding-top: 24px; border-top: 1px solid #1E2129; flex-wrap: wrap">
        <label style="flex: 1; min-width: 240px; display: flex; align-items: center; gap: 12px; font-size: 15px; color: #ECEEF3"><span aria-hidden="true" style="width: 24px; height: 24px; flex: none; border-radius: 8px; background: {{{{accent}}}}; color: #0A0B10; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 14px">✓</span>I have read and understood this policy</label>
        {btn('Confirm and read the next one',True)}
      </div>
    </article>
    <aside style="flex: 1 1 300px; max-width: 380px; display: flex; flex-direction: column; gap: 16px">
      <div style="{card}; padding: 12px; display: flex; flex-direction: column; gap: 4px">
        {pol(1,'Data protection policy','About 6 minutes · reading now','now')}{pol(2,'Flood response plan 2026','About 4 minutes · summary for new staff','next')}
      </div>
      <div style="{card}; display: flex; flex-direction: column; gap: 10px">
        <span style="font-weight: 600">What confirming means</span>
        <span style="font-size: 14px; line-height: 1.5; color: #C3C8D4">Your name and the time are recorded. Olena and HR can see that you confirmed. You can read it again any time in the handbook.</span>
        <a href="#" style="font-size: 14px">Ask the data protection officer</a>
      </div>
    </aside>
  </div>'''))

# phone pieces
s=open(BK+'MobileChats.dc.html').read(); i=s.index('<nav aria-label="Main"'); NAV=s[i:s.index('</nav>',i)+6]
NAV=NAV.replace('<a href="#" aria-current="page" style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 3px; text-decoration: none; color: {{accent}}; font-size: 12px; font-weight: 600">','<a href="MobileChats.dc.html" style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 3px; text-decoration: none; color: #9198A8; font-size: 12px">')
a='<a href="MobileMore.dc.html" style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 3px; text-decoration: none; color: #9198A8; font-size: 12px">'
assert a in NAV; NAV=NAV.replace(a,'<a href="MobileMore.dc.html" aria-current="page" style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 3px; text-decoration: none; color: {{accent}}; font-size: 12px; font-weight: 600">')
BACK='<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="m15 18-6-6 6-6"/></svg>'
def mhead(t,sub='',back='MobileMore.dc.html',right=''):
    subh=f'<span style="font-size: 13px; color: {G}">{sub}</span>' if sub else ''
    return f'<header style="display: flex; align-items: center; gap: 4px; padding: 12px 8px; border-bottom: 1px solid #1E2129"><a href="{back}" aria-label="Back" style="width: 44px; height: 44px; flex: none; display: flex; align-items: center; justify-content: center; color: #ECEEF3">{BACK}</a><span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px"><span style="font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{t}</span>{subh}</span>{right}</header>'
mcard='padding: 16px; border-radius: 18px; background: #11131A; border: 1px solid #1E2129'
def mbtn(t,p=False,href='#',extra=''): return f'<a href="{href}" style="height: 48px; border-radius: 14px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; text-decoration: none; font: {"600" if p else "500"} 15px Geist, sans-serif; {"background: {{accent}}; color: #0A0B10" if p else "border: 1px solid #333846; color: #ECEEF3"}; {extra}">{t}</a>'

# 4 · Citizen reads the answer (S4.5)
tl=lambda t,m,st: f'<div style="display: flex; gap: 12px; align-items: center; min-height: 52px"><span style="width: 10px; height: 10px; flex: none; border-radius: 50%; {"background: #4FD1C5" if st else "border: 2px solid #333846; box-sizing: border-box"}"></span><span style="flex: 1; font-weight: 500">{t}</span><span style="font-size: 14px; color: {G}">{m}</span></div>'
out['MobileCitizenAnswer']=('Citizen answer',390,844,phone(f'''
  <header style="display: flex; align-items: center; gap: 10px; padding: 16px"><span style="width: 36px; height: 36px; flex: none; border-radius: 10px; background: #1E2230; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 600; color: #C3C8D4">GOV</span><span style="flex: 1; display: flex; flex-direction: column"><span style="font-weight: 600">Ministry of [Name]</span><span style="font-size: 13px; color: #6FE0D5">Verified sender</span></span></header>
  <div style="flex: 1; padding: 8px 16px 0; display: flex; flex-direction: column; gap: 16px">
    <div style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: 14px; color: {G}">Your case <span style="font-family: 'Geist Mono', monospace; color: #C3C8D4">2026/CI/1302</span></span><h1 style="margin: 0; font-size: 26px; font-weight: 600; letter-spacing: -.02em; line-height: 1.2">We answered your report</h1></div>
    <div style="{mcard}; display: flex; flex-direction: column; gap: 12px">
      <span style="font-size: 14px; color: {G}">Citizen Services · today 08:14</span>
      <span style="line-height: 1.55; color: #D6D9E1">Dear Ms Peters, thank you for your report. The roads team repairs Mill Lane on Thursday. For your car, please book an assessment visit.</span>
    </div>
    {mbtn('Book an assessment visit',True,'MobileBooking.dc.html')}
    {mbtn('Write back')}
    <div style="{mcard}; padding: 8px 16px; display: flex; flex-direction: column">
      {tl('Report received','08:05',True)}{tl('Answered','08:14',True)}{tl('Assessment visit','Not booked',False)}
    </div>
  </div>
  <span style="padding: 16px; font-size: 13px; color: {G}; text-align: center">No account needed. This page opens only from the link in your email.</span>''','#0A0B10'))

# 5 · Phone doc (V1)
out['MobileDoc']=('Mobile document',390,844,phone(mhead('Flood response plan 2026','v12 · saved','MobileDrive.dc.html')+f'''
  <div style="flex: 1; overflow: hidden; padding: 16px; display: flex; flex-direction: column; gap: 16px">
    <div style="display: flex; align-items: center; gap: 10px">{cls()}<span style="font-size: 14px; color: {G}">Marek and Ana are here</span></div>
    <article style="background: #FBFBF9; color: #1B1D22; border-radius: 8px; padding: 24px 22px; font-family: 'Source Serif 4', Georgia, serif; font-size: 17px; line-height: 1.6; display: flex; flex-direction: column; gap: 12px">
      <h1 style="margin: 0; font-size: 22px">3. Shelters</h1>
      <p style="margin: 0">Each district opens at least one shelter when the river gauge passes <span style="background: #FFF1C9">4.0 m</span>. District 4 uses the <span style="text-decoration: line-through; color: #A0463E">sports hall</span> <span style="background: #D9F2E6">school on Park Street</span> as the second site.</p>
      <p style="margin: 0">Buses leave from the central depot under police escort.</p>
    </article>
    <div style="{mcard}; display: flex; flex-direction: column; gap: 12px">
      <div style="display: flex; align-items: center; gap: 12px">{av('AF','#C6F06B')}<span style="flex: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-weight: 600">Ana suggests a change</span><span style="font-size: 14px; color: {G}">“sports hall” → “school on Park Street”</span></span></div>
      <div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 8px">{mbtn('Accept',True)}{mbtn('Reject')}</div>
    </div>
    <a href="#" style="display: flex; align-items: center; gap: 12px; min-height: 64px; padding: 0 16px; border-radius: 18px; border: 1px solid #1E2129; text-decoration: none; color: #ECEEF3">{av('MN','#A9B6FF')}<span style="flex: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-weight: 500">Marek on “4.0 m”</span><span style="font-size: 14px; color: {G}">Hydrology says 3.8 m is safer</span></span><span style="font-size: 14px; color: {G}">1 reply</span></a>
  </div>
  <div style="padding: 12px 16px 28px; border-top: 1px solid #1E2129; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px">{mbtn('Comment')}{mbtn('Suggest')}{mbtn('Share',False,'MobileShare.dc.html')}</div>'''))

# 6 · Phone tasks (V1)
def task(t,m,due,tone='grey',who=None):
    w=av(*who,s=32) if who else '<span aria-hidden="true" style="width: 24px; height: 24px; margin: 0 4px; flex: none; border-radius: 8px; border: 2px solid #333846; box-sizing: border-box"></span>'
    return f'<a href="#" style="display: flex; align-items: center; gap: 12px; min-height: 68px; padding: 0 12px; border-radius: 16px; text-decoration: none; color: #ECEEF3">{w}<span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px"><span style="font-weight: 500; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{t}</span><span style="font-size: 14px; color: {G}">{m}</span></span>{chip(due,tone)}</a>'
tab=lambda t,on=False,href='#': f'<a href="{href}" style="height: 36px; padding: 0 14px; border-radius: 12px; display: flex; align-items: center; text-decoration: none; font: {"600" if on else "500"} 14px Geist, sans-serif; {"background: #ECEEF3; color: #0A0B10" if on else "border: 1px solid #262A35; color: #C3C8D4"}">{t}</a>'
sec=lambda t: f'<span style="font-size: 13px; font-weight: 500; color: {G}; padding: 16px 12px 4px">{t}</span>'
out['MobileTasks']=('Mobile tasks',390,844,phone(f'''
  <header style="padding: 18px 16px 12px; display: flex; flex-direction: column; gap: 16px">
    <div style="display: flex; align-items: center; gap: 10px"><h1 style="margin: 0; flex: 1; font-size: 30px; font-weight: 600; letter-spacing: -.03em">For you</h1><a href="#" aria-label="New task" style="width: 44px; height: 44px; border-radius: 14px; background: {{{{accent}}}}; color: #0A0B10; display: flex; align-items: center; justify-content: center; text-decoration: none; font-size: 24px">+</a></div>
    <div style="display: flex; gap: 6px">{tab('Approvals 2',False,'MobileApprovals.dc.html')}{tab('Tasks 6',True)}{tab('Forms 1')}</div>
  </header>
  <div style="flex: 1; overflow: hidden; padding: 0 8px; display: flex; flex-direction: column">
    {sec('Due today')}
    {task('Open school shelter on Park Street','Flood response · 3 of 5 steps','Today','warn')}
    {task('Update public info page','From chat · #flood-response','Today','warn')}
    {sec('This week')}
    {task('Book 6 buses for evacuation','Flood response','Fri')}
    {task('Check sandbag stock in depot 2','Flood response · 0 of 3 steps','Mon')}
    {sec('You asked others')}
    {task('Close road R-12 and divert traffic','Marek · 2 of 4 steps','Today','warn',('MN','#A9B6FF'))}
    {task('Hydrology: confirm 3.8 m threshold','Anna · 1 day late','Late','warn',('AK','#F5B57A'))}
  </div>
  {NAV}'''))

# 7 · Phone case file (V2)
rec=lambda ref,t,m,st,tone: f'<a href="#" style="display: flex; align-items: center; gap: 12px; min-height: 68px; padding: 0 12px; border-radius: 16px; text-decoration: none; color: #ECEEF3"><span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px"><span style="font-weight: 500; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">{t}</span><span style="font-size: 14px; color: {G}"><span style="font-family: \'Geist Mono\', monospace; font-size: 13px">{ref}</span> · {m}</span></span>{chip(st,tone)}</a>'
out['MobileRecords']=('Mobile case file',390,844,phone(mhead('Flood response 2026','<span style="font-family: \'Geist Mono\', monospace">2026/EM/0114</span> · owner Marek')+f'''
  <div style="flex: 1; overflow: hidden; padding: 16px 8px 0; display: flex; flex-direction: column">
    <div style="margin: 0 8px; {mcard}; display: flex; flex-direction: column; gap: 12px">
      <div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap">{cls()}{chip('Open','acc')}{chip('Legal hold','warn')}</div>
      <span style="font-size: 14px; line-height: 1.5; color: #C3C8D4">41 records · kept 10 years, then sent to the national archive.</span>
    </div>
    {sec('Latest records')}
    {rec('0114-033','Flood response plan 2026 · signed','today 16:21','Record','ok')}
    {rec('0114-032','Decision: close road R-12','chat · 10:47','Record','ok')}
    {rec('0114-031','Gauge report','mail · 10:42','Record','ok')}
    {rec('0114-030','Shelter capacity sheet','Drive · 09:15','Working','grey')}
    <a href="MobileShare.dc.html" style="margin: 12px 8px 0; height: 48px; border-radius: 14px; border: 1px dashed #333846; display: flex; align-items: center; justify-content: center; text-decoration: none; color: #ECEEF3; font-weight: 500">File something to this case</a>
  </div>
  {NAV}'''))

# 8 · Town hall, guest on a phone (Later, S4.8)
q=lambda v,t,m,mine=False: f'<div style="display: flex; align-items: center; gap: 12px; min-height: 68px; padding: 0 12px; border-radius: 16px; {"background: #161922; box-shadow: inset 0 0 0 1px #333846" if mine else ""}"><span style="width: 48px; height: 44px; flex: none; border-radius: 12px; background: #1E2230; display: flex; flex-direction: column; align-items: center; justify-content: center; font-size: 13px; font-weight: 600; line-height: 1.2"><span style="color: {G}">▲</span>{v}</span><span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px"><span style="font-weight: 500">{t}</span><span style="font-size: 14px; color: {"#6FE0D5" if mine else G}">{m}</span></span></div>'
out['MobileTownHall']=('Mobile town hall guest',390,844,phone(f'''
  <div style="position: relative; height: 260px; flex: none; background: radial-gradient(300px 200px at 50% 45%, #232838 0%, #0D0F15 75%); display: flex; align-items: center; justify-content: center">
    <span style="width: 88px; height: 88px; border-radius: 28px; background: #DDE3F8; color: #0A0B10; display: flex; align-items: center; justify-content: center; font-size: 26px; font-weight: 700; box-shadow: 0 0 0 3px {{{{accent}}}}">KL</span>
    <span style="position: absolute; left: 16px; top: 16px; display: flex; align-items: center; gap: 8px; height: 30px; padding: 0 12px; border-radius: 10px; background: rgba(7,8,12,.7); font-size: 13px; font-weight: 600"><span style="width: 8px; height: 8px; border-radius: 50%; background: #FF7A6E"></span>Live · 412 watching</span>
    <span style="position: absolute; left: 16px; right: 16px; bottom: 14px; padding: 10px 14px; border-radius: 12px; background: rgba(7,8,12,.78); font-size: 15px; line-height: 1.4">Katarzyna Lis: “…the roads team repairs Mill Lane on Thursday.”</span>
  </div>
  <div style="padding: 16px 16px 4px; display: flex; flex-direction: column; gap: 4px"><h1 style="margin: 0; font-size: 20px; font-weight: 600; letter-spacing: -.01em">Town hall: flood response</h1><span style="font-size: 14px; color: {G}">You joined as a guest · captions on · you are muted</span></div>
  <div style="flex: 1; overflow: hidden; padding: 0 8px; display: flex; flex-direction: column">
    {sec('Questions')}
    {q(128,'When will Mill Lane be repaired?','Your question · answered live',True)}
    {q(96,'Will there be compensation for damaged cars?','District 2')}
    {q(41,'How can volunteers sign up?','Guest')}
  </div>
  <div style="padding: 12px 16px 28px; border-top: 1px solid #1E2129; display: flex; align-items: center; gap: 8px">
    <label for="tq" style="position: absolute; left: -9999px">Ask a question</label>
    <input id="tq" placeholder="Ask a question" style="flex: 1; min-width: 0; height: 48px; padding: 0 16px; border-radius: 14px; border: 1px solid #333846; background: #13151C; color: #ECEEF3; font: 15px Geist, sans-serif; box-sizing: border-box">
    <a href="#" style="height: 48px; padding: 0 18px; border-radius: 14px; background: {{{{accent}}}}; color: #0A0B10; display: flex; align-items: center; font-weight: 600; text-decoration: none">Ask</a>
  </div>'''))

for n,(t,w,h,body) in out.items(): open(P+n+'.dc.html','w').write(page(t,body,w,h))
print(list(out))
