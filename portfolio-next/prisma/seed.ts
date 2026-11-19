// Remplit la base avec le contenu du portfolio. Relançable : repart d'une base propre
// pour le contenu éditorial, mais NE TOUCHE PAS aux messages reçus ni aux réseaux déjà saisis.
import { PrismaClient, Role } from "@prisma/client";
const db = new PrismaClient();

const ASPI_EQUIPE =
  "Continuer à construire des solutions numériques utiles à celles et ceux qui en ont besoin en Afrique, et grandir avec l'équipe, projet après projet.";
const H1 = { date: "6-7 novembre 2026", title: "Hackathon IA & Musique, SIMA 2026", text: "Participe à la conception et au développement de TraceSon. L'équipe termine à la 3e place." };
const G1 = { date: "Novembre 2026", title: "GPU Challenge 2026", text: "Travaille sur le logiciel de comptabilité vocale en fon, présenté en candidature." };

type M = {
  slug: string; name: string; firstName: string; initials: string; color: string; role: Role;
  title: string; badge?: string; bio: string; aspiration?: string; extra?: string; photo?: string;
  contributions: { date: string; title: string; text: string }[];
  facts?: { value: string; label: string }[];
  sources?: { label: string; url: string }[];
};

const MEMBERS: M[] = [
  { slug: "karl", name: "Karl Francisco", firstName: "Karl", initials: "KF", color: "#3D5AFE", role: "MEMBER", title: "Équipe Africa Builders", photo: "karl.jpg",
    bio: "Karl étudie au Bénin et se passionne pour les logiciels qui servent vraiment. Sa méthode : partir d'un problème concret, bâtir un prototype qui fonctionne, puis le mesurer honnêtement.",
    aspiration: ASPI_EQUIPE, contributions: [H1, G1] },
  { slug: "taoufic", name: "Taoufic Moumouni", firstName: "Taoufic", initials: "TM", color: "#FF5A4E", role: "MEMBER", title: "Équipe Africa Builders", photo: "taoufic.jpg",
    bio: "Taoufic étudie au Bénin et fait partie de l'équipe Africa Builders. Son envie de construire et d'apprendre en faisant nourrit les projets de l'équipe.",
    aspiration: ASPI_EQUIPE, contributions: [H1, G1] },
  { slug: "christiano", name: "Christiano Guidimadjegbe", firstName: "Christiano", initials: "CG", color: "#1FC8A1", role: "MEMBER",
    title: "Médaillé de bronze aux Olympiades internationales d'IA 2026", badge: "IOAI 2026 · Médaille de bronze", photo: "christiano.jpg",
    bio: "Christiano a décroché la médaille de bronze aux Olympiades internationales d'intelligence artificielle (IOAI) 2026, à Astana, au Kazakhstan. Il y représentait le Bénin face à 437 candidats venus de 106 pays. C'est la première médaille du pays dans cette compétition, qui place le Bénin 3e d'Afrique.",
    aspiration: "Après l'IOAI, Christiano veut continuer à construire avec Africa Builders des projets d'intelligence artificielle utiles à celles et ceux qui en ont besoin en Afrique.",
    extra: "Le Bénin a aussi remporté une mention honorable avec un autre candidat de la délégation. Les Olympiades réunissent chaque année de jeunes talents du monde entier autour de problèmes d'intelligence artificielle.",
    contributions: [H1, G1, { date: "En continu", title: "Intelligence artificielle", text: "Met l'intelligence artificielle, sa discipline de compétition, au service des projets de l'équipe." }],
    facts: [
      { value: "3e", label: "édition des Olympiades, à Astana (Kazakhstan)" },
      { value: "437", label: "candidats venus de 106 pays" },
      { value: "1re", label: "médaille du Bénin à l'IOAI, après une mention honorable en 2025" },
    ],
    sources: [
      { label: "gouv.bj", url: "https://www.gouv.bj/article/3630/le-benin-podium-olympiades-internationales-intelligence-artificielle-ioai-2026/" },
      { label: "La Nation", url: "https://lanation.bj/societe/olympiades-internationales-dintelligence-artificielle-le-benin-decroche-une-medaille-de-bronze-grace-a-emmanuel-guidimadjegbe" },
    ] },
  { slug: "dolores", name: "Dolorès Obagou", firstName: "Dolorès", initials: "DO", color: "#9B6BFF", role: "MEMBER", title: "Équipe Africa Builders",
    bio: "Dolorès étudie au Bénin et fait partie de l'équipe Africa Builders. Sa contribution aide à faire naître des projets qui comptent pour celles et ceux qui les utilisent.",
    aspiration: ASPI_EQUIPE, contributions: [H1] },
  { slug: "dossou", name: "Dossou Kajarnak Lokossou", firstName: "Dossou", initials: "DL", color: "#FFB81C", role: "COLLABORATOR", title: "Comptabilité vocale en fon", photo: "dossou.jpg",
    bio: "Collaborateur de l'équipe Africa Builders sur le projet de comptabilité vocale en fon. L'idée est née ensemble, et l'équipe et lui y travaillent ensemble.",
    extra: "L'idée de la comptabilité vocale en fon est née ensemble avec l'équipe, et nous y travaillons. Le logiciel sera présenté au GPU Challenge 2026.",
    contributions: [{ date: "Novembre 2026", title: "GPU Challenge 2026", text: "L'idée du logiciel de comptabilité vocale en fon est née ensemble avec l'équipe. Ils y travaillent ensemble." }] },
];

const PROJECTS = [
  { slug: "traceson", name: "TraceSon", tag: "3e place · SIMA 2026", status: "ok", tagline: "Reconnaît la musique à la radio",
    lead: "Il reconnaît la musique diffusée à la radio et tient le registre des diffusions.",
    paragraphs: [
      "Chaque chanson a une empreinte sonore, un peu comme une empreinte digitale. TraceSon écoute les radios en ligne, la compare à un catalogue d'œuvres et inscrit ce qu'il reconnaît.",
      "Pour un organisme de gestion collective, ce registre montre ce qui a été diffusé, donc ce qu'il faut rémunérer. Un agent valide ou écarte chaque détection, puis exporte le rapport en PDF ou en CSV.",
    ],
    linkLabel: "Voir le code →", linkUrl: "https://github.com/karl-fr/traceson", chips: null,
    stageTitle: "Schéma de principe · TraceSon", stageNote: "Exemple illustratif, sans données réelles.",
    steps: [
      ["Écoute", "Il écoute les radios diffusées sur internet."],
      ["Empreinte", "Il calcule l'empreinte sonore et la compare à un catalogue."],
      ["Registre", "Chaque morceau reconnu est inscrit : œuvre, artiste, station, moment."],
    ] },
  { slug: "fon", name: "Comptabilité vocale en fon", tag: "En construction", status: "wip", tagline: "Des comptes tenus à la voix",
    lead: "Un commerçant dicte ses ventes à voix haute, ses comptes se remplissent seuls.",
    paragraphs: [
      "Beaucoup de petits commerçants n'ont pas d'outil de comptabilité pensé pour leur langue. Ici, il suffit de parler.",
      "L'idée est née ensemble, avec Dossou Kajarnak Lokossou, et nous y travaillons ensemble. Le projet est en construction : nous travaillons encore à bien comprendre le fon à l'oral.",
    ],
    linkLabel: null, linkUrl: null, chips: ["Langue : fon", "GPU Challenge 2026", "Avec Dossou Kajarnak Lokossou"],
    stageTitle: "Schéma de principe · Comptabilité vocale", stageNote: "Schéma de principe : la reconnaissance du fon est en cours de développement.",
    steps: [
      ["Parole", "Le commerçant dit une vente ou une dépense, en fon."],
      ["Compréhension", "Le logiciel en retire ce qui a été vendu ou acheté, et le montant."],
      ["Cahier", "L'opération est inscrite dans son cahier de comptes."],
    ] },
];

async function main() {
  // contenu éditorial : on repart de zéro, en conservant les réseaux déjà saisis
  const oldLinks = await db.link.findMany({ include: { member: true } });
  await db.member.deleteMany(); await db.project.deleteMany();

  for (const [i, m] of MEMBERS.entries()) {
    const { contributions, facts, sources, ...base } = m;
    const created = await db.member.create({
      data: { ...base, position: i,
        contributions: { create: contributions.map((c, k) => ({ ...c, position: k })) },
        facts: facts ? { create: facts.map((f, k) => ({ ...f, position: k })) } : undefined,
        sources: sources ? { create: sources } : undefined },
    });
    for (const l of oldLinks.filter((x) => x.member.slug === m.slug))
      await db.link.create({ data: { memberId: created.id, kind: l.kind, url: l.url } });
  }
  for (const [i, p] of PROJECTS.entries()) {
    const { steps, paragraphs, chips, ...base } = p;
    await db.project.create({ data: { ...base, position: i, paragraphs: paragraphs.join("\n"), chips: chips ? chips.join("\n") : null,
      steps: { create: steps.map(([title, text], k) => ({ title, text, position: k })) } } });
  }
  // coordonnées : à remplir (ligne vide = bouton masqué). Ne remplace jamais une valeur déjà saisie.
  for (const key of ["email", "github", "linkedin", "instagram"])
    await db.setting.upsert({ where: { key }, update: {}, create: { key, value: "" } });
  console.log("Base remplie :", MEMBERS.length, "profils,", PROJECTS.length, "projets.");
}
main().finally(() => db.$disconnect());
