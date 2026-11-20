import re,json
P='/tmp/claude-1002/-home-bohdaq-git/6b5adcb0-31d6-44c8-b201-55c34d7527ea/scratchpad/mailui/project/'
def rail_of(f,avatar=None,deactivate=False):
    s=open(P+f+'.dc.html').read(); i=s.index('<nav aria-label="Apps"'); j=s.index('</nav>',i)+6; r=s[i:j]
    if deactivate: r=r.replace(' aria-current="page"','').replace('background: #1E2230; color: {{accent}}; font-weight: 600','color: #9198A8')
    if avatar: r=re.sub(r'>(OH|TB|SK|KL)</a>','>'+avatar+'</a>',r)
    return r
MARK='<path d="M22 30 L4 30 A18 18 0 0 1 22 12 Z" fill="{a}"/><path d="M26 30 L26 12 A18 18 0 0 1 44 30 Z" fill="{b}"/><rect x="4" y="34" width="40" height="5" rx="2.5" fill="{c}"/>'
def mark(s,a='{{accent}}',b='#6E86FF',c='#4FD1C5'): return f'<svg style="flex: none" width="{s}" height="{s}" viewBox="0 0 48 48" aria-hidden="true">'+MARK.format(a=a,b=b,c=c)+'</svg>'
def page(title,body,w,h,body_bg='#0A0B10'):
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
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&family=Source+Serif+4:wght@400;600&display=swap" rel="stylesheet">
<style>
body{{margin:0;background:{body_bg};color:#ECEEF3;font-family:Geist,system-ui,sans-serif}}
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
mono="font: 500 12px 'Geist Mono', monospace"
def pill(t,bg,c): return f'<span style="{mono}; padding: 3px 8px; border-radius: 7px; background: {bg}; color: {c}">{t}</span>'
def sw(on): return f'<span aria-hidden="true" style="width: 42px; height: 24px; flex: none; border-radius: 12px; position: relative; background: {"{{accent}}" if on else "#333846"}"><span style="position: absolute; top: 3px; left: {"21px" if on else "3px"}; width: 18px; height: 18px; border-radius: 50%; background: #0A0B10"></span></span>'
btn=lambda t,p=False,extra='': f'<button style="height: 44px; padding: 0 18px; border-radius: 12px; font: {"600" if p else "500"} 15px Geist, sans-serif; {"border: 0; background: {{accent}}; color: #0A0B10" if p else "border: 1px solid #333846; background: transparent; color: #ECEEF3"}; {extra}">{t}</button>'

# 1. Record signed and filed
sig=lambda n,r,t: f'<div style="display: flex; flex-direction: column; gap: 4px; padding: 10px; border-radius: 6px; border: 1px solid #9FD8C9; background: #EEF8F5"><span style="font-weight: 600">{n}</span><span style="color: #4B5262">{r}</span><span style="font-weight: 600; color: #1F7A4D">{t}</span></div>'
fact=lambda k,v,c='#ECEEF3': f'<div style="display: flex; justify-content: space-between; gap: 12px; min-height: 30px; align-items: center"><span style="color: #A4ABBA">{k}</span><span style="font-weight: 500; text-align: right; color: {c}">{v}</span></div>'
rec=web(rail_of('WebRecords'),f'''
  <header style="display: flex; align-items: center; gap: 12px; padding: 14px 20px; border-bottom: 1px solid #1E2129; flex-wrap: wrap">
    <a href="WebRecords.dc.html" style="font-weight: 600; text-decoration: none; color: #ECEEF3">Records</a><span style="color: #8A91A1">/</span><span>Case 2026/EM/0114</span><span style="color: #8A91A1">/</span><span style="font-weight: 600">Record 0114-033</span>
    <span style="flex: 1"></span>{pill("OFFICIAL-SENSITIVE","rgba(245,163,92,.15)","#F5B57A")}
  </header>
  <div style="display: flex; align-items: center; gap: 14px; margin: 18px 20px 0; padding: 16px 18px; border-radius: 16px; background: rgba(79,209,197,.1); border: 1px solid rgba(79,209,197,.35)">
    <span style="width: 44px; height: 44px; flex: none; border-radius: 14px; background: rgba(79,209,197,.2); color: #6FE0D5; display: flex; align-items: center; justify-content: center; font-size: 22px">✓</span>
    <span style="flex: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-size: 18px; font-weight: 600">Signed by all three and filed at 16:21</span><span style="color: #C3C8D4">Flood response plan 2026 · v12 is now the official record. #flood-response has been told.</span></span>
  </div>
  <div style="flex: 1; display: flex; flex-wrap: wrap; gap: 20px; padding: 20px">
    <article style="flex: 999 1 480px; min-width: 0; max-width: 680px; background: #FBFBF9; color: #1B1D22; border-radius: 6px; padding: 44px 52px; box-sizing: border-box; font-family: 'Source Serif 4', Georgia, serif; display: flex; flex-direction: column; gap: 12px; line-height: 1.6; position: relative">
      <span style="position: absolute; right: 24px; top: 24px; font: 600 11px Geist, sans-serif; padding: 4px 10px; border-radius: 6px; border: 2px solid #1F7A4D; color: #1F7A4D; transform: rotate(4deg)">SIGNED · SEALED · PDF/A</span>
      <h1 style="margin: 0; font-size: 26px">Flood response plan 2026</h1>
      <p style="margin: 0">Approved for use by all districts from 18 November 2026, 16:20.</p>
      <p style="margin: 0; color: #4B5262">… 14 pages …</p>
      <div style="margin-top: 20px; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px; font: 13px Geist, sans-serif">{sig("Marek Nowak","Head of Operations","Signed 13:30")}{sig("Olena Hrytsenko","Logistics review","Approved 14:05")}{sig("Katarzyna Lis","Director","Signed 16:20 · eID")}</div>
    </article>
    <aside aria-label="Record details" style="flex: 1 1 320px; max-width: 380px; display: flex; flex-direction: column; gap: 14px">
      <section style="padding: 18px; border-radius: 18px; background: #11131A; border: 1px solid #1E2129; display: flex; flex-direction: column; gap: 4px">
        <h2 style="margin: 0 0 8px; font-size: 17px; font-weight: 600">Record</h2>
        {fact("Reference","0114-033")}{fact("Type","Decision document")}{fact("Signatures","3 of 3 valid","#6FE0D5")}{fact("Trusted timestamp","18 Nov 2026 16:20:41")}{fact("Keep","10 years, then national archive")}{fact("Fingerprint","9f2c…e41a")}
      </section>
      <section style="padding: 18px; border-radius: 18px; background: #11131A; border: 1px solid #1E2129; display: flex; flex-direction: column; gap: 10px">
        <h2 style="margin: 0; font-size: 17px; font-weight: 600">What happened next</h2>
        <span style="color: #C3C8D4">16:21 · Posted to #flood-response</span><span style="color: #C3C8D4">16:21 · Published on the intranet as must-read</span><span style="color: #C3C8D4">16:22 · Sent to 3 federated organisations</span>
      </section>
      <div style="display: flex; flex-direction: column; gap: 8px">{btn("Download signed PDF",True)}{btn("Verify signatures")}</div>
      <span style="font-size: 13px; color: #A4ABBA; line-height: 1.5">This record can’t be edited or deleted. To change the plan, start version 13; it goes through approval again.</span>
    </aside>
  </div>''')
open(P+'WebRecordFiled.dc.html','w').write(page('Record signed and filed',rec,1440,900,'#07080C'))

# 2. Device policy editor
def prow(a,b,ctrl): return f'<div style="display: flex; align-items: center; gap: 14px; padding: 12px 16px; border-top: 1px solid #1A1D25"><span style="flex: 1; display: flex; flex-direction: column; gap: 2px"><span style="font-weight: 500">{a}</span><span style="font-size: 13px; color: #A4ABBA">{b}</span></span>{ctrl}</div>'
val=lambda t: f'<span style="{mono}; padding: 5px 10px; border-radius: 8px; background: #1E2230">{t} ▾</span>'
def pgroup(t,rows): return f'<section style="border-radius: 16px; background: #11131A; border: 1px solid #1E2129"><h2 style="margin: 0; padding: 14px 16px; font-size: 16px; font-weight: 600">{t}</h2>{rows}</section>'
pol_list=''.join(f'<a href="#" style="display: flex; flex-direction: column; gap: 2px; padding: 10px 12px; border-radius: 12px; text-decoration: none; color: #ECEEF3; {"background: #1E2230; box-shadow: inset 2px 0 0 {{accent}}" if s else ""}"><span style="font-weight: {600 if s else 500}">{n}</span><span style="font-size: 13px; color: #A4ABBA">{m}</span></a>' for n,m,s in [('Office laptops','v7 live · v8 draft · 1,402 devices',1),('Lobby kiosks','v3 · 4 devices',0),('Field tablets','v2 · 38 devices',0),('Work phones','v5 · 1,402 devices',0),('Guest Wi-Fi laptops','v1 · 12 devices',0)])
pol=web(rail_of('AdminDomains'),f'''
  <header style="display: flex; align-items: center; gap: 12px; padding: 14px 20px; border-bottom: 1px solid #1E2129; flex-wrap: wrap">
    <span style="font-weight: 600">Admin</span>{pill("DEVICES","#1E2230","#C3C8D4")}<a href="AdminDevices.dc.html" style="text-decoration: none">Devices</a><span style="font-weight: 600">Policies</span>
    <span style="flex: 1"></span>{pill("DRAFT v8 · NOT PUBLISHED","rgba(245,163,92,.15)","#F5B57A")}
  </header>
  <div style="flex: 1; display: flex; flex-wrap: wrap">
    <nav aria-label="Policies" style="flex: 1 1 240px; max-width: 280px; padding: 16px 12px; border-right: 1px solid #1E2129; display: flex; flex-direction: column; gap: 4px; box-sizing: border-box">{pol_list}<button style="margin-top: 8px; height: 40px; border-radius: 12px; border: 1px dashed #333846; background: transparent; color: #C3C8D4; font: 500 14px Geist, sans-serif">+ New policy</button></nav>
    <main style="flex: 999 1 480px; min-width: 0; padding: 20px; display: flex; flex-direction: column; gap: 14px">
      <div style="display: flex; flex-direction: column; gap: 4px"><h1 style="margin: 0; font-size: 26px; font-weight: 600; letter-spacing: -.02em">Office laptops</h1><span style="color: #A4ABBA">Applies to group “All staff laptops”. Changes from v7 are marked.</span></div>
      {pgroup("Updates",prow("Install system updates","Devices restart outside working hours",val("Within 3 days"))+prow("Restart window","",val("02:00 – 04:00"))+prow("Rollout rings","25 devices, then 300, then everyone",val("3 rings")))}
      {pgroup("Storage and screen",prow("USB storage","Changed in v8: was “read only”",f'<span style="display: flex; align-items: center; gap: 10px">{pill("CHANGED","rgba(142,162,255,.15)","#A9B6FF")}{val("Blocked")}</span>')+prow("Lock screen after","",val("5 minutes"))+prow("Lock when the owner’s phone leaves","Bluetooth, about 5 metres",sw(True)))}
      {pgroup("Apps and network",prow("Install apps","Only from the software centre · 42 apps allowed",sw(True))+prow("VPN outside the office network","",sw(True))+prow("SECRET-labelled content","Never on laptops; separate instance only",val("Blocked")))}
    </main>
    <aside aria-label="Publish" style="flex: 1 1 300px; max-width: 340px; padding: 20px 20px 20px 0; box-sizing: border-box; display: flex; flex-direction: column; gap: 14px">
      <section style="padding: 18px; border-radius: 18px; background: #11131A; border: 1px solid #1E2129; display: flex; flex-direction: column; gap: 10px">
        <h2 style="margin: 0; font-size: 17px; font-weight: 600">Before you publish</h2>
        <span style="color: #C3C8D4">1,402 devices get this policy.</span>
        <span style="padding: 12px; border-radius: 12px; background: rgba(245,163,92,.08); border: 1px solid rgba(245,163,92,.3); color: #F8C79A; line-height: 1.45">3 people have a USB disk plugged in now. They’ll see a message and lose access to it.</span>
        <a href="#" style="font-size: 14px">Show the 3 devices</a>
      </section>
      {btn("Test on ring 1 · 25 devices",True)}{btn("Publish to everyone")}
      <span style="font-size: 13px; color: #A4ABBA; line-height: 1.5">Publishing needs a second admin’s approval. v7 stays available for one-click rollback.</span>
    </aside>
  </div>''')
open(P+'AdminPolicy.dc.html','w').write(page('Device policy',pol,1440,900,'#07080C'))

# 3. Welcome (first run, empty states)
def todo(n,t,d,cta,done=False): return f'<div style="flex: 1 1 240px; padding: 18px; border-radius: 18px; background: #11131A; border: 1px solid {"rgba(79,209,197,.35)" if done else "#262A35"}; display: flex; flex-direction: column; gap: 8px"><span style="{mono}; color: {"#6FE0D5" if done else "{{accent}}"}">{"DONE" if done else "STEP "+n}</span><span style="font-size: 17px; font-weight: 600">{t}</span><span style="color: #C3C8D4; line-height: 1.45">{d}</span><span style="margin-top: auto; padding-top: 6px">{cta}</span></div>'
def empty(icon_bg,title,text,cta): return f'<section style="flex: 1 1 260px; padding: 22px; border-radius: 18px; background: #0F1117; border: 1px dashed #333846; display: flex; flex-direction: column; align-items: flex-start; gap: 10px"><span style="width: 44px; height: 44px; border-radius: 14px; background: {icon_bg}"></span><span style="font-size: 17px; font-weight: 600">{title}</span><span style="color: #C3C8D4; line-height: 1.5">{text}</span>{cta}</section>'
av=lambda i,bg,n,r: f'<span style="display: flex; align-items: center; gap: 10px"><span style="width: 40px; height: 40px; border-radius: 13px; background: {bg}; color: #0A0B10; font-weight: 700; font-size: 13px; display: flex; align-items: center; justify-content: center">{i}</span><span style="display: flex; flex-direction: column"><span style="font-weight: 600">{n}</span><span style="font-size: 13px; color: #A4ABBA">{r}</span></span></span>'
wel=web(rail_of('Main','IS',True),f'''
  <div style="width: 100%; max-width: 1120px; margin: 0 auto; padding: 36px 24px; box-sizing: border-box; display: flex; flex-direction: column; gap: 26px">
    <div style="display: flex; align-items: flex-end; gap: 20px; flex-wrap: wrap">
      <div style="flex: 1; min-width: 280px; display: flex; flex-direction: column; gap: 6px"><span style="{mono}; color: #A4ABBA">WEDNESDAY 18 NOVEMBER · YOUR FIRST DAY</span><h1 style="margin: 0; font-size: 36px; font-weight: 600; letter-spacing: -.02em">Welcome, Iryna</h1><span style="font-size: 17px; color: #C3C8D4">You’re set up. Three things to do today, then you’re done.</span></div>
      <span style="color: #A4ABBA">1 of 3 done</span>
    </div>
    <div style="display: flex; gap: 14px; flex-wrap: wrap">{todo("1","Set up your phone and laptop","Your phone is your key. Both devices are enrolled and protected.","",True)}{todo("2","Read two short policies","Data protection, and the flood response plan. About 10 minutes.",btn("Start reading",True))}{todo("3","Say hello to your team","Logistics has 28 people. Your channel is #logistics.",btn("Open #logistics"))}</div>
    <section style="padding: 18px; border-radius: 18px; background: #11131A; border: 1px solid #1E2129; display: flex; align-items: center; gap: 28px; flex-wrap: wrap">
      <span style="{mono}; color: #A4ABBA">YOUR PEOPLE</span>{av("OH","#A9B6FF","Olena Hrytsenko","Your manager · meets you at 11:00")}{av("SK","#DDE3F8","Sam Kim","Your buddy this week")}{av("TB","#6FE0D5","Taras Bondar","IT help")}
    </section>
    <div style="display: flex; gap: 14px; flex-wrap: wrap">
      {empty("linear-gradient(155deg, #1B2350, #0B0D14)","No mail yet","Your address is iryna@ministry.example. Messages to you will appear here.",btn("Write a message"))}
      {empty("linear-gradient(155deg, #0E2F2E, #0B0D14)","One invitation","Olena invited you to “Welcome to Logistics”, today 11:00, room 3.12.",f'<span style="display: flex; gap: 8px">{btn("Accept",True)}{btn("Maybe")}</span>')}
      {empty("linear-gradient(155deg, #3A2412, #0B0D14)","Your drive is empty","Files you upload, files shared with you and mail attachments will appear here.",btn("Upload a file"))}
    </div>
  </div>''')
open(P+'WebWelcome.dc.html','w').write(page('Welcome, first run',wel,1440,900,'#07080C'))

# 4. Phone welcome + enrolment
step=lambda done,t,d: f'<div style="display: flex; gap: 14px; align-items: flex-start"><span style="width: 32px; height: 32px; flex: none; border-radius: 11px; display: flex; align-items: center; justify-content: center; font-weight: 700; {"background: rgba(79,209,197,.18); color: #6FE0D5" if done else "background: {{accent}}; color: #0A0B10"}">{"✓" if done else "3"}</span><span style="display: flex; flex-direction: column; gap: 2px"><span style="font-weight: 600">{t}</span><span style="font-size: 14px; color: #C3C8D4; line-height: 1.45">{d}</span></span></div>'
mw=phone(f'''
  <div style="padding: 44px 24px 0; display: flex; flex-direction: column; gap: 22px; flex: 1">
    {mark(56)}
    <div style="display: flex; flex-direction: column; gap: 6px"><h1 style="margin: 0; font-size: 30px; font-weight: 600; letter-spacing: -.02em; line-height: 1.15">Welcome, Iryna</h1><span style="color: #C3C8D4">Ministry of [Name] · Logistics</span></div>
    <div style="display: flex; flex-direction: column; gap: 18px">{step(True,"Code from your welcome letter","MOI-7Q4K-22XP accepted")}{step(True,"Face unlock is on","Needed every time you approve a sign-in")}{step(False,"This phone becomes your key","You’ll scan a code with it to unlock your laptop and to sign documents. No passwords.")}</div>
    <div style="padding: 14px; border-radius: 16px; background: #11131A; border: 1px solid #262A35; display: flex; flex-direction: column; gap: 8px; font-size: 14px"><span style="font-weight: 600">What IT can see on this phone</span><span style="color: #6FE0D5">Yes: app version, system version, whether it’s encrypted</span><span style="color: #C3C8D4">No: your photos, messages, calls or location</span></div>
  </div>
  <div style="padding: 16px 24px 28px; display: flex; flex-direction: column; gap: 10px"><button style="height: 54px; border-radius: 16px; border: 0; background: {{{{accent}}}}; color: #0A0B10; font: 600 17px Geist, sans-serif">Make this phone my key</button><span style="font-size: 13px; color: #A4ABBA; text-align: center">Lost your phone later? IT can turn the key off in one minute.</span></div>''')
open(P+'MobileWelcome.dc.html','w').write(page('Phone welcome and enrolment',mw,390,844))

# 5. Citizen form (public, phone)
chip=lambda t,s=False: f'<button style="height: 44px; padding: 0 16px; border-radius: 22px; font: {"600" if s else "500"} 15px Geist, sans-serif; {"border: 0; background: {{accent}}; color: #0A0B10" if s else "border: 1px solid #333846; background: transparent; color: #ECEEF3"}">{t}</button>'
cf=phone(f'''
  <header style="display: flex; align-items: center; gap: 10px; padding: 16px 20px 10px">
    <span style="width: 36px; height: 36px; border-radius: 10px; background: #F4F5F7; color: #0A0B10; font: 700 10px 'Geist Mono', monospace; display: flex; align-items: center; justify-content: center">[GOV]</span>
    <span style="flex: 1; font-weight: 600">Ministry of [Name]</span><button style="height: 36px; padding: 0 12px; border-radius: 10px; border: 1px solid #333846; background: transparent; color: #ECEEF3; font: 500 14px Geist, sans-serif">EN ▾</button>
  </header>
  <div style="padding: 0 20px; display: flex; gap: 6px"><span style="flex: 1; height: 4px; border-radius: 2px; background: #4FD1C5"></span><span style="flex: 1; height: 4px; border-radius: 2px; background: {{{{accent}}}}"></span><span style="flex: 1; height: 4px; border-radius: 2px; background: #1E2230"></span><span style="flex: 1; height: 4px; border-radius: 2px; background: #1E2230"></span></div>
  <div style="flex: 1; padding: 18px 20px 0; display: flex; flex-direction: column; gap: 18px">
    <div style="display: flex; flex-direction: column; gap: 4px"><span style="{mono}; color: #A4ABBA">STEP 2 OF 4</span><h1 style="margin: 0; font-size: 26px; font-weight: 600; letter-spacing: -.02em">Report flood damage</h1></div>
    <label style="display: flex; flex-direction: column; gap: 8px"><span style="font-weight: 600">Your address</span><input value="14 Mill Lane, District 4" style="height: 50px; padding: 0 14px; border-radius: 14px; border: 1px solid #333846; background: #11131A; color: #ECEEF3; font: 16px Geist, sans-serif"></label>
    <div style="display: flex; flex-direction: column; gap: 8px"><span style="font-weight: 600">What was damaged?</span><div style="display: flex; gap: 8px; flex-wrap: wrap">{chip("Home")}{chip("Car",True)}{chip("Business")}{chip("Road")}{chip("Other")}</div></div>
    <div style="display: flex; flex-direction: column; gap: 8px"><span style="font-weight: 600">Photos <span style="font-weight: 400; color: #A4ABBA">· up to 5</span></span>
      <div style="display: flex; gap: 10px"><span style="width: 84px; height: 84px; border-radius: 14px; background: linear-gradient(135deg,#3A4257,#1A1D27)"></span><span style="width: 84px; height: 84px; border-radius: 14px; background: linear-gradient(135deg,#4A3B2E,#1A1D27)"></span><button aria-label="Add photo" style="width: 84px; height: 84px; border-radius: 14px; border: 1px dashed #333846; background: transparent; color: #C3C8D4; font-size: 26px">+</button></div>
      <div role="alert" style="display: flex; gap: 10px; align-items: center; padding: 12px; border-radius: 14px; background: rgba(245,163,92,.1); border: 1px solid rgba(245,163,92,.35)"><span style="flex: 1; font-size: 14px; color: #F8C79A; line-height: 1.4">garage.heic is larger than 20 MB.</span><button style="height: 36px; padding: 0 12px; border-radius: 10px; border: 0; background: #F5A35C; color: #0A0B10; font: 600 14px Geist, sans-serif">Shrink and add</button></div>
    </div>
  </div>
  <div style="padding: 14px 20px 26px; display: flex; flex-direction: column; gap: 10px"><div style="display: flex; gap: 10px"><button style="height: 52px; padding: 0 20px; border-radius: 16px; border: 1px solid #333846; background: transparent; color: #ECEEF3; font: 500 16px Geist, sans-serif">Back</button><button style="flex: 1; height: 52px; border-radius: 16px; border: 0; background: {{{{accent}}}}; color: #0A0B10; font: 600 16px Geist, sans-serif">Next</button></div><span style="font-size: 13px; color: #A4ABBA; text-align: center">No account needed · your answers are saved on this phone</span></div>''')
open(P+'MobileCitizenForm.dc.html','w').write(page('Citizen form',cf,390,844))

# 6. Citizen receipt
def tl(done,t,d): return f'<div style="display: flex; gap: 12px; align-items: flex-start"><span style="width: 14px; height: 14px; margin-top: 4px; flex: none; border-radius: 50%; {"background: #4FD1C5" if done else "border: 2px solid #333846; box-sizing: border-box"}"></span><span style="display: flex; flex-direction: column"><span style="font-weight: {600 if done else 500}; color: {"#ECEEF3" if done else "#C3C8D4"}">{t}</span><span style="font-size: 14px; color: #A4ABBA">{d}</span></span></div>'
cr=phone(f'''
  <div style="flex: 1; padding: 40px 22px 0; display: flex; flex-direction: column; gap: 20px">
    <span style="width: 60px; height: 60px; border-radius: 20px; background: rgba(79,209,197,.18); color: #6FE0D5; font-size: 30px; display: flex; align-items: center; justify-content: center">✓</span>
    <div style="display: flex; flex-direction: column; gap: 6px"><h1 style="margin: 0; font-size: 28px; font-weight: 600; letter-spacing: -.02em; line-height: 1.15">We have your report, Maria</h1><span style="color: #C3C8D4">A person will answer within 8 working hours, usually much sooner.</span></div>
    <div style="padding: 16px; border-radius: 18px; background: #11131A; border: 1px solid #262A35; display: flex; flex-direction: column; gap: 4px"><span style="{mono}; color: #A4ABBA">YOUR CASE NUMBER</span><span style="font: 600 24px 'Geist Mono', monospace; letter-spacing: .02em">2026/CI/1302</span><span style="font-size: 14px; color: #A4ABBA">Also sent to maria.peters@mail.example</span></div>
    <div style="display: flex; flex-direction: column; gap: 14px">{tl(True,"Report received","Today 08:05 · car, 2 photos")}{tl(False,"Read by Citizen Services","Next")}{tl(False,"Answer by email","By 16:05 today")}{tl(False,"Assessment visit","You choose the time")}</div>
  </div>
  <div style="padding: 14px 22px 26px; display: flex; flex-direction: column; gap: 10px"><a href="MobileBooking.dc.html" style="height: 52px; border-radius: 16px; background: {{{{accent}}}}; color: #0A0B10; font-weight: 600; text-decoration: none; display: flex; align-items: center; justify-content: center">Book an assessment visit</a><button style="height: 50px; border-radius: 16px; border: 1px solid #333846; background: transparent; color: #ECEEF3; font: 500 16px Geist, sans-serif">Add information or photos</button><span style="font-size: 13px; color: #F8C79A; text-align: center">In danger now? Call [EMERGENCY NUMBER]</span></div>''')
open(P+'MobileCitizenReceipt.dc.html','w').write(page('Citizen receipt',cr,390,844))
print('ok')
