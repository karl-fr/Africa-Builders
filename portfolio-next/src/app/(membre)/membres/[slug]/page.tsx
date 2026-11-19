import type { Metadata } from "next";
import { notFound } from "next/navigation";
import { getMemberBySlug, getMembers, photoUrl, SOCIALS } from "@/lib/data";
import { EmblemDefs, LogoSmall } from "@/components/Emblem";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Progress from "@/components/Progress";
import Reveal from "@/components/Reveal";
import MembreBehaviors from "@/components/MembreBehaviors";

export const revalidate = 300;
export const dynamicParams = true;

export async function generateStaticParams() {
  return (await getMembers()).map((m) => ({ slug: m.slug }));
}

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }): Promise<Metadata> {
  const m = await getMemberBySlug((await params).slug);
  if (!m) return {};
  const tl = m.role === "COLLABORATOR" ? "collaborateur d'Africa Builders" : "membre actif d'Africa Builders";
  return { title: `${m.name} · Africa Builders`, description: `${m.name}, ${tl}. Qui il ou elle est, ce qu'il ou elle fait, et où le retrouver.` };
}

export default async function Membre({ params }: { params: Promise<{ slug: string }> }) {
  const m = await getMemberBySlug((await params).slug);
  if (!m) notFound();
  const img = photoUrl(m.photo);
  const links = Object.fromEntries(m.links.map((l) => [l.kind, l.url]));
  const collab = m.role === "COLLABORATOR";
  const asideStyle = { viewTransitionName: `av-${m.slug}`, ...(img ? { ["--img" as string]: `url(${img})`, ["--pos" as string]: m.photoPos } : {}) } as React.CSSProperties;
  const colorVar = { ["--c" as string]: m.color } as React.CSSProperties;

  const blocks: { k: string; label: string; body: React.ReactNode }[] = [
    { k: "qui", label: "Présentation", body: <p className="scrub">{m.bio}</p> },
  ];
  if (m.facts.length)
    blocks.push({ k: "dist", label: "Distinction", body: (
      <>
        <p className="big-p">Médaille de bronze, Olympiades internationales d&apos;intelligence artificielle (IOAI) 2026, Astana, Kazakhstan.</p>
        <ul className="counts">
          {m.facts.map((f) => {
            const x = /^(\d+)(.*)$/.exec(f.value);
            return <li key={f.id}><b data-n={x?.[1]} data-s={x?.[2]}>{f.value}</b><span>{f.label}</span></li>;
          })}
        </ul>
        {m.extra && <p>{m.extra}</p>}
        {m.sources.length > 0 && (
          <p className="src">Sources : {m.sources.map((s, i) => <span key={s.id}>{i > 0 && " · "}<a href={s.url} target="_blank" rel="noopener">{s.label}</a></span>)}</p>
        )}
      </>
    ) });
  blocks.push({ k: "contrib", label: "Contributions", body: (
    <ol className="route">
      {m.contributions.map((c) => <li key={c.id}><time>{c.date}</time><b>{c.title}</b><span>{c.text}</span></li>)}
    </ol>
  ) });
  if (m.aspiration) blocks.push({ k: "aspi", label: "Ambitions", body: <blockquote className="quote"><p>{m.aspiration}</p></blockquote> });

  return (
    <>
      <a className="skip" href="#contenu">Aller au contenu</a>
      <Progress />
      <Header page="membre" />
      <EmblemDefs />
      <main id="contenu" className="mpage" style={colorVar}>
        <div className="wrap">
          <div className="mgrid">
            <aside className="mside" aria-label={`Profil de ${m.name}`}>
              <a className="back" href="/#equipe">← L&apos;équipe</a>
              <span className={"avatar" + (img ? " has" : "")} aria-hidden="true" style={asideStyle}>{m.initials}</span>
              <h1>{m.name}</h1>
              <p className="role">{m.title}</p>
              {m.badge && <span className="mbadge"><i aria-hidden="true">3</i>{m.badge}</span>}
              <div className="mylogo"><LogoSmall /><span>{collab ? "Collaborateur" : "Membre actif"}</span></div>
              <p className="lbl">Réseaux :</p>
              <ul className="socials">
                {SOCIALS.map(([k, label]) => (
                  <li key={k}>
                    {links[k]
                      ? <a className="soc" href={links[k]} target="_blank" rel="noopener">{label}</a>
                      : <span className="soc off" aria-disabled="true" title={`${label} : bientôt`}>{label}</span>}
                  </li>
                ))}
              </ul>
            </aside>
            <div className="mright">
              {blocks.map((b, j) => (
                <section key={b.k} className={`blk reveal ${b.k}`} id={b.k} data-n={String(j + 1).padStart(2, "0")}>
                  <h2 className="pk">{String(j + 1).padStart(2, "0")} · {b.label}</h2>
                  {b.body}
                </section>
              ))}
            </div>
          </div>
        </div>
      </main>
      <Footer />
      <Reveal stagger={false} />
      <MembreBehaviors />
    </>
  );
}
