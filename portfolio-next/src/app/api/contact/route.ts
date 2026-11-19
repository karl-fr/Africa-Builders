import { NextResponse } from "next/server";
import { db } from "@/lib/db";

const EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

export async function POST(req: Request) {
  let body: Record<string, unknown>;
  try { body = await req.json(); } catch { return NextResponse.json({ error: "Requête invalide." }, { status: 400 }); }

  // pot de miel : un humain ne remplit pas ce champ caché ; on répond « ok » sans rien enregistrer
  if (typeof body.website === "string" && body.website.trim()) return NextResponse.json({ ok: true });

  const name = String(body.name ?? "").trim().slice(0, 120);
  const email = String(body.email ?? "").trim().slice(0, 200);
  const message = String(body.message ?? "").trim().slice(0, 4000);
  if (!name) return NextResponse.json({ error: "Indiquez votre nom." }, { status: 422 });
  if (!EMAIL.test(email)) return NextResponse.json({ error: "Adresse e-mail invalide." }, { status: 422 });
  if (message.length < 10) return NextResponse.json({ error: "Votre message est un peu court." }, { status: 422 });

  // limite : 3 messages par adresse IP toutes les 10 minutes
  const ip = (req.headers.get("x-forwarded-for") ?? "").split(",")[0].trim().slice(0, 64) || null;
  if (ip) {
    const recent = await db.message.count({ where: { ip, createdAt: { gte: new Date(Date.now() - 10 * 60_000) } } });
    if (recent >= 3) return NextResponse.json({ error: "Trop de messages d'un coup. Réessayez dans quelques minutes." }, { status: 429 });
  }
  await db.message.create({ data: { name, email, message, ip } });
  return NextResponse.json({ ok: true }, { status: 201 });
}
