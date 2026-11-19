import base64, os, glob, math, itertools
D=os.path.dirname(os.path.abspath(__file__)); F=D+"/../fonts/"
INK,IVORY,GOLD,CORAL,MINT,ROYAL,MIST="#12142B","#FBF6EC","#FFB81C","#FF5A4E","#1FC8A1","#3D5AFE","#8B8FA8"
def b64(f): return base64.b64encode(open(F+f,"rb").read()).decode()
FONT=f"""@font-face{{font-family:'Bricolage Grotesque';font-weight:600;src:url(data:font/woff2;base64,{b64('BricolageGrotesque-600.woff2')}) format('woff2')}}
@font-face{{font-family:'Bricolage Grotesque';font-weight:800;src:url(data:font/woff2;base64,{b64('BricolageGrotesque-800.woff2')}) format('woff2')}}
@font-face{{font-family:'Instrument Sans';font-weight:400;src:url(data:font/woff2;base64,{b64('InstrumentSans-400.woff2')}) format('woff2')}}
@font-face{{font-family:'Instrument Sans';font-weight:600;src:url(data:font/woff2;base64,{b64('InstrumentSans-600.woff2')}) format('woff2')}}"""
def hexp(cx,cy,r):
    pts=[(cx+r*math.cos(math.radians(30+60*k)),cy+r*math.sin(math.radians(30+60*k))) for k in range(6)]
    return "M"+" L".join(f"{x:.2f} {y:.2f}" for x,y in pts)+" Z"
S3=math.sqrt(3)
LIL="#9B6BFF"
HR=100; HH=HR*S3/2; SW=26
VB_M="-122 -104 244 208"
def pieces(dark=False,mono=None):
    c=[mono]*4 if mono else [ROYAL,CORAL,MINT,LIL]
    core=mono or GOLD
    ex=f'fill="none" stroke-width="{SW}" stroke-linejoin="miter" stroke-miterlimit="10"'
    return (f'<path d="M-52 {-HH:.1f} L{-HR} 0 L-52 {HH:.1f}" {ex} stroke="{c[0]}"/>'
            f'<path d="M52 {-HH:.1f} L{HR} 0 L52 {HH:.1f}" {ex} stroke="{c[1]}"/>'
            f'<path d="M-34 {-HH:.1f} H34" stroke="{c[2]}" stroke-width="{SW}"/>'
            f'<path d="M-34 {HH:.1f} H34" stroke="{c[3]}" stroke-width="{SW}"/>'
            f'<path d="{hexp_flat(0,0,34)}" fill="{core}" stroke="{core}" stroke-width="6" stroke-linejoin="round"/>')
def hexp_flat(cx,cy,r):
    pts=[(cx+r*math.cos(math.radians(60*k)),cy+r*math.sin(math.radians(60*k))) for k in range(6)]
    return "M"+" L".join(f"{x:.1f} {y:.1f}" for x,y in pts)+" Z"
def svg_mark(dark=False,mono=None): return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{VB_M}">{pieces(dark,mono)}</svg>'
def word(fg,sub,x0): return f'<text x="{x0}" y="22" font-family="Bricolage Grotesque" font-weight="800" font-size="112" fill="{fg}" letter-spacing="-3">africa</text><text x="{x0+4}" y="88" font-family="Bricolage Grotesque" font-weight="600" font-size="54" fill="{sub}" letter-spacing="13">builders</text>'
def svg_h(dark=False,mono=None):
    fg=mono or (IVORY if dark else INK)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-122 -104 790 208"><style>{FONT}</style>{pieces(dark,mono)}{word(fg,fg,150)}</svg>'
def svg_v(dark=False,mono=None):
    fg=mono or (IVORY if dark else INK)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-250 -104 500 400"><style>{FONT}</style>{pieces(dark,mono)}<text x="0" y="214" text-anchor="middle" font-family="Bricolage Grotesque" font-weight="800" font-size="112" fill="{fg}" letter-spacing="-3">africa</text><text x="7" y="280" text-anchor="middle" font-family="Bricolage Grotesque" font-weight="600" font-size="54" fill="{fg}" letter-spacing="13">builders</text></svg>'
def svg_tile(bg=INK,dark=True):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300"><rect width="300" height="300" rx="66" fill="{bg}"/><g transform="translate(150,150) scale(.78)">{pieces(True)}</g></svg>'
K="#000000"
files={"marque_couleur":svg_mark(),"marque_sur-fonce":svg_mark(True),"marque_mono-noir":svg_mark(mono=K),"pastille":svg_tile(),
"horizontal_couleur":svg_h(),"horizontal_sur-fonce":svg_h(True),"horizontal_mono-noir":svg_h(mono=K),
"vertical_couleur":svg_v(),"vertical_sur-fonce":svg_v(True),"vertical_mono-noir":svg_v(mono=K)}
for n,s in files.items(): open(f"{D}/logos/africa-builders_{n}.svg","w").write(s)
def sz(s,h=None,w=None): return s.replace('<svg ','<svg'+(f' height="{h}"' if h else '')+(f' width="{w}"' if w else '')+' ',1)
M=lambda h,d=False,m=None: sz(svg_mark(d,m),h); H=lambda h,d=False,m=None: sz(svg_h(d,m),h); V=lambda h,d=False,m=None: sz(svg_v(d,m),h); T=lambda h: sz(svg_tile(),h)
# contraste WCAG
def lum(h):
    h=h.lstrip('#'); c=[int(h[i:i+2],16)/255 for i in (0,2,4)]
    c=[x/12.92 if x<=.03928 else ((x+.055)/1.055)**2.4 for x in c]; return .2126*c[0]+.7152*c[1]+.0722*c[2]
def cr(a,b):
    la,lb=sorted((lum(a),lum(b)),reverse=True); return (la+.05)/(lb+.05)
def pair(bg,fg,label):
    r=cr(bg,fg); lv="AAA" if r>=7 else "AA" if r>=4.5 else "Titres seulement" if r>=3 else "À éviter"
    return f'<div class="pr" style="background:{bg};color:{fg}"><b>Aa</b><span>{label}</span><em>{r:.1f} : 1 · {lv}</em></div>'
pat=lambda op=.12,c="#fff": f'<svg class="pat" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 720" preserveAspectRatio="xMidYMid slice" style="opacity:{op}">'+"".join(f'<path d="{hexp(x*S3*60+(S3*30 if y%2 else 0),y*90,56)}" fill="none" stroke="{c}" stroke-width="2"/>' for y in range(-1,10) for x in range(-1,23))+'</svg>'
pg=[]
def page(c,b,n=None,t=""): pg.append(f'<section class="page {c}">{b}'+(f'<div class="foot"><span>Africa Builders · Charte graphique</span><span>{n:02d} · {t}</span></div>' if n else '')+'</section>')
# 1 couverture
page("dark cover",f'{pat(.10)}<div class="cm">{M(400,True)}</div><div class="ct"><p class="kick">CHARTE GRAPHIQUE · VERSION 1.0</p><h1>africa<br>builders</h1><p class="lead">Quatre bâtisseurs, une idée au centre. Voilà notre signature.</p></div>')
# 2 sommaire
toc=["Qui nous sommes","Valeurs","Le logo et son histoire","Construction","Variantes","Protection et tailles","Usages à éviter","Couleurs","Contrastes et accessibilité","Typographie","Le motif alvéole","Ton et voix","Applications","Marque de projet","Fichiers et checklist"]
page("light",f'<p class="kick">SOMMAIRE</p><h2>Quinze pages, un seul réflexe.</h2><ol class="toc">{"".join(f"<li><b>{i+3:02d}</b><span>{t}</span></li>" for i,t in enumerate(toc))}</ol>',2,"Sommaire")
# 3 qui
page("light split",f'<div><p class="kick">01 · QUI NOUS SOMMES</p><h2 class="xl">On construit ensemble, et on le montre.</h2><p>Africa Builders réunit quatre étudiants qui bâtissent des solutions numériques utiles, vite et proprement. Notre premier projet, TraceSon, a obtenu la 3e place du Hackathon IA &amp; Musique, SIMA 2026.</p></div><div class="team">{"".join(f"<div><i style=\'background:{c}\'></i><b>{n}</b></div>" for n,c in [("Karl Francisco",ROYAL),("Taoufic Moumouni",CORAL),("Christiano Guidimadjegbe",MINT),("Dolorès Obagou",LIL)])}</div>',3,"Qui nous sommes")
# 4 valeurs
vals=[("Construire","Nous livrons des choses qui marchent, pas seulement des idées.",ROYAL),("Prouver","Nous annonçons ce qui est mesuré, et disons ce qui ne l'est pas.",CORAL),("Servir","Chaque projet part d'un vrai problème rencontré en Afrique.",MINT),("Ensemble","Nous gagnons et apprenons en équipe, et nous le montrons.",GOLD)]
page("light",f'<p class="kick">02 · VALEURS</p><h2>Quatre valeurs, quatre alvéoles.</h2><div class="vals">{"".join(f"<div class=val><div class=hx style=\'background:{c}\'><b>{i+1}</b></div><h3>{a}</h3><p>{b}</p></div>" for i,(a,b,c) in enumerate(vals))}</div>',4,"Valeurs")
# 5 histoire du logo
page("light split",f'<div><p class="kick">03 · LE LOGO ET SON HISTOIRE</p><h2>Quatre pièces autour d\'une idée.</h2><p>Les deux chevrons sont les signes du code : < et >. Avec les deux barres, ils dessinent une alvéole de ruche. C\'est ce que nous faisons, du code, à plusieurs.</p><p>Les quatre pièces sont les quatre bâtisseurs, chacun dans sa couleur. Au centre, l\'alvéole dorée : l\'idée, le projet que nous construisons ensemble. Les ouvertures laissent la place à ceux qui nous rejoindront.</p><ul class="leg"><li><i style="background:{ROYAL}"></i><i style="background:{CORAL}"></i><i style="background:{MINT}"></i><i style="background:{LIL}"></i>Les quatre bâtisseurs</li><li><i style="background:{GOLD}"></i>L\'idée, au cœur</li></ul></div><div class="stage">{M(230)}</div>',5,"Le logo")
# 6 construction
def grid_overlay():
    g=f'<path d="{hexp_flat(0,0,HR)}" fill="none" stroke="{CORAL}" stroke-width="1.2" stroke-dasharray="5 4"/><path d="M-122 0 H122 M0 -104 V104" stroke="{CORAL}" stroke-width=".8" stroke-dasharray="2 4"/><circle cx="0" cy="0" r="34" fill="none" stroke="{CORAL}" stroke-width="1" stroke-dasharray="2 3"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-135 -115 270 230" height="330">{pieces()}{g}<text x="38" y="-4" font-size="12" fill="{CORAL}" font-family="Instrument Sans" font-weight="600">0,34 R</text><text x="60" y="-92" font-size="12" fill="{CORAL}" font-family="Instrument Sans" font-weight="600">R</text></svg>'
page("light split",f'<div><p class="kick">04 · CONSTRUCTION</p><h2>Un hexagone, une mesure : R.</h2><p>Le logo s\'inscrit dans un hexagone de rayon R. Les chevrons ont une épaisseur de 0,26 R, les barres sont centrées sur les côtés haut et bas. Un jeu de 0,18 R sépare chaque pièce.</p><p>L\'alvéole dorée a un rayon de 0,34 R et reste toujours au centre.</p></div><div class="stage">{grid_overlay()}</div>',6,"Construction")


# 7 variantes
page("light",f'<p class="kick">05 · VARIANTES</p><h2>Formats et fonds.</h2><div class="vars"><div class="v w">{H(70)}<span>Horizontal · à privilégier</span></div><div class="v w">{V(150)}<span>Vertical · couverture, affiche</span></div><div class="v w">{M(120)}<span>Carte seule · avatar, favicon</span></div><div class="v d">{H(70,True)}<span>Sur fond Encre</span></div><div class="v i">{H(70)}<span>Sur fond Ivoire</span></div><div class="v o">{H(70,m=INK)}<span>Sur fond Miel · une seule couleur</span></div></div>',7,"Variantes")
# 8 protection
page("light split",f'<div><p class="kick">06 · PROTECTION ET TAILLES</p><h2>Laisser respirer.</h2><p>Gardez autour du logo un espace libre égal à une alvéole entière (R). Aucun texte, image ou bord de page n\'y entre.</p><table class="t"><tr><td>Carte seule</td><td><b>20 px</b> / 7 mm</td></tr><tr><td>Logo horizontal</td><td><b>110 px</b> de large / 28 mm</td></tr><tr><td>Logo vertical</td><td><b>70 px</b> de large / 18 mm</td></tr></table></div><div class="stage"><div class="zone">{H(90)}<em class="x1">R</em><em class="x2">R</em></div></div>',8,"Protection")
# 9 interdits
bad=[("Ne pas déformer",f'<div style="transform:scaleX(1.5)">{H(54)}</div>'),("Ne pas fermer l\'hexagone",sz(svg_mark().replace('</svg>',f'<path d="{hexp_flat(0,0,HR)}" fill="none" stroke="{INK}" stroke-width="10"/></svg>'),62)),("Ne pas changer la couleur du cœur",sz(svg_mark().replace(GOLD,CORAL),62)),("Ne pas poser sur un fond chargé",f'<div class="busy">{H(54)}</div>'),("Pas d\'ombre ni de contour",f'<div style="filter:drop-shadow(5px 6px 3px rgba(0,0,0,.55))">{H(54)}</div>'),("Pas de couleurs hors palette",sz(svg_mark().replace(ROYAL,"#7CFC00").replace(MINT,"#FF00FF"),62))]
page("light",f'<p class="kick">07 · USAGES À ÉVITER</p><h2>Ce que nous ne faisons jamais.</h2><div class="grid3">{"".join(f"<div class=bad><div class=bx>{s}<b>×</b></div><span>{t}</span></div>" for t,s in bad)}</div>',9,"Usages à éviter")
# 10 couleurs
cols=[("Encre",INK,"18 20 43","Fonds sombres, textes, logo. Dominante.","45 %"),("Ivoire",IVORY,"251 246 236","Fonds clairs, pages de lecture.","25 %"),("Miel",GOLD,"255 184 28","L'idée : chiffres clés, accents, boutons.","10 %"),("Royal",ROYAL,"61 90 254","Liens, bleus d'interface.","5 %"),("Corail",CORAL,"255 90 78","Alertes et rappels.","5 %"),("Menthe",MINT,"31 200 161","Réussite, validation.","5 %"),("Lilas",LIL,"155 107 255","Quatrième bâtisseur, accents.","5 %")]
page("light",f'<p class="kick">08 · COULEURS</p><h2>Encre et ivoire, avec cinq éclats.</h2><div class="cols">{"".join(f"<div class=sw><div class=hx2 style=\'background:{h}\'></div><b>{n}</b><code>{h}</code><small>RVB {r}</small><p>{u}</p><i>{p}</i></div>" for n,h,r,u,p in cols)}</div><div class="bar">{"".join(f"<span style=\'flex:{p[:-2]};background:{h}\'></span>" for n,h,r,u,p in cols)}</div>',10,"Couleurs")
# 11 contrastes
page("light",f'<p class="kick">09 · CONTRASTES ET ACCESSIBILITÉ</p><h2>Des couples testés, pas devinés.</h2><div class="prs">{pair(INK,IVORY,"Ivoire sur Encre")}{pair(IVORY,INK,"Encre sur Ivoire")}{pair(INK,GOLD,"Miel sur Encre")}{pair(GOLD,INK,"Encre sur Miel")}{pair(INK,MINT,"Menthe sur Encre")}{pair(IVORY,CORAL,"Corail sur Ivoire")}{pair(IVORY,GOLD,"Miel sur Ivoire")}{pair(IVORY,MINT,"Menthe sur Ivoire")}</div><p class="note">Rapports calculés selon la méthode WCAG. Au-dessus de 4,5 : à utiliser pour du texte courant. Entre 3 et 4,5 : titres et gros chiffres seulement. En dessous : décor uniquement.</p>',11,"Contrastes")
# 12 typo
page("light",f'<p class="kick">10 · TYPOGRAPHIE</p><h2>Deux polices libres, une échelle claire.</h2><div class="typ"><div class="tl"><span class="bf" style="font-size:96px;font-weight:800;line-height:1;letter-spacing:-3px">Aa</span><b>Bricolage Grotesque</b><small>Titres, chiffres, logo · 600 et 800</small></div><div class="tr"><p class="bf" style="font-size:54px;font-weight:800;line-height:1;letter-spacing:-1.5px;margin:0 0 8px">Titre · 48 à 64 pt</p><p class="bf" style="font-size:28px;font-weight:600;margin:0 0 10px">Sous-titre · 22 à 28 pt</p><p style="font-size:17px;margin:0 0 10px">Texte courant en Instrument Sans, 12 à 16 pt, interligne 1,5. Lisible sur écran comme à l\'impression.</p><p style="font:600 12px Instrument Sans;letter-spacing:.24em;color:{CORAL};margin:0">LÉGENDE · 9 À 11 PT · MAJUSCULES ESPACÉES</p></div></div>',12,"Typographie")
# 13 motif
page("dark split",f'{pat(.0)}<div><p class="kick">11 · LE MOTIF ALVÉOLE</p><h2>Une ruche en fond, jamais en bruit.</h2><p>Le nid d\'abeille est notre motif de fond : filet fin sur Encre, ou cellules pleines en couleur pour les affiches. Une seule alvéole dorée peut y signaler l\'élément important.</p><p>Il reste discret derrière du texte : 10 % d\'opacité maximum.</p></div><div class="stage mot">{pat(.35)}<div class="mgold"></div></div>',13,"Motif")
# 14 ton
page("light",f'<p class="kick">12 · TON ET VOIX</p><h2>Clairs, directs, honnêtes.</h2><div class="ba"><div class="bad2"><small>AU LIEU DE</small><p>« Une solution révolutionnaire, 100 % fiable. »</p></div><div class="good2"><small>ÉCRIRE</small><p>« Il retrouve 536 extraits sur 540 dans nos essais. Pas encore testé sur de vraies diffusions. »</p></div><div class="bad2"><small>AU LIEU DE</small><p>« Nous sommes une startup leader. »</p></div><div class="good2"><small>ÉCRIRE</small><p>« Équipe Africa Builders, quatre étudiants. »</p></div></div><p class="note">Français simple, phrases courtes, chiffres mesurés et sourcés, limites annoncées. Pas de tirets longs.</p>',14,"Ton")
# 15 applications
page("light",f'<p class="kick">13 · APPLICATIONS</p><h2>Sur tous nos projets.</h2><div class="apps"><div class="app"><div class="slide">{pat(.08)}{H(34,True)}<b>TraceSon</b><small>Hackathon IA &amp; Musique · SIMA 2026</small></div><span>Couverture de présentation</span></div><div class="app"><div class="post">{pat(.08)}{M(80,True)}<b>3e place</b><small>Équipe Africa Builders</small></div><span>Publication réseaux sociaux</span></div><div class="app"><div class="mail"><b>Karl Francisco</b><small>Équipe Africa Builders · projet TraceSon</small><i></i>{H(40)}</div><span>Signature de mail</span></div><div class="app"><div class="readme">{M(50)}<div><b>TraceSon</b><small>Un projet Africa Builders</small></div></div><span>README de dépôt de code</span></div></div>',15,"Applications")
# 16 projet
page("dark split",f'{pat(.07)}<div><p class="kick">14 · MARQUE DE PROJET</p><h2>Chaque projet a sa voix. L\'équipe signe.</h2><p>Un projet comme TraceSon garde son identité. L\'équipe y figure sous la forme « Un projet Africa Builders », alvéoles à gauche, en pied de page ou de présentation.</p><p>Le logo de l\'équipe ne remplace jamais celui du projet : les deux se complètent.</p></div><div class="stage dk"><div class="endorse"><span class="proj">TraceSon</span><div class="sep"></div>{M(54,True)}<small>Un projet<br>Africa Builders</small></div></div>',16,"Marque de projet")
# 17 fichiers
page("light split",f'<div><p class="kick">15 · FICHIERS ET CHECKLIST</p><h2>Avant d\'envoyer.</h2><ul class="check"><li>Version couleur sur fond clair, « sur fond foncé » sur Encre.</li><li>Le cœur reste doré et au centre, les quatre pièces gardent leur couleur.</li><li>Zone de protection d\'une alvéole respectée.</li><li>Texte orange ou miel seulement sur fond Encre.</li><li>« Un projet Africa Builders » présent sur le projet.</li></ul></div><div class="card"><p class="kick">DOSSIER LOGOS</p><ul class="files"><li>carte seule : couleur · sur fond foncé · mono</li><li>horizontal : couleur · sur fond foncé · mono</li><li>vertical : couleur · sur fond foncé · mono</li><li>pastille d\'avatar (carré arrondi)</li></ul><p class="note">SVG (vectoriel) et PNG fond transparent.</p></div>',17,"Fichiers")
HX="polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%)"
css=FONT+f"""@page{{size:1280px 720px;margin:0}}*{{box-sizing:border-box;margin:0;padding:0}}body{{background:#bbb;font:16px/1.55 'Instrument Sans',Arial,sans-serif;color:{INK}}}
.page{{width:1280px;height:720px;position:relative;overflow:hidden;padding:72px 84px 70px;margin:0 auto 24px;break-after:page}}@media print{{body{{background:none}}.page{{margin:0}}}}
.light{{background:{IVORY}}}.dark{{background:{INK};color:{IVORY}}}.light:not(.split){{display:flex;flex-direction:column;justify-content:center;padding-bottom:90px}}
.pat{{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}}.page>*{{position:relative}}.page>.pat{{position:absolute}}
h1,h2,h3,b,.bf{{font-family:'Bricolage Grotesque',Arial,sans-serif}}h1{{font-size:132px;line-height:.88;font-weight:800;letter-spacing:-4px}}h2{{font-size:44px;line-height:1.05;font-weight:800;letter-spacing:-1.2px;margin:6px 0 24px;max-width:740px}}h2.xl{{font-size:56px}}h3{{font-size:24px;font-weight:800;margin:14px 0 4px}}
.kick{{font:600 12px 'Instrument Sans';letter-spacing:.24em;color:{CORAL};margin-bottom:10px}}.dark .kick{{color:{GOLD}}}p{{margin-bottom:14px;max-width:560px}}
.foot{{position:absolute!important;left:84px;right:84px;bottom:26px;display:flex;justify-content:space-between;font-size:11px;color:{MIST}}}
.cover{{display:flex;align-items:center;gap:90px}}.cm{{flex:0 0 400px}}.lead{{font-size:21px;margin-top:30px;max-width:540px;color:#cfd3ea}}
.split{{display:grid;grid-template-columns:1fr 440px;gap:60px;align-items:center}}.stage{{background:#fff;border-radius:16px;height:440px;display:grid;place-items:center;border:1px solid #e7dfcd;position:relative;overflow:hidden}}.stage.dk{{background:#1b1e3d;border-color:#2a2e57}}
.toc{{list-style:none;columns:3;column-gap:50px;margin-top:10px}}.toc li{{display:flex;gap:16px;padding:11px 0;border-bottom:1px solid #e4dccb;break-inside:avoid;font-size:17px}}.toc b{{color:{CORAL}}}
.team{{display:flex;flex-direction:column;gap:14px}}.team div{{display:flex;align-items:center;gap:20px;background:#fff;border-radius:14px;padding:18px 24px;border:1px solid #e7dfcd}}.team i{{width:46px;height:52px;clip-path:{HX}}}.team b{{font-size:24px}}
.vals{{display:grid;grid-template-columns:repeat(4,1fr);gap:26px}}.hx{{width:110px;height:124px;clip-path:{HX};display:grid;place-items:center}}.hx b{{font-size:44px;color:{INK}}}.val p{{font-size:15px}}
.leg{{list-style:none;margin-top:18px}}.leg li{{display:flex;align-items:center;gap:6px;margin:8px 0;font-weight:600}}.leg i{{width:20px;height:23px;clip-path:{HX};display:inline-block}}.leg li i:last-of-type{{margin-right:10px}}
.vars{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}}.v{{height:196px;border-radius:14px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;border:1px solid #e7dfcd}}.v span{{font-size:12px;opacity:.75}}.v.w{{background:#fff}}.v.d{{background:{INK};color:#fff}}.v.i{{background:#F1E9D6}}.v.o{{background:{GOLD}}}
.zone{{position:relative;padding:50px 56px;outline:2px dashed {CORAL};outline-offset:-2px;background:repeating-linear-gradient(45deg,rgba(255,90,78,.07) 0 8px,transparent 8px 16px)}}.zone svg{{display:block;background:#fff}}.zone em{{position:absolute;font:800 18px 'Bricolage Grotesque';color:{CORAL};font-style:normal}}.x1{{left:16px;top:50%}}.x2{{top:14px;left:50%}}
.t{{border-collapse:collapse;margin-top:12px;width:100%;max-width:560px}}.t td{{padding:11px 0;border-bottom:1px solid #e4dccb}}
.grid3{{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}}.bad .bx{{height:140px;border-radius:14px;background:#fff;border:1px solid #e7dfcd;display:grid;place-items:center;position:relative;overflow:hidden}}.bad .bx b{{position:absolute;top:8px;right:12px;color:{CORAL};font-size:26px}}.bad span{{display:block;margin-top:8px;font-size:14px;font-weight:600}}.busy{{padding:14px 22px;background:linear-gradient(135deg,{GOLD},{CORAL} 40%,{MINT} 70%,{ROYAL})}}
.cols{{display:grid;grid-template-columns:repeat(7,1fr);gap:12px}}.hx2o{{filter:drop-shadow(0 0 1.2px #8a8a8a)}}.hx2{{width:100%;aspect-ratio:1/1.15;clip-path:{HX};margin-bottom:12px}}.sw b{{display:block;font-size:20px}}.sw code{{display:block;font:600 13px 'Instrument Sans'}}.sw small{{display:block;color:#5b5f7a;font-size:12px}}.sw p{{font-size:13px;line-height:1.35;margin:6px 0}}.sw i{{font:800 18px 'Bricolage Grotesque';color:{CORAL};font-style:normal}}
.bar{{display:flex;height:22px;border-radius:11px;overflow:hidden;margin-top:26px;border:1px solid #e7dfcd}}
.prs{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}}.pr{{border-radius:14px;padding:18px;display:flex;flex-direction:column;gap:6px;border:1px solid #e7dfcd}}.pr b{{font-size:44px;line-height:1}}.pr span{{font-weight:600;font-size:14px}}.pr em{{font-style:normal;font-size:12px;opacity:.9}}
.note{{margin-top:22px;font-size:14px;color:#4b4f6e;max-width:none}}
.typ{{display:grid;grid-template-columns:360px 1fr;gap:60px;align-items:center;margin-top:10px}}.tl small{{display:block;color:#5b5f7a}}.tl b{{display:block;font-size:24px}}
.mot{{background:#1b1e3d}}.mgold{{position:absolute;left:46%;top:44%;width:76px;height:86px;clip-path:{HX};background:{GOLD}}}
.ba{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}.ba>div{{border-radius:14px;padding:20px 24px}}.ba p{{margin:6px 0 0;font:600 19px/1.35 'Bricolage Grotesque'}}.bad2{{background:#efe7d6;color:#6b6b7a}}.bad2 p{{text-decoration:line-through;text-decoration-color:{CORAL}}}.good2{{background:{INK};color:#fff}}.ba small{{font:600 11px 'Instrument Sans';letter-spacing:.2em;opacity:.7}}
.apps{{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}}.app>div{{height:236px;border-radius:14px;padding:22px;display:flex;flex-direction:column;justify-content:flex-end;gap:6px;border:1px solid #e7dfcd;position:relative;overflow:hidden}}.app span{{display:block;margin-top:8px;font-size:13px;font-weight:600}}
.slide,.post{{background:{INK};color:#fff}}.slide{{justify-content:flex-start!important}}.slide b{{font-size:38px;margin-top:auto}}.slide small,.post small{{color:{GOLD};font-size:12px;letter-spacing:.12em;text-transform:uppercase}}.post{{align-items:flex-start;justify-content:space-between!important}}.post b{{font-size:46px;line-height:1}}
.mail{{background:#fff}}.mail i{{display:block;width:40px;height:3px;background:{GOLD};margin:8px 0}}.mail small{{color:#5b5f7a}}.mail b{{font-size:20px}}.readme{{background:#fff;flex-direction:row!important;align-items:center;justify-content:center!important;gap:14px!important}}.readme b{{font-size:24px;display:block}}.readme small{{color:#5b5f7a}}
.endorse{{display:flex;align-items:center;gap:26px;color:#fff}}.proj{{font:800 52px 'Bricolage Grotesque';letter-spacing:-1px}}.sep{{width:2px;height:60px;background:#3b4075}}.endorse small{{font-size:13px;line-height:1.25;color:#cfd3ea}}
.card{{background:#fff;border-radius:14px;padding:26px 28px;border:1px solid #e7dfcd}}.check,.files{{list-style:none}}.check li{{padding:11px 0 11px 40px;position:relative;border-bottom:1px solid #e4dccb}}.check li:before{{content:"";position:absolute;left:0;top:13px;width:22px;height:25px;clip-path:{HX};background:{GOLD}}}.files li{{padding:8px 0;border-bottom:1px solid #eee7d8}}
"""
open(D+"/Africa-Builders_charte-graphique.html","w").write(f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Africa Builders · Charte graphique</title><style>{css}</style></head><body>{"".join(pg)}</body></html>')
for f in sorted(glob.glob(D+"/logos/*.svg")):
    n=os.path.basename(f)[:-4]; vb=open(f).read().split('viewBox="')[1].split('"')[0].split(); w,h=float(vb[2]),float(vb[3]); Wd=1600; Hd=int(Wd*h/w)
    open("/tmp/_p.html","w").write(f'<body style="margin:0;background:transparent"><img src="file://{f}" width="{Wd}" height="{Hd}" style="display:block">')
    os.system(f'google-chrome --headless --no-sandbox --disable-gpu --default-background-color=00000000 --hide-scrollbars --screenshot="{D}/logos/png/{n}.png" --window-size={Wd},{Hd} file:///tmp/_p.html >/dev/null 2>&1')
