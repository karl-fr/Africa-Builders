import base64, os, subprocess
D=os.path.dirname(os.path.abspath(__file__))
NUIT,SOLEIL,LATE,BAO,SABLE,BRUME="#0D1B2A","#F2A33A","#C4532D","#1F7A5A","#F5EFE4","#8A97A6"
def b64(f): return base64.b64encode(open(f"{D}/fonts/{f}","rb").read()).decode()
FONT_CSS=f"""@font-face{{font-family:'Bricolage Grotesque';font-weight:600;src:url(data:font/woff2;base64,{b64('BricolageGrotesque-600.woff2')}) format('woff2')}}
@font-face{{font-family:'Bricolage Grotesque';font-weight:800;src:url(data:font/woff2;base64,{b64('BricolageGrotesque-800.woff2')}) format('woff2')}}"""
def mark_inner(fg,ac,uid="m"):
    return f"""<defs><clipPath id="{uid}"><rect x="0" y="0" width="260" height="180"/></clipPath></defs><g clip-path="url(#{uid})">
<path d="M22 180 L72 50 L122 180" fill="none" stroke="{fg}" stroke-width="28" stroke-linejoin="miter" stroke-miterlimit="12"/>
<rect x="52" y="126" width="40" height="28" fill="{ac}"/>
<path d="M172 36 V180" stroke="{fg}" stroke-width="28"/>
<path d="M172 50 H196 a24 24 0 0 1 0 48 H172 M172 98 H202 a30 30 0 0 1 0 60 H172" fill="none" stroke="{fg}" stroke-width="28" stroke-linejoin="round"/></g>"""
def svg_mark(fg=NUIT,ac=SOLEIL,uid="m"): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 260 180">{mark_inner(fg,ac,uid)}</svg>'
def svg_h(fg=NUIT,ac=SOLEIL,sub=None,uid="h"):
    sub=sub or fg
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 780 180"><style>{FONT_CSS}</style>{mark_inner(fg,ac,uid)}
<text x="300" y="108" font-family="Bricolage Grotesque" font-weight="800" font-size="98" fill="{fg}" letter-spacing="-2">AFRICA</text>
<text x="304" y="160" font-family="Bricolage Grotesque" font-weight="600" font-size="38" fill="{sub}" letter-spacing="17.5">BUILDERS</text></svg>"""
def svg_v(fg=NUIT,ac=SOLEIL,sub=None,uid="v"):
    sub=sub or fg
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 360"><style>{FONT_CSS}</style><g transform="translate(120,0)">{mark_inner(fg,ac,uid)}</g>
<text x="250" y="288" text-anchor="middle" font-family="Bricolage Grotesque" font-weight="800" font-size="98" fill="{fg}" letter-spacing="-2">AFRICA</text>
<text x="259" y="338" text-anchor="middle" font-family="Bricolage Grotesque" font-weight="600" font-size="38" fill="{sub}" letter-spacing="17.5">BUILDERS</text></svg>"""
os.makedirs(f"{D}/logos",exist_ok=True)
files={
 "africa-builders_marque_couleur.svg":svg_mark(),
 "africa-builders_marque_blanc.svg":svg_mark("#FFFFFF","#F2A33A"),
 "africa-builders_marque_mono-noir.svg":svg_mark("#000000","#000000"),
 "africa-builders_horizontal_couleur.svg":svg_h(),
 "africa-builders_horizontal_blanc.svg":svg_h("#FFFFFF","#F2A33A"),
 "africa-builders_horizontal_mono-noir.svg":svg_h("#000000","#000000"),
 "africa-builders_vertical_couleur.svg":svg_v(),
 "africa-builders_vertical_blanc.svg":svg_v("#FFFFFF","#F2A33A"),
 "africa-builders_vertical_mono-noir.svg":svg_v("#000000","#000000"),
}
for n,s in files.items(): open(f"{D}/logos/{n}","w").write(s)
os.system(f"rm -f {D}/logos/mark.svg")
def inl(s,w=None,h=None):  # inline svg with size
    a=(f' width="{w}"' if w else '')+(f' height="{h}"' if h else '')
    return s.replace('<svg ','<svg'+a+' ',1)
import itertools
cnt=itertools.count()
def M(fg=NUIT,ac=SOLEIL,h=None,w=None): return inl(svg_mark(fg,ac,f"u{next(cnt)}"),w,h)
def H(fg=NUIT,ac=SOLEIL,h=None,w=None,sub=None): return inl(svg_h(fg,ac,sub,f"u{next(cnt)}"),w,h)
def V(fg=NUIT,ac=SOLEIL,h=None,w=None): return inl(svg_v(fg,ac,None,f"u{next(cnt)}"),w,h)
pages=[]
def page(cls,body,n=None,title=""):
    foot=f'<div class="foot"><span>Africa Builders · Charte graphique v1.0</span><span>{n:02d}</span></div>' if n else ''
    pages.append(f'<section class="page {cls}">{body}{foot}</section>')
# 1 cover
page("dark cover",f"""<div class="bgb"></div><div class="cm">{M('#FFFFFF',SOLEIL,h=250)}</div>
<div class="ct"><p class="kick">CHARTE GRAPHIQUE · VERSION 1.0</p><h1>Africa<br>Builders</h1><p class="lead">Identité visuelle et règles d'usage de l'équipe, pour tous nos projets, hackathons et communications.</p></div>""")
# 2 sommaire
toc=["Qui nous sommes","Positionnement et valeurs","Le logo","Variantes","Zone de protection et taille minimale","Usages à éviter","Couleurs","Typographie","Formes et motif","Ton et voix","Applications","Fichiers et checklist"]
page("light",f"""<p class="kick">SOMMAIRE</p><h2>Ce que contient ce dossier</h2><ol class="toc">{''.join(f'<li><b>{i+1:02d}</b><span>{t}</span></li>' for i,t in enumerate(toc))}</ol>""",2)
# 3 qui
page("light split",f"""<div><p class="kick">01 · QUI NOUS SOMMES</p><h2>Une équipe de bâtisseurs, née dans les hackathons.</h2>
<p>Africa Builders réunit quatre étudiants qui construisent ensemble des solutions numériques utiles, vite et proprement. Notre premier projet, TraceSon, a obtenu la 3e place du Hackathon IA &amp; Musique, SIMA 2026.</p>
<p>Notre identité doit nous rendre reconnaissables sur chaque projet, que ce soit une présentation, un dépôt de code, une affiche ou un mail.</p></div>
<div class="card"><p class="kick">L'ÉQUIPE</p><ul class="names"><li>Karl Francisco</li><li>Taoufic Moumouni</li><li>Christiano Guidimadjegbe</li><li>Dolorès Obagou</li></ul></div>""",3)
# 4 positionnement
vals=[("Construire","Nous livrons des choses qui marchent, pas seulement des idées."),("Prouver","Nous annonçons ce qui est mesuré et disons ce qui ne l'est pas."),("Servir","Chaque projet part d'un vrai problème rencontré en Afrique."),("Ensemble","Nous gagnons et apprenons en équipe, et nous le montrons.")]
page("light",f"""<p class="kick">02 · POSITIONNEMENT ET VALEURS</p><h2>Concevoir en Afrique, avec rigueur et ambition.</h2>
<p class="sub">Promesse : des projets numériques concrets, utiles et honnêtes.</p>
<div class="grid4">{''.join(f'<div class="card"><i class="brick"></i><h3>{a}</h3><p>{b}</p></div>' for a,b in vals)}</div>""",4)
# 5 logo
page("light split",f"""<div><p class="kick">03 · LE LOGO</p><h2>Un A et un B bâtis comme une construction.</h2>
<p>Le monogramme assemble nos initiales en formes simples et solides, comme des poutres. Le A est une charpente, le B s'appuie sur une même base : l'équipe repose sur un socle commun.</p>
<p>La brique orange, posée au cœur du A, représente ce que nous faisons : chaque projet est une brique ajoutée à l'ensemble. C'est l'élément à reconnaître en premier.</p></div>
<div class="stage">{M(h=300)}</div>""",5)
# 6 variantes
page("light",f"""<p class="kick">04 · VARIANTES</p><h2>Trois formats, trois fonds.</h2><div class="vars">
<div class="v w">{H(h=70)}<span>Horizontal · à privilégier</span></div>
<div class="v w">{V(h=130)}<span>Vertical · couverture, affiche</span></div>
<div class="v w">{M(h=100)}<span>Monogramme · avatar, favicon, sceau</span></div>
<div class="v d">{H('#FFFFFF',SOLEIL,h=70)}<span>Sur fond Nuit</span></div>
<div class="v s">{H(h=70)}<span>Sur fond Sable</span></div>
<div class="v o">{H(NUIT,NUIT,h=70)}<span>Sur fond Soleil · une seule couleur</span></div></div>""",6)
# 7 zone
page("light split",f"""<div><p class="kick">05 · ZONE DE PROTECTION ET TAILLE MINIMALE</p><h2>Laisser respirer le logo.</h2>
<p>Gardez autour du logo un espace libre égal à la hauteur de la brique orange (x) sur les quatre côtés. Aucun texte, image ou bord de page ne doit entrer dans cette zone.</p>
<table class="t"><tr><td>Monogramme seul</td><td><b>16 px</b> / 6 mm</td></tr><tr><td>Logo horizontal</td><td><b>96 px</b> de large / 25 mm</td></tr><tr><td>Logo vertical</td><td><b>64 px</b> de large / 17 mm</td></tr></table></div>
<div class="stage"><div class="zone">{H(h=96)}<em class="x1">x</em><em class="x2">x</em></div></div>""",7)
# 8 interdits
bad=[("Ne pas déformer",f'<div style="transform:scaleX(1.5)">{H(h=60)}</div>'),("Ne pas changer les couleurs",H("#C4532D","#1F7A5A",h=60)),("Ne pas faire pivoter",f'<div style="transform:rotate(-14deg)">{H(h=60)}</div>'),("Ne pas poser sur un fond chargé",f'<div class="busy">{H(h=60)}</div>'),("Pas d'ombre ni de contour",f'<div style="filter:drop-shadow(5px 6px 3px rgba(0,0,0,.55))">{H(h=60)}</div>'),("Ne pas écrire en bas contraste",H("#B9C0C9","#D9DEE4",h=60))]
page("light",f"""<p class="kick">06 · USAGES À ÉVITER</p><h2>Ce que nous ne faisons jamais.</h2><div class="grid3">{''.join(f'<div class="bad"><div class="bx">{s}<b>×</b></div><span>{t}</span></div>' for t,s in bad)}</div>""",8)
# 9 couleurs
cols=[("Nuit",NUIT,"13 27 42","Couleur principale. Fonds sombres, textes, logo.","60 %"),("Soleil",SOLEIL,"242 163 58","Accent. Brique du logo, chiffres clés, boutons.","10 %"),("Sable",SABLE,"245 239 228","Fonds clairs et pages de lecture.","20 %"),("Latérite",LATE,"196 83 45","Accent secondaire. Alertes, rappels, sparingly.","5 %"),("Baobab",BAO,"31 122 90","Succès, validation, états positifs.","3 %"),("Brume",BRUME,"138 151 166","Textes secondaires, filets, légendes.","2 %")]
page("light",f"""<p class="kick">07 · COULEURS</p><h2>Une base sombre, un soleil.</h2><div class="cols">{''.join(f'<div class="sw"><div class="chip" style="background:{h};{"border:1px solid #d6cfc1" if n=="Sable" else ""}"></div><b>{n}</b><code>{h}</code><small>RVB {r}</small><p>{u}</p><i>{p}</i></div>' for n,h,r,u,p in cols)}</div>
<p class="note">Règle de contraste : le texte orange ne s'utilise que sur fond Nuit. Sur fond clair, on utilise Nuit.</p>""".replace("sparingly","avec parcimonie"),9)
# 10 typo
page("light split",f"""<div><p class="kick">08 · TYPOGRAPHIE</p><h2>Deux polices, libres de droits.</h2>
<p><b>Bricolage Grotesque</b> pour les titres, chiffres et le logo : expressive, solide, avec du caractère.</p>
<p><b>Inter</b> pour les textes courants : lisible à toutes les tailles, sur écran comme à l'impression.</p>
<table class="t"><tr><td>Titre</td><td>Bricolage 800 · 40 à 64 pt</td></tr><tr><td>Sous-titre</td><td>Bricolage 600 · 20 à 28 pt</td></tr><tr><td>Texte</td><td>Inter 400 · 12 à 16 pt</td></tr><tr><td>Légende</td><td>Inter 600 · 9 à 11 pt, majuscules espacées</td></tr></table>
<p class="note">Les deux sont gratuites sur Google Fonts. Remplacement si indisponible : Arial.</p></div>
<div class="spec"><div class="big">Aa</div><h3 class="bf">Bricolage Grotesque</h3><p class="bf" style="font-weight:800;font-size:22px">Construire, prouver, servir.</p><div class="big sm">Aa</div><h3 style="font-family:Inter,Arial,sans-serif">Inter</h3><p style="font-family:Inter,Arial,sans-serif">ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>abcdefghijklmnopqrstuvwxyz 0123456789</p></div>""",10)
# 11 formes
page("light split",f"""<div><p class="kick">09 · FORMES ET MOTIF</p><h2>La brique est notre signature.</h2>
<p>Un rectangle orange, proche du rapport 10:7 de la brique du logo, sert de motif : puce de liste, repère de titre, élément de fond. Il rappelle que chaque projet s'ajoute au précédent.</p>
<p>Les angles restent vifs pour les formes du logo. Les cartes et boutons utilisent un arrondi de 12 px.</p></div>
<div class="stage motif"><div class="rows"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div></div>""",11)
# 12 ton
page("light",f"""<p class="kick">10 · TON ET VOIX</p><h2>Clairs, directs, honnêtes.</h2><div class="grid2">
<div class="card"><h3>Nous écrivons</h3><ul><li>En français simple, phrases courtes.</li><li>Avec des chiffres mesurés et sourcés.</li><li>En disant ce qui reste à valider.</li><li>En nous présentant « Équipe Africa Builders ».</li></ul></div>
<div class="card"><h3>Nous évitons</h3><ul><li>Les superlatifs et promesses non prouvées.</li><li>Le jargon qui isole le lecteur.</li><li>Les tirets longs et formules toutes faites.</li><li>De nous présenter comme une entreprise établie.</li></ul></div></div>
<p class="note">Signature type : « Équipe Africa Builders » suivie du nom du projet.</p>""",12)
# 13 applications
page("light",f"""<p class="kick">11 · APPLICATIONS</p><h2>Sur tous nos projets.</h2><div class="apps">
<div class="app"><div class="slide">{H('#FFFFFF',SOLEIL,h=30)}<b>TraceSon</b><small>Hackathon IA &amp; Musique · SIMA 2026</small></div><span>Couverture de présentation</span></div>
<div class="app"><div class="post">{M('#FFFFFF',SOLEIL,h=70)}<b>3e place</b><small>Équipe Africa Builders</small></div><span>Publication réseaux sociaux</span></div>
<div class="app"><div class="mail"><b>Karl Francisco</b><small>Équipe Africa Builders · projet TraceSon</small><i></i>{H(h=34)}</div><span>Signature de mail</span></div>
<div class="app"><div class="readme">{M(h=36)}<div><b>TraceSon</b><small>Un projet Africa Builders</small></div></div><span>README de dépôt de code</span></div></div>""",13)
# 14 projets
page("dark split",f"""<div><p class="kick">12 · MARQUE DE PROJET</p><h2>Chaque projet a son identité, nous gardons la nôtre.</h2>
<p>Un projet (comme TraceSon) peut avoir sa propre palette. La marque Africa Builders y figure toujours sous la forme « Un projet Africa Builders », le monogramme à gauche, en bas de page ou en pied de présentation.</p>
<p>Le projet ne reprend jamais le logo Africa Builders à la place du sien : les deux se complètent.</p></div>
<div class="stage dk"><div class="endorse"><span class="proj">TraceSon</span><div class="sep"></div>{M('#FFFFFF',SOLEIL,h=44)}<small>Un projet<br>Africa Builders</small></div></div>""",14)
# 15 fichiers
page("light split",f"""<div><p class="kick">13 · FICHIERS ET CHECKLIST</p><h2>Avant d'envoyer.</h2><ul class="check"><li>Le bon fichier : couleur sur fond clair, blanc sur fond sombre.</li><li>La zone de protection est respectée.</li><li>Bricolage Grotesque pour les titres, Inter pour le texte.</li><li>Le texte orange n'est que sur fond Nuit.</li><li>« Un projet Africa Builders » figure sur le projet.</li></ul></div>
<div class="card"><p class="kick">DOSSIER LOGOS</p><ul class="files"><li>marque : couleur · blanc · mono-noir</li><li>horizontal : couleur · blanc · mono-noir</li><li>vertical : couleur · blanc · mono-noir</li></ul><p class="note">Formats : SVG (vectoriel, à privilégier) et PNG fond transparent.</p></div>""",15)
css=f"""{FONT_CSS}
@page{{size:1280px 720px;margin:0}}*{{box-sizing:border-box;margin:0;padding:0}}
body{{background:#cfc8ba;font:16px/1.55 Inter,Arial,sans-serif;color:{NUIT}}}
.page{{width:1280px;height:720px;position:relative;overflow:hidden;padding:72px 84px 70px;margin:0 auto 24px;page-break-after:always;break-after:page}}
@media print{{body{{background:none}}.page{{margin:0}}}}
.light{{background:{SABLE}}}.light:not(.split){{display:flex;flex-direction:column;justify-content:center;padding-bottom:90px}}.dark{{background:{NUIT};color:#fff}}
h1,h2,h3,.big,.bf,b{{font-family:'Bricolage Grotesque',Inter,Arial,sans-serif}}
h1{{font-size:112px;line-height:.92;font-weight:800;letter-spacing:-2px}}
h2{{font-size:42px;line-height:1.08;font-weight:800;letter-spacing:-1px;margin:6px 0 22px;max-width:760px}}
h3{{font-size:22px;font-weight:800;margin-bottom:6px}}
.kick{{font:600 12px Inter;letter-spacing:.24em;color:{LATE};margin-bottom:10px}}.dark .kick{{color:{SOLEIL}}}
p{{margin-bottom:14px;max-width:560px}}.sub{{font-size:19px;max-width:none;margin-bottom:26px}}
.foot{{position:absolute;left:84px;right:84px;bottom:26px;display:flex;justify-content:space-between;font-size:11px;color:{BRUME};letter-spacing:.06em}}
.cover{{display:flex;align-items:center;gap:80px}}.cm{{flex:0 0 360px}}.ct .lead{{font-size:20px;margin-top:30px;max-width:520px;color:#c9d1da}}
.bgb{{position:absolute;right:-120px;top:-120px;width:520px;height:520px;background:{SOLEIL};opacity:.08;transform:rotate(14deg)}}
.split{{display:grid;grid-template-columns:1fr 440px;gap:60px;align-items:center}}
.stage{{background:#fff;border-radius:12px;height:440px;display:grid;place-items:center;border:1px solid #e3dccd}}.stage.dk{{background:#14263a;border-color:#1f3550}}
.card{{background:#fff;border-radius:12px;padding:26px 28px;border:1px solid #e3dccd}}.dark .card{{background:#14263a}}
.card ul{{padding-left:20px}}.card li{{margin-bottom:6px}}
.names{{list-style:none;padding:0!important;font:800 26px 'Bricolage Grotesque'}}.names li{{margin-bottom:10px}}
.toc{{list-style:none;columns:2;column-gap:60px;margin-top:20px}}.toc li{{display:flex;gap:18px;padding:12px 0;border-bottom:1px solid #ddd5c6;break-inside:avoid;font-size:19px}}.toc b{{color:{LATE};font-size:19px}}
.grid4{{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}}.grid3{{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}}.grid2{{display:grid;grid-template-columns:1fr 1fr;gap:24px}}
.brick{{display:block;width:34px;height:24px;background:{SOLEIL};margin-bottom:16px}}
.vars{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:10px}}
.v{{height:196px;border-radius:12px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;border:1px solid #e3dccd}}.v span{{font-size:12px;opacity:.75}}
.v.w{{background:#fff}}.v.d{{background:{NUIT};color:#fff}}.v.s{{background:#EADFC8}}.v.o{{background:{SOLEIL}}}
.zone{{position:relative;padding:48px;outline:2px dashed {LATE};outline-offset:-2px;background:repeating-linear-gradient(45deg,rgba(196,83,45,.07) 0 8px,transparent 8px 16px)}}.zone svg{{display:block;background:#fff;outline:1px solid #e3dccd}}
.zone em{{position:absolute;font:800 18px 'Bricolage Grotesque';color:{LATE};font-style:normal}}.x1{{left:14px;top:50%}}.x2{{top:12px;left:50%}}
.t{{border-collapse:collapse;margin-top:12px;width:100%;max-width:560px}}.t td{{padding:11px 0;border-bottom:1px solid #ddd5c6}}
.bad .bx{{height:150px;border-radius:12px;background:#fff;border:1px solid #e3dccd;display:grid;place-items:center;position:relative;overflow:hidden}}.bad .bx b{{position:absolute;top:8px;right:12px;color:{LATE};font-size:26px}}
.bad span{{display:block;margin-top:8px;font-size:14px;font-weight:600}}.busy{{padding:16px 24px;background:linear-gradient(135deg,#F2A33A,#C4532D 40%,#1F7A5A 70%,#0D1B2A)}}
.cols{{display:grid;grid-template-columns:repeat(6,1fr);gap:14px;margin-top:6px}}.sw .chip{{height:150px;border-radius:12px;margin-bottom:12px}}.sw b{{display:block;font-size:20px}}.sw code{{display:block;font:600 13px Inter;margin:2px 0}}.sw small{{display:block;color:#5b6775;font-size:12px}}.sw p{{font-size:13px;line-height:1.4;margin:8px 0 6px}}.sw i{{font:800 18px 'Bricolage Grotesque';color:{LATE};font-style:normal}}
.note{{margin-top:22px;font-size:14px;color:#4b5866;max-width:none}}
.spec{{background:#fff;border-radius:12px;border:1px solid #e3dccd;padding:26px 30px}}.big{{font-size:88px;font-weight:800;line-height:1}}.big.sm{{font-family:Inter;font-weight:600;margin-top:12px}}
.motif{{overflow:hidden;background:{NUIT}}}.rows{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;width:360px;transform:rotate(-8deg)}}.rows i{{display:block;height:48px;background:{SOLEIL};opacity:.9}}.rows i:nth-child(3n+2){{background:#fff;opacity:.9}}.rows i:nth-child(4n){{background:{LATE}}}
.apps{{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}}.app>div{{height:230px;border-radius:12px;padding:22px;display:flex;flex-direction:column;justify-content:flex-end;gap:6px;position:relative;border:1px solid #e3dccd}}.app span{{display:block;margin-top:8px;font-size:13px;font-weight:600}}
.slide{{background:{NUIT};color:#fff;justify-content:flex-start!important}}.slide b{{font-size:36px;margin-top:auto}}.slide small,.post small{{color:{SOLEIL};font-size:12px;letter-spacing:.12em;text-transform:uppercase}}
.post{{background:{NUIT};color:#fff;align-items:flex-start;justify-content:space-between!important}}.post b{{font-size:44px;line-height:1;color:#fff}}
.mail{{background:#fff}}.mail i{{display:block;width:40px;height:3px;background:{SOLEIL};margin:8px 0}}.mail small{{color:#4b5866}}.mail b{{font-size:20px}}
.readme{{background:#fff;flex-direction:row!important;align-items:center;justify-content:center!important;gap:14px!important}}.readme b{{font-size:24px;display:block}}.readme small{{color:#4b5866}}
.endorse{{display:flex;align-items:center;gap:26px;color:#fff}}.proj{{font:800 52px 'Bricolage Grotesque';letter-spacing:-1px}}.sep{{width:2px;height:56px;background:#3a5470}}.endorse small{{font-size:13px;line-height:1.25;color:#c9d1da}}
.check,.files{{list-style:none;padding:0!important}}.check li{{padding:11px 0 11px 36px;position:relative;border-bottom:1px solid #ddd5c6}}.check li:before{{content:"";position:absolute;left:0;top:17px;width:20px;height:14px;background:{SOLEIL}}}.files li{{padding:8px 0;border-bottom:1px solid #eee7d8}}
"""
html=f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Africa Builders · Charte graphique</title><style>{css}</style></head><body>{"".join(pages)}</body></html>'
open(f"{D}/charte_graphique_africa_builders.html","w").write(html)

# PNG export (fond transparent)
import glob
os.makedirs(f"{D}/logos/png",exist_ok=True)
for f in sorted(glob.glob(f"{D}/logos/*.svg")):
    n=os.path.basename(f)[:-4]; vb=open(f).read().split('viewBox="0 0 ')[1].split('"')[0].split(); w,h=float(vb[0]),float(vb[1])
    W=1600; H=int(W*h/w)
    open("/tmp/_p.html","w").write(f'<body style="margin:0;background:transparent"><img src="file://{f}" width="{W}" height="{H}" style="display:block">')
    os.system(f'google-chrome --headless --no-sandbox --disable-gpu --default-background-color=00000000 --hide-scrollbars --screenshot="{D}/logos/png/{n}.png" --window-size={W},{H} file:///tmp/_p.html >/dev/null 2>&1')
