// Minimal local shim of the Design Component runtime, for screenshots only.
window.DCLogic = class { constructor(props){ this.props = props || {}; this.state = {}; } setState(s){ Object.assign(this.state, s); } };
document.addEventListener('DOMContentLoaded', () => {
  const host = document.querySelector('x-dc'); if (!host) return;
  const helmet = host.querySelector('helmet'); if (helmet) { [...helmet.childNodes].forEach(n => document.head.appendChild(n)); helmet.remove(); }
  const sc = document.querySelector('script[data-dc-script]');
  let props = {};
  try { const d = JSON.parse(sc.getAttribute('data-props') || '{}'); for (const k in d) if (k[0] !== '$' && d[k] && 'default' in d[k]) props[k] = d[k].default; } catch (e) {}
  let vals = {};
  try { const C = new Function('DCLogic', sc.textContent + '\nreturn Component;')(window.DCLogic); vals = new C(props).renderVals() || {}; } catch (e) { document.title = 'ERR ' + e.message; }
  const look = (path, scope) => {
    path = path.trim();
    if (path === 'true') return true; if (path === 'false') return false; if (/^-?\d+(\.\d+)?$/.test(path)) return +path;
    const parts = path.split('.'); let v;
    for (let i = scope.length - 1; i >= 0; i--) if (parts[0] in scope[i]) { v = scope[i][parts[0]]; break; }
    for (const p of parts.slice(1)) v = v == null ? undefined : v[p];
    return v;
  };
  const sub = (str, scope) => str.replace(/\{\{([^}]+)\}\}/g, (_, p) => { const v = look(p, scope); return v == null || typeof v === 'function' ? '' : String(v); });
  const walk = (node, scope) => {
    for (const ch of [...node.childNodes]) {
      if (ch.nodeType === 3) { if (ch.nodeValue.includes('{{')) ch.nodeValue = sub(ch.nodeValue, scope); continue; }
      if (ch.nodeType !== 1) continue;
      const tag = ch.tagName.toLowerCase();
      if (tag === 'sc-for') {
        const m = (ch.getAttribute('list') || '').match(/\{\{(.+)\}\}/); const list = m ? look(m[1], scope) : [];
        const as = ch.getAttribute('as') || 'item'; const frag = document.createDocumentFragment();
        (list || []).forEach((it, i) => { const wrap = document.createElement('div'); wrap.innerHTML = ch.innerHTML; walk(wrap, scope.concat([{ [as]: it, $index: i }])); [...wrap.childNodes].forEach(n => frag.appendChild(n)); });
        ch.replaceWith(frag); continue;
      }
      if (tag === 'sc-if') {
        const m = (ch.getAttribute('value') || '').match(/\{\{(.+)\}\}/); const ok = m ? look(m[1], scope) : false;
        if (ok) { walk(ch, scope); ch.replaceWith(...ch.childNodes); } else ch.remove(); continue;
      }
      for (const a of [...ch.attributes]) if (a.value.includes('{{')) { if (/^on[A-Z]/.test(a.name) || /^on/.test(a.name)) { ch.removeAttribute(a.name); continue; } try { ch.setAttribute(a.name, sub(a.value, scope)); } catch (e) {} }
      walk(ch, scope);
    }
  };
  walk(host, [vals]);
  document.body.setAttribute('data-ready', '1');
  setTimeout(()=>{document.body.setAttribute('data-h', Math.max(document.documentElement.scrollHeight, document.body.scrollHeight)); document.body.setAttribute('data-w', document.documentElement.scrollWidth);}, 1500);
});
