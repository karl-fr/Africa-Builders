import { db } from "./db";

export const SOCIALS: [string, string][] = [
  ["linkedin", "LinkedIn"], ["instagram", "Instagram"], ["youtube", "YouTube"],
  ["kaggle", "Kaggle"], ["zindi", "Zindi"], ["portfolio", "Portfolio"],
];

export const getMembers = () => db.member.findMany({ orderBy: { position: "asc" } });

export const getMemberBySlug = (slug: string) =>
  db.member.findUnique({
    where: { slug },
    include: {
      contributions: { orderBy: { position: "asc" } },
      facts: { orderBy: { position: "asc" } },
      sources: true,
      links: true,
    },
  });

export const getProjects = () =>
  db.project.findMany({ orderBy: { position: "asc" }, include: { steps: { orderBy: { position: "asc" } } } });

export async function getContact(): Promise<Record<string, string>> {
  const rows = await db.setting.findMany();
  return Object.fromEntries(rows.map((r) => [r.key, r.value]));
}

export const photoUrl = (photo: string | null) => (photo ? `/assets/photos/${photo}` : null);
