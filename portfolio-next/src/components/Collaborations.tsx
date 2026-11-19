"use client";
import { useEffect, useRef, useState } from "react";

export type Collab = { slug: string; name: string; initials: string; color: string; text: string; photoUrl: string | null };

const SLOTS: [number, number][] = [[0, 0], [1, 0], [0.5, -0.866], [-0.5, -0.866], [-1, 0], [-0.5, 0.866], [0.5, 0.866]];
const LIBRE = { color: "#C4532D", chip: "Place libre", title: "Une alvéole pour vous",
  text: "Un défi, une idée, un projet à construire : l'équipe s'ouvre à d'autres talents. Écrivez-nous et racontez-nous ce que vous voulez bâtir." };

// Les collaborateurs occupent les premières alvéoles ; les autres restent des places libres.
export default function Collaborations({ collabs }: { collabs: Collab[] }) {
  const [cur, setCur] = useState<string>(collabs[0]?.slug ?? "libre");
  const [swap, setSwap] = useState(0);
  const [shown, setShown] = useState(false);
  const cl = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!cl.current) return;
    if (!("IntersectionObserver" in window)) { setShown(true); return; }
    const io = new IntersectionObserver((es, o) => es.forEach((e) => { if (e.isIntersecting) { setShown(true); o.disconnect(); } }), { threshold: 0.3 });
    io.observe(cl.current);
    return () => io.disconnect();
  }, []);

  const show = (k: string) => { if (k !== cur) { setCur(k); setSwap((n) => n + 1); } };
  const c = collabs.find((x) => x.slug === cur);
  const info = c ? { color: c.color, chip: "Collaborateur", title: c.name, text: c.text, href: `/membres/${c.slug}`, cta: "Voir le profil" }
    : { ...LIBRE, href: "#contact", cta: "Nous écrire" };

  return (
    <div className="wrap collab-grid">
      <div className="collab-t">
        <p className="kick">COLLABORATIONS</p>
        <h2 id="t-col" className="reveal">Ceux qui construisent avec nous.</h2>
        <p className="collab-p reveal">Selon les défis, des talents rejoignent l&apos;équipe. Chaque collaboration est une alvéole de plus dans la ruche.</p>
      <div className={"cx-panel" + (swap ? " swap" : "")} key={swap} id="cx-panel" aria-live="polite" style={{ ["--c" as string]: info.color }}>
        <span className="cx-chip">{info.chip}</span>
        <h3>{info.title}</h3>
        <p>{info.text}</p>
        <a href={info.href}>{info.cta} →</a>
      </div>
      </div>
      <div className={"cx-cluster reveal" + (shown ? " in" : "")} ref={cl} id="cx-cluster" role="group" aria-label="Les collaborateurs, en alvéoles">
        {SLOTS.map(([x, y], i) => {
          const m = collabs[i]; const st = { ["--x" as string]: x, ["--y" as string]: y } as React.CSSProperties;
          if (m) {
            if (m.photoUrl) (st as Record<string, string>)["--img"] = `url(${m.photoUrl})`;
            return (
              <a key={m.slug} className={"cx" + (i === 0 ? " you" : "") + (m.photoUrl ? " has" : "")} href={`/membres/${m.slug}`}
                data-vt={m.slug} style={st} aria-label={`${m.name}, collaborateur`}
                onPointerEnter={(e) => e.pointerType === "mouse" && show(m.slug)} onFocus={() => show(m.slug)}>
                <span>{m.initials}</span>
              </a>
            );
          }
          return (
            <button key={i} type="button" className="cx open" style={st} aria-label="Place libre : collaborer avec nous"
              onPointerEnter={(e) => e.pointerType === "mouse" && show("libre")} onFocus={() => show("libre")}
              onClick={() => { show("libre"); document.getElementById("contact")?.scrollIntoView({ behavior: "smooth" }); }}>
              <span>+</span>
            </button>
          );
        })}
      </div>
    </div>
  );
}
