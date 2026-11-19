# Génère les pages membres/*.html. Relancer : python3 outils/generer_membres.py
import os, re
D=os.path.dirname(os.path.abspath(__file__))+"/.."
ASPI_EQUIPE="Continuer à construire des solutions numériques utiles à celles et ceux qui en ont besoin en Afrique, et grandir avec l'équipe, projet après projet."
M=[
 dict(id="karl",nom="Karl Francisco",ini="KF",c="#3D5AFE",prenom="Karl",
  titre="Équipe Africa Builders",
  qui="Karl étudie au Bénin et se passionne pour les logiciels qui servent vraiment. Sa méthode : partir d'un problème concret, bâtir un prototype qui fonctionne, puis le mesurer honnêtement.",
  fait=["Participe à la conception et au développement de TraceSon, 3e place du Hackathon IA & Musique, SIMA 2026.","Travaille sur le logiciel de comptabilité vocale en fon présenté au GPU Challenge 2026."],
  aspi=ASPI_EQUIPE),
 dict(id="taoufic",nom="Taoufic Moumouni",ini="TM",c="#FF5A4E",prenom="Taoufic",
  titre="Équipe Africa Builders",
  qui="Taoufic étudie au Bénin et fait partie de l'équipe Africa Builders. Son envie de construire et d'apprendre en faisant nourrit les projets de l'équipe.",
  fait=["Participe à la conception et au développement de TraceSon, 3e place du Hackathon IA & Musique, SIMA 2026.","Travaille sur le logiciel de comptabilité vocale en fon présenté au GPU Challenge 2026."],
  aspi=ASPI_EQUIPE),
  dict(id="christiano",nom="Christiano Guidimadjegbe",ini="CG",c="#1FC8A1",prenom="Christiano",
  titre="Médaillé de bronze aux Olympiades internationales d'IA 2026",
  badge="IOAI 2026 · Médaille de bronze",
  qui="Christiano a décroché la médaille de bronze aux Olympiades internationales d'intelligence artificielle (IOAI) 2026, à Astana, au Kazakhstan. Il y représentait le Bénin face à 437 candidats venus de 106 pays. C'est la première médaille du pays dans cette compétition, qui place le Bénin 3e d'Afrique.",
  fait=["Participe à la conception et au développement de TraceSon, 3e place du Hackathon IA & Musique, SIMA 2026.","Travaille sur le logiciel de comptabilité vocale en fon présenté au GPU Challenge 2026.","Met l'intelligence artificielle, sa discipline de compétition, au service des projets de l'équipe."],
  aspi="Après l'IOAI, Christiano veut continuer à construire avec Africa Builders des projets d'intelligence artificielle utiles à celles et ceux qui en ont besoin en Afrique.",
  faits=[("3e","édition des Olympiades, à Astana (Kazakhstan)"),("437","candidats venus de 106 pays"),("1re","médaille du Bénin à l'IOAI, après une mention honorable en 2025")],
  sources=[("gouv.bj","https://www.gouv.bj/article/3630/le-benin-podium-olympiades-internationales-intelligence-artificielle-ioai-2026/"),("La Nation","https://lanation.bj/societe/olympiades-internationales-dintelligence-artificielle-le-benin-decroche-une-medaille-de-bronze-grace-a-emmanuel-guidimadjegbe")]),
 dict(id="dolores",nom="Dolorès Obagou",ini="DO",c="#9B6BFF",prenom="Dolorès",
  titre="Équipe Africa Builders",
  qui="Dolorès étudie au Bénin et fait partie de l'équipe Africa Builders. Sa contribution aide à faire naître des projets qui comptent pour celles et ceux qui les utilisent.",
  fait=["Participe à la conception et au développement de TraceSon, 3e place du Hackathon IA & Musique, SIMA 2026."],
  aspi=ASPI_EQUIPE),
 dict(id="dossou",nom="Dossou Kajarnak Lokossou",ini="DL",c="#FFB81C",prenom="Dossou",
  titre="Comptabilité vocale en fon",
  qui="Collaborateur de l'équipe Africa Builders sur le projet de comptabilité vocale en fon. L'idée est née ensemble, et l'équipe et lui y travaillent ensemble.",
  fait=["L'idée du logiciel de comptabilité vocale en fon est née ensemble avec l'équipe.","Ils y travaillent ensemble, pour le GPU Challenge 2026."],
  aspi=None),
]
HEAD='''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(nom)s · Africa Builders</title>
<meta name="description" content="%(nom)s, %(tl)s. Qui il ou elle est, ce qu'il ou elle fait, et où le retrouver.">
<meta name="theme-color" content="#12142B">
<link rel="icon" href="../assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="../style.css">
</head>
<body class="membre">
<a class="skip" href="#contenu">Aller au contenu</a>
<div class="progress" aria-hidden="true"><i></i><i></i><i></i><i></i></div>
<header class="top" id="top">
  <a class="brand" href="../index.html" aria-label="Africa Builders, accueil">
    <svg class="mk" viewBox="-122 -104 244 208" aria-hidden="true"><use href="#emblem"/></svg>
    <span class="wm"><b>africa</b><i>builders</i></span>
  </a>
  <button class="burger" aria-label="Menu" aria-expanded="false" aria-controls="nav"><span></span><span></span></button>
  <nav id="nav" aria-label="Navigation principale">
    <a href="../histoire.html">Histoire</a><a href="../index.html#projets">Projets</a><a href="../index.html#equipe">Équipe</a><a href="../index.html#collaborations">Collaborations</a><a class="cta-s" href="../index.html#contact">Nous écrire</a>
  </nav>
</header>
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs><g id="emblem"><g fill="none" stroke-width="26" stroke-miterlimit="10"><path d="M-52 -86.6 L-100 0 L-52 86.6" stroke="#3D5AFE"/><path d="M52 -86.6 L100 0 L52 86.6" stroke="#FF5A4E"/></g><path d="M-34 -86.6 H34" stroke="#1FC8A1" stroke-width="26"/><path d="M-34 86.6 H34" stroke="#9B6BFF" stroke-width="26"/><path d="M34 0 L17 29.4 L-17 29.4 L-34 0 L-17 -29.4 L17 -29.4 Z" fill="#FFB81C" stroke="#FFB81C" stroke-width="6" stroke-linejoin="round"/></g></defs></svg>
'''
TEAM_ITEMS=[("6-7 novembre 2026","Hackathon IA & Musique, SIMA 2026","TraceSon, conçu en deux jours. L'équipe termine à la 3e place."),
 ("Novembre 2026","GPU Challenge 2026","Candidature avec le logiciel de comptabilité vocale en fon.")]
def parcours(m):
    if m["id"]=="dossou": items=[TEAM_ITEMS[1]]
    elif m["id"]=="dolores": items=TEAM_ITEMS[:1]
    else: items=TEAM_ITEMS
    return '<ol class="route">'+"".join(f'<li><time>{d}</time><b>{t}</b><span>{x}</span></li>' for d,t,x in items)+'</ol>'
H1=("6-7 novembre 2026","Hackathon IA & Musique, SIMA 2026","Participe à la conception et au développement de TraceSon. L'équipe termine à la 3e place.")
G1=("Novembre 2026","GPU Challenge 2026","Travaille sur le logiciel de comptabilité vocale en fon, présenté en candidature.")
CONTRIB={
 "karl":[H1,G1],"taoufic":[H1,G1],
 "christiano":[H1,G1,("En continu","Intelligence artificielle","Met l'intelligence artificielle, sa discipline de compétition, au service des projets de l'équipe.")],
 "dolores":[("6-7 novembre 2026","Hackathon IA & Musique, SIMA 2026","Participe à la conception et au développement de TraceSon. L'équipe termine à la 3e place.")],
 "dossou":[("Novembre 2026","GPU Challenge 2026","L'idée du logiciel de comptabilité vocale en fon est née ensemble avec l'équipe. Ils y travaillent ensemble.")],
}
def sections(m):
    p=m["prenom"]; out=[]
    out.append(("qui",f"Qui est {p}","Présentation",f'<p class="scrub">{m["qui"]}</p>'))
    if m.get("faits"):
        faits='<ul class="counts">'+"".join(f'<li><b data-n="{re.match(r"(\d+)(.*)",a).group(1)}" data-s="{re.match(r"(\d+)(.*)",a).group(2)}">{a}</b><span>{b}</span></li>' for a,b in m["faits"])+'</ul>'
        extra='<p>Le Bénin a aussi remporté une mention honorable avec un autre candidat de la délégation. Les Olympiades réunissent chaque année de jeunes talents du monde entier autour de problèmes d\'intelligence artificielle.</p>'
        src='<p class="src">Sources : '+" · ".join(f'<a href="{u}" target="_blank" rel="noopener">{t}</a>' for t,u in m["sources"])+'</p>'
        out.append(("dist","Une distinction","Médaille de bronze, IOAI 2026",f'<p class="big-p">Médaille de bronze, Olympiades internationales d\'intelligence artificielle (IOAI) 2026, Astana, Kazakhstan.</p>{faits}{extra}{src}'))
    route='<ol class="route">'+"".join(f'<li><time>{d}</time><b>{t}</b><span>{x}</span></li>' for d,t,x in CONTRIB[m["id"]])+'</ol>'
    out.append(("contrib","Contributions","Contributions",route))
    if m["aspi"]: out.append(("aspi",f"Ce vers quoi {p} tend","Ambitions",f'<blockquote class="quote"><p>{m["aspi"]}</p></blockquote>'))
    return out
PIECES={"karl":("p1","chevron gauche"),"taoufic":("p2","chevron droit"),"christiano":("p3","barre du haut"),"dolores":("p4","barre du bas"),"dossou":("core","le cœur doré")}
def mini(mid,c):
    paths={"p1":'<path d="M-52 -86.6 L-100 0 L-52 86.6" fill="none" stroke-width="26" stroke-miterlimit="10"/>',"p2":'<path d="M52 -86.6 L100 0 L52 86.6" fill="none" stroke-width="26" stroke-miterlimit="10"/>',"p3":'<path d="M-34 -86.6 H34" stroke-width="26"/>',"p4":'<path d="M-34 86.6 H34" stroke-width="26"/>'}
    own=PIECES[mid][0]; out=""
    for k,p in paths.items(): out+=p.replace("<path",f'<path stroke="{c if k==own else "#d9d3c3"}"',1)
    core='<path d="M34 0 L17 29.4 L-17 29.4 L-34 0 L-17 -29.4 L17 -29.4 Z" fill="%s" stroke="%s" stroke-width="6" stroke-linejoin="round"/>'%(("#FFB81C" if own=="core" else "#e9e2cf"),("#FFB81C" if own=="core" else "#e9e2cf"))
    return f'<svg viewBox="-122 -104 244 208" aria-hidden="true">{out}{core}</svg>'
SPECS={
 "karl":[("Équipe","Africa Builders"),("Projets","TraceSon, comptabilité vocale"),("Pièce du logo","chevron gauche")],
 "taoufic":[("Équipe","Africa Builders"),("Projets","TraceSon, comptabilité vocale"),("Pièce du logo","chevron droit")],
 "christiano":[("Équipe","Africa Builders"),("Distinction","IOAI 2026, bronze"),("Projets","TraceSon, comptabilité vocale"),("Pièce du logo","barre du haut")],
 "dolores":[("Équipe","Africa Builders"),("Projets","TraceSon"),("Pièce du logo","barre du bas")],
 "dossou":[("Statut","Collaborateur"),("Projet","Comptabilité vocale en fon"),("Pièce du logo","le cœur doré")],
}
NUM={"karl":"01","taoufic":"02","christiano":"03","dolores":"04","dossou":"+"}
def emblem_big(mid,c):
    own=PIECES[mid][0]; DIM="#2f3466"
    def col(k): return c if own==k else DIM
    nm=lambda x,y,anc,t,k: f'<text x="{x}" y="{y}" text-anchor="{anc}" class="enm{" on" if own==k else ""}">{t}</text>'
    core=("#FFB81C" if own=="core" else "#4a4630")
    lead=('<path d="M24 -16 L96 -86 H168" stroke="#FFB81C" stroke-width="1.6" fill="none"/><circle cx="24" cy="-16" r="3" fill="#FFB81C"/><text x="170" y="-92" text-anchor="end" class="enm on">Dossou</text>' if own=="core" else "")
    return f'''<svg class="emb" viewBox="-200 -140 400 280" aria-hidden="true">
      <path d="M-52 -86.6 L-100 0 L-52 86.6" fill="none" stroke="{col("p1")}" stroke-width="26" stroke-miterlimit="10"/>
      <path d="M52 -86.6 L100 0 L52 86.6" fill="none" stroke="{col("p2")}" stroke-width="26" stroke-miterlimit="10"/>
      <path d="M-34 -86.6 H34" stroke="{col("p3")}" stroke-width="26"/><path d="M-34 86.6 H34" stroke="{col("p4")}" stroke-width="26"/>
      <path d="M34 0 L17 29.4 L-17 29.4 L-34 0 L-17 -29.4 L17 -29.4 Z" fill="{core}" stroke="{core}" stroke-width="6" stroke-linejoin="round"/>
      {nm(-122,5,"end","Karl","p1")}{nm(122,5,"start","Taoufic","p2")}{nm(0,-106,"middle","Christiano","p3")}{nm(0,118,"middle","Dolorès","p4")}{lead}
    </svg>'''
def logo_small():
    return '<svg class="lg" viewBox="-122 -104 244 208" aria-hidden="true"><g fill="none" stroke-width="26" stroke-miterlimit="10"><path d="M-52 -86.6 L-100 0 L-52 86.6" stroke="#3D5AFE"/><path d="M52 -86.6 L100 0 L52 86.6" stroke="#FF5A4E"/></g><path d="M-34 -86.6 H34" stroke="#1FC8A1" stroke-width="26"/><path d="M-34 86.6 H34" stroke="#9B6BFF" stroke-width="26"/><path d="M34 0 L17 29.4 L-17 29.4 L-34 0 L-17 -29.4 L17 -29.4 Z" fill="#FFB81C" stroke="#FFB81C" stroke-width="6" stroke-linejoin="round"/></svg>'
PHOTOS={"karl":("karl.jpg","50% 30%"),"taoufic":("taoufic.jpg","50% 30%"),"christiano":("christiano.jpg","50% 30%"),"dossou":("dossou.jpg","50% 30%")}
def page(i,m):
    pv=M[(i-1)%len(M)]; nx=M[(i+1)%len(M)]
    tl=("collaborateur d'Africa Builders" if m["id"]=="dossou" else "membre actif d'Africa Builders"); S=sections(m)
    badge=f'<span class="mbadge"><i aria-hidden="true">3</i>{m["badge"]}</span>' if m.get("badge") else ""
    LAB={"qui":"Présentation","dist":"Distinction","contrib":"Contributions","aspi":"Ambitions"}
    blocks="".join(f'<section class="blk reveal {k}" id="{k}" data-n="{j+1:02d}"><h2 class="pk">{j+1:02d} · {LAB[k]}</h2>{body}</section>' for j,(k,t,teas,body) in enumerate(S))
    specs="".join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a,b in SPECS[m["id"]])
    strip="".join(f'<a class="px{" cur" if o["id"]==m["id"] else ""}" href="{o["id"]}.html" style="--c:{o["c"]}" aria-label="{o["nom"]}"{" aria-current=\'page\'" if o["id"]==m["id"] else ""}><i>{o["ini"]}</i><span>{o["nom"].split(" ")[0]}</span></a>' for o in M)
    return (HEAD%dict(nom=m["nom"],tl=tl)).replace('<body class="membre">',f'<body class="membre" style="--c:{m["c"]}">')+f'''
<main id="contenu" class="mpage" style="--c:{m["c"]}">
  <div class="wrap">
    <div class="mgrid">
      <aside class="mside" aria-label="Profil de {m["nom"]}">
        <a class="back" href="../index.html#equipe">← L'équipe</a>
        <span class="avatar{" has" if m["id"] in PHOTOS else ""}" aria-hidden="true" style="view-transition-name:av-{m["id"]}{(";--img:url(assets/photos/"+PHOTOS[m["id"]][0]+");--pos:"+PHOTOS[m["id"]][1]) if m["id"] in PHOTOS else ""}">{m["ini"]}</span>
        <h1>{m["nom"]}</h1>
        <p class="role">{m["titre"]}</p>
        {badge}
        <div class="mylogo">{logo_small()}<span>{"Collaborateur" if m["id"]=="dossou" else "Membre actif"}</span></div>
        <p class="lbl">Réseaux :</p>
        <ul class="socials" data-m="{m["id"]}"></ul>
      </aside>
      <div class="mright">
        {blocks}
      </div>
    </div>
  </div>
</main>
<footer class="foot"><div class="wrap"><span>© <span id="yr">2026</span> Africa Builders</span><span>Quatre bâtisseurs, une idée au centre.</span></div></footer>
<script src="../liens.js"></script>
<script src="../membre.js"></script>
</body>
</html>
'''
os.makedirs(D+"/membres",exist_ok=True)
for i,m in enumerate(M): open(f'{D}/membres/{m["id"]}.html',"w").write(page(i,m))
print(len(M),"pages")
