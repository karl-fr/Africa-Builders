import base64, os, glob, itertools
D=os.path.dirname(os.path.abspath(__file__)); F=D+"/../fonts/"
G,SUN,CLAY,CREAM,MIST="#0E3B2E","#F5B63A","#D9663B","#FBF4E4","#8FA39A"
def b64(f): return base64.b64encode(open(F+f,"rb").read()).decode()
FONT=f"""@font-face{{font-family:'Bricolage Grotesque';font-weight:600;src:url(data:font/woff2;base64,{b64('BricolageGrotesque-600.woff2')}) format('woff2')}}
@font-face{{font-family:'Bricolage Grotesque';font-weight:800;src:url(data:font/woff2;base64,{b64('BricolageGrotesque-800.woff2')}) format('woff2')}}
@font-face{{font-family:'Instrument Sans';font-weight:400;src:url(data:font/woff2;base64,{b64('InstrumentSans-400.woff2')}) format('woff2')}}
@font-face{{font-family:'Instrument Sans';font-weight:600;src:url(data:font/woff2;base64,{b64('InstrumentSans-600.woff2')}) format('woff2')}}"""
def arches(a,b,c): # trois arches : 0..200 de large, 0..170 de haut
    return f"""<g fill="none" stroke-width="17"><path d="M8.5 170 V108 a58 58 0 0 1 116 0 V170" stroke="{a}" transform="translate(33,-50)"/><path d="M32.5 170 V108 a34 34 0 0 1 68 0 V170" stroke="{b}" transform="translate(33,-50)"/></g><path d="M52 170 V108 a14 14 0 0 1 28 0 V170 Z" fill="{c}" transform="translate(33,-50)"/>"""
# zone utile : x 41.5..174.5 ; y 0..120 ; recadrage vb "40 0 136 120"
def svg_mark(a=CLAY,b=SUN,c=G): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="32 -10 136 130">{arches(a,b,c)}</svg>'
def svg_tile(bg=G,a=CLAY,b=SUN,c=CREAM): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200"><rect x="4" y="4" width="192" height="192" rx="44" fill="{bg}"/><g transform="translate(0,34)">{arches(a,b,c)}</g></svg>'
def svg_h(fg=G,sub=G,a=CLAY,b=SUN,c=G):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="32 -10 520 130"><style>{FONT}</style>{arches(a,b,c)}<text x="190" y="70" font-family="Bricolage Grotesque" font-weight="800" font-size="76" fill="{fg}" letter-spacing="-2">africa</text><text x="192" y="112" font-family="Bricolage Grotesque" font-weight="600" font-size="38" fill="{sub}" letter-spacing="9">builders</text></svg>'
def svg_v(fg=G,sub=G,a=CLAY,b=SUN,c=G):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 330 256"><style>{FONT}</style><g transform="translate(97,10)">{arches(a,b,c)}</g><text x="165" y="190" text-anchor="middle" font-family="Bricolage Grotesque" font-weight="800" font-size="76" fill="{fg}" letter-spacing="-2">africa</text><text x="170" y="236" text-anchor="middle" font-family="Bricolage Grotesque" font-weight="600" font-size="38" fill="{sub}" letter-spacing="9">builders</text></svg>'
os.makedirs(D+"/logos/png",exist_ok=True)
W,K="#FFFFFF","#000000"
files={"marque_couleur":svg_mark(),"marque_blanc":svg_mark(CLAY,SUN,CREAM),"marque_mono-noir":svg_mark(K,K,K),"pastille_couleur":svg_tile(),
"horizontal_couleur":svg_h(),"horizontal_blanc":svg_h(W,SUN,CLAY,SUN,CREAM),"horizontal_mono-noir":svg_h(K,K,K,K,K),
"vertical_couleur":svg_v(),"vertical_blanc":svg_v(W,SUN,CLAY,SUN,CREAM),"vertical_mono-noir":svg_v(K,K,K,K,K)}
for n,s in files.items(): open(f"{D}/logos/africa-builders-v2_{n}.svg","w").write(s)
cnt=itertools.count()
def inl(s,w=None,h=None): return s.replace('<svg ','<svg'+(f' width="{w}"' if w else '')+(f' height="{h}"' if h else '')+' ',1)
def M(h=None,**k): return inl(svg_mark(**k),None,h)
def T(h=None,**k): return inl(svg_tile(**k),None,h)
def H(h=None,**k): return inl(svg_h(**k),None,h)
def V(h=None,**k): return inl(svg_v(**k),None,h)
def DM(h): return inl(svg_mark(CLAY,SUN,CREAM),None,h)
def DH(h): return inl(svg_h(W,SUN,CLAY,SUN,CREAM),None,h)
pg=[]
def page(c,b,n=None): pg.append(f'<section class="page {c}">{b}'+(f'<div class="foot"><span>Africa Builders · Proposition de logo B</span><span>{n}</span></div>' if n else '')+'</section>')
page("dark cover",f'<div class="cm">{DM(260)}</div><div class="ct"><p class="kick">PROPOSITION B · LES ARCHES</p><h1>africa<br>builders</h1><p class="lead">Trois arches emboîtées : des portes ouvertes, un passage, une construction qui grandit.</p></div>')
page("light split",f'''<div><p class="kick">LE CONCEPT</p><h2>Des portes qui s'ouvrent, l'une après l'autre.</h2><p>Chaque arche est un projet. La plus petite, au centre, est l'idée de départ. Autour d'elle, chaque nouvelle arche s'appuie sur la précédente : c'est notre façon de grandir, hackathon après hackathon.</p><p>L'arche évoque aussi les ponts, les portes et les voûtes de l'architecture : construire, c'est ouvrir un passage.</p></div><div class="stage">{M(280)}</div>''',2)
page("light",f'''<p class="kick">LES VARIANTES</p><h2>Formats et fonds.</h2><div class="vars"><div class="v w">{H(70)}<span>Horizontal</span></div><div class="v w">{V(150)}<span>Vertical</span></div><div class="v w">{T(120)}<span>Pastille · avatar, favicon</span></div><div class="v d">{DH(70)}<span>Sur fond Baobab</span></div><div class="v c">{H(70,fg=G,sub=G,a=CLAY,b=G,c=G)}<span>Sur fond Crème</span></div><div class="v o">{H(70,fg=G,sub=G,a=G,b=G,c=G)}<span>Sur fond Soleil · une seule couleur</span></div></div>''',3)
cols=[("Baobab",G,"14 59 46","Couleur principale"),("Soleil",SUN,"245 182 58","Accent chaud"),("Argile",CLAY,"217 102 59","Accent secondaire"),("Crème",CREAM,"251 244 228","Fonds clairs"),("Brume",MIST,"143 163 154","Textes secondaires")]
page("light",f'''<p class="kick">COULEURS ET POLICES</p><h2>Vert profond, soleil, terre cuite.</h2><div class="cols">{''.join(f'<div class="sw"><div class="chip" style="background:{h};{"border:1px solid #ddd" if n=="Crème" else ""}"></div><b>{n}</b><code>{h}</code><small>RVB {r}</small><p>{u}</p></div>' for n,h,r,u in cols)}</div><div class="ty"><div><span class="bf big">Aa</span><b>Bricolage Grotesque</b><small>Titres et logo</small></div><div><span class="big isf">Aa</span><b class="isf">Instrument Sans</b><small>Textes courants</small></div></div>''',4)
page("light",f'''<p class="kick">APPLICATIONS</p><h2>Sur nos projets.</h2><div class="apps">
<div class="app"><div class="slide">{DH(34)}<b>TraceSon</b><small>Hackathon IA &amp; Musique · SIMA 2026</small></div><span>Couverture de présentation</span></div>
<div class="app"><div class="post">{DM(70)}<b>3e place</b><small>Équipe Africa Builders</small></div><span>Publication réseaux sociaux</span></div>
<div class="app"><div class="mail"><b>Karl Francisco</b><small>Équipe Africa Builders · projet TraceSon</small><i></i>{H(36)}</div><span>Signature de mail</span></div>
<div class="app"><div class="readme">{M(40)}<div><b>TraceSon</b><small>Un projet Africa Builders</small></div></div><span>README de dépôt de code</span></div></div>''',5)
css=FONT+f"""@page{{size:1280px 720px;margin:0}}*{{box-sizing:border-box;margin:0;padding:0}}body{{background:#ccc;font:16px/1.55 'Instrument Sans',Arial,sans-serif;color:{G}}}
.page{{width:1280px;height:720px;position:relative;overflow:hidden;padding:72px 84px 70px;margin:0 auto 24px;break-after:page}}@media print{{body{{background:none}}.page{{margin:0}}}}
.light{{background:{CREAM}}}.dark{{background:{G};color:#fff}}.light:not(.split){{display:flex;flex-direction:column;justify-content:center;padding-bottom:90px}}
h1,h2,b,.bf{{font-family:'Bricolage Grotesque',Arial,sans-serif}}h1{{font-size:120px;line-height:.9;font-weight:800;letter-spacing:-3px}}h2{{font-size:42px;line-height:1.08;font-weight:800;letter-spacing:-1px;margin:6px 0 24px;max-width:740px}}
.kick{{font:600 12px 'Instrument Sans';letter-spacing:.24em;color:{CLAY};margin-bottom:10px}}.dark .kick{{color:{SUN}}}p{{margin-bottom:14px;max-width:560px}}
.foot{{position:absolute;left:84px;right:84px;bottom:26px;display:flex;justify-content:space-between;font-size:11px;color:{MIST}}}
.cover{{display:flex;align-items:center;gap:90px}}.cm{{flex:0 0 320px}}.lead{{font-size:20px;margin-top:30px;max-width:520px;color:#cfe0d8}}
.split{{display:grid;grid-template-columns:1fr 440px;gap:60px;align-items:center}}.stage{{background:#fff;border-radius:12px;height:440px;display:grid;place-items:center;border:1px solid #eadfc6}}
.vars{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}}.v{{height:196px;border-radius:12px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;border:1px solid #eadfc6}}.v span{{font-size:12px;opacity:.75}}
.v.w{{background:#fff}}.v.d{{background:{G};color:#fff}}.v.c{{background:#F1E6CB}}.v.o{{background:{SUN}}}
.cols{{display:grid;grid-template-columns:repeat(5,1fr);gap:16px}}.sw .chip{{height:120px;border-radius:12px;margin-bottom:10px}}.sw b{{display:block;font-size:20px}}.sw code{{display:block;font-size:13px;font-weight:600}}.sw small{{display:block;font-size:12px;color:#506b60}}.sw p{{font-size:13px;margin:6px 0}}
.ty{{display:flex;gap:80px;margin-top:30px}}.ty>div{{display:flex;align-items:baseline;gap:18px}}.big{{font-size:70px;font-weight:800;line-height:1}}.isf{{font-family:'Instrument Sans';font-weight:600}}.ty small{{color:#506b60}}
.apps{{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}}.app>div{{height:230px;border-radius:12px;padding:22px;display:flex;flex-direction:column;justify-content:flex-end;gap:6px;border:1px solid #eadfc6}}.app span{{display:block;margin-top:8px;font-size:13px;font-weight:600}}
.slide,.post{{background:{G};color:#fff}}.slide{{justify-content:flex-start!important}}.slide b{{font-size:36px;margin-top:auto}}.slide small,.post small{{color:{SUN};font-size:12px;letter-spacing:.12em;text-transform:uppercase}}.post{{align-items:flex-start;justify-content:space-between!important}}.post b{{font-size:44px;line-height:1}}
.mail{{background:#fff}}.mail i{{display:block;width:40px;height:3px;background:{SUN};margin:8px 0}}.mail small{{color:#506b60}}.mail b{{font-size:20px}}.readme{{background:#fff;flex-direction:row!important;align-items:center;justify-content:center!important;gap:14px!important}}.readme b{{font-size:24px;display:block}}.readme small{{color:#506b60}}
"""
open(D+"/proposition_logo_B.html","w").write(f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Africa Builders · Proposition B</title><style>{css}</style></head><body>{"".join(pg)}</body></html>')
# PNG
for f in sorted(glob.glob(D+"/logos/*.svg")):
    n=os.path.basename(f)[:-4]; vb=open(f).read().split('viewBox="')[1].split('"')[0].split(); w,h=float(vb[2]),float(vb[3]); Wd=1600; Hd=int(Wd*h/w)
    open("/tmp/_p.html","w").write(f'<body style="margin:0;background:transparent"><img src="file://{f}" width="{Wd}" height="{Hd}" style="display:block">')
    os.system(f'google-chrome --headless --no-sandbox --disable-gpu --default-background-color=00000000 --hide-scrollbars --screenshot="{D}/logos/png/{n}.png" --window-size={Wd},{Hd} file:///tmp/_p.html >/dev/null 2>&1')

import subprocess
A=open(D+"/../logos/africa-builders_horizontal_couleur.svg").read(); Av=open(D+"/../logos/africa-builders_vertical_couleur.svg").read(); Am=open(D+"/../logos/africa-builders_marque_couleur.svg").read()
Aw=open(D+"/../logos/africa-builders_horizontal_blanc.svg").read()
def sz(sv,h): return sv.replace("<svg ",f'<svg height="{h}" ',1)
cmp=f"""<!doctype html><meta charset=utf-8><style>{FONT}@page{{size:1280px 720px;margin:0}}*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:'Instrument Sans',Arial;color:{G}}}
.pg{{width:1280px;height:720px;display:grid;grid-template-columns:1fr 1fr;position:relative}}.col{{padding:56px 60px;display:flex;flex-direction:column;gap:22px}}.a{{background:#F5EFE4;color:#0D1B2A}}.b{{background:{CREAM}}}
h2{{font:800 40px 'Bricolage Grotesque';letter-spacing:-1px}}.k{{font:600 12px 'Instrument Sans';letter-spacing:.24em;color:{CLAY}}}.box{{flex:1;border-radius:12px;display:grid;place-items:center;background:#fff;border:1px solid #e3dccd}}.row{{display:grid;grid-template-columns:1.4fr 1fr;gap:16px;flex:1}}.dk{{background:#0D1B2A}}.dk2{{background:{G}}}.row>div{{border-radius:12px;display:grid;place-items:center}}
ul{{padding-left:18px;font-size:15px;line-height:1.5}}</style>
<div class=pg><div class="col a"><p class=k>PROPOSITION A · LE MONOGRAMME</p><h2>AB, bâti comme une charpente</h2><div class=row><div style="background:#fff;border:1px solid #e3dccd">{sz(A,50)}</div><div class=dk>{sz(Am.replace('#0D1B2A','#FFFFFF'),90)}</div></div><div class=box style="flex:.8">{sz(Av,150)}</div><ul><li>Lisible tout de suite : on lit AB.</li><li>Sobre, institutionnel, bleu nuit et orange.</li><li>Moins de personnalité visuelle.</li></ul></div>
<div class="col b"><p class=k>PROPOSITION B · LES ARCHES</p><h2>Trois arches, des portes ouvertes</h2><div class=row><div style="background:#fff;border:1px solid #eadfc6">{sz(open(D+"/logos/africa-builders-v2_horizontal_couleur.svg").read(),56)}</div><div class=dk2>{sz(open(D+"/logos/africa-builders-v2_marque_blanc.svg").read(),90)}</div></div><div class=box style="flex:.8;border-color:#eadfc6">{sz(open(D+"/logos/africa-builders-v2_vertical_couleur.svg").read(),150)}</div><ul><li>Plus chaleureux, plus mémorable en petit.</li><li>Vert profond, soleil et terre cuite.</li><li>Ne contient pas nos initiales.</li></ul></div></div>"""
open(D+"/comparaison_A_B.html","w").write(cmp)
