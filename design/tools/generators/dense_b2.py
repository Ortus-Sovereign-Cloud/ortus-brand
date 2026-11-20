import sys; sys.path.insert(0,'/tmp/claude-1002/-home-bohdaq-git/6b5adcb0-31d6-44c8-b201-55c34d7527ea/scratchpad/gen')
from dense_lib import edit
edit('WebPersonal',[("n: 'Desktop app · Windows / macOS'","n: 'Desktop app · other systems'"),("'Summaries of long threads and documents'","'Summaries of threads and documents'")])
L='''<span style="font: 500 12px 'Geist Mono', monospace; color: #9198A8; letter-spacing: .06em">%s</span>'''
N='<span style="font-size: 13px; font-weight: 500; color: #9198A8">%s</span>'
edit('AppSwitcher',[
 (L%'COMMUNICATE',N%'Communicate'),(L%'ORGANISE',N%'Organise'),(L%'CREATE & RECORD',N%'Create and record'),(L%'ORGANISATION',N%'Organisation'),
 ('''<span style="position: absolute; right: 10px; top: 8px; font: 500 11px 'Geist Mono', monospace; color: {{accent}}">PIN</span>''','<span title="Pinned to the rail" style="position: absolute; right: 22px; top: 12px; width: 8px; height: 8px; border-radius: 50%; background: {{accent}}; box-shadow: 0 0 0 3px #11131A"></span>',6),
 ('margin: 14px 0 0 10px; width: calc(100% - 26px); max-width: 640px; padding: 18px; border-radius: 22px;','margin: 16px 0 0 12px; width: calc(100% - 28px); max-width: 680px; padding: 28px; border-radius: 22px;'),
 ('box-sizing: border-box; display: flex; flex-direction: column; gap: 14px">\n      <div style="display: flex; align-items: center; gap: 10px">','box-sizing: border-box; display: flex; flex-direction: column; gap: 20px">\n      <div style="display: flex; align-items: center; gap: 12px">'),
 ('margin: 0; flex: 1; font-size: 17px; font-weight: 600">All apps','margin: 0; flex: 1; font-size: 20px; font-weight: 600">All apps'),
 ('width: 200px; height: 34px; padding: 0 10px; border-radius: 10px;','width: 220px; height: 40px; padding: 0 14px; border-radius: 12px;'),
 ('<div style="display: flex; flex-direction: column; gap: 8px"><span','<div style="display: flex; flex-direction: column; gap: 10px"><span',4),
 ('grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 6px">','grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 8px">',4),
 ('gap: 6px; padding: 12px 4px; border-radius: 14px; text-decoration: none; color: #ECEEF3; font-size: 13px; text-align: center">','gap: 8px; padding: 14px 4px; border-radius: 14px; text-decoration: none; color: #ECEEF3; font-size: 14px; text-align: center">',20),
 ('<span style="font-size: 13px; color: #9198A8">Drag an app onto the rail to pin it. Apps your role can’t use are hidden.</span>','<span style="font-size: 13px; color: #9198A8">Drag an app onto the rail to pin it. A dot marks pinned apps.</span>'),
 ("t: 'COMMUNICATE'","t: 'Communicate'"),("t: 'ORGANISE'","t: 'Organise'"),("t: 'CREATE & RECORD'","t: 'Create and record'"),("t: 'ORGANISATION'","t: 'Organisation'"),
])
