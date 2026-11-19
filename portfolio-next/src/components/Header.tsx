"use client";
import { useEffect, useState } from "react";

// En-tête commun : menu mobile, ombre au défilement, lien actif selon la section visible.
export default function Header({ page }: { page: "home" | "histoire" | "membre" }) {
  const [open, setOpen] = useState(false);
  const [scrolled, setScrolled] = useState(false);
  const [active, setActive] = useState("");
  const home = page === "home";
  const h = (hash: string) => (home ? hash : "/" + hash);

  useEffect(() => {
    const sc = () => setScrolled(scrollY > 12);
    sc();
    addEventListener("scroll", sc, { passive: true });
    return () => removeEventListener("scroll", sc);
  }, []);

  useEffect(() => {
    if (!home) return;
    const ids = ["projets", "equipe", "collaborations"];
    const spy = new IntersectionObserver(
      (es) => es.forEach((en) => en.isIntersecting && setActive(en.target.id)),
      { rootMargin: "-45% 0px -50% 0px" },
    );
    ids.forEach((id) => { const t = document.getElementById(id); if (t) spy.observe(t); });
    return () => spy.disconnect();
  }, [home]);

  const link = (href: string, label: string, id?: string, cls = "") => (
    <a href={href} className={[cls, id && active === id ? "on" : ""].join(" ").trim() || undefined}
      onClick={() => setOpen(false)}>{label}</a>
  );

  return (
    <header className={"top" + (scrolled ? " scrolled" : "")} id="top">
      <a className="brand" href={home ? "#top" : "/"} aria-label="Africa Builders, accueil">
        <svg className="mk" viewBox="-122 -104 244 208" aria-hidden="true"><use href="#emblem" /></svg>
        <span className="wm"><b>africa</b><i>builders</i></span>
      </a>
      <button className="burger" aria-label="Menu" aria-expanded={open} aria-controls="nav" onClick={() => setOpen((o) => !o)}>
        <span></span><span></span>
      </button>
      <nav id="nav" className={open ? "open" : undefined} aria-label="Navigation principale">
        {link("/histoire", "Histoire", undefined, page === "histoire" ? "on-page" : "")}
        {link(h("#projets"), "Projets", "projets")}
        {link(h("#equipe"), "Équipe", "equipe")}
        {link(h("#collaborations"), "Collaborations", "collaborations")}
        {link(h("#contact"), "Nous écrire", undefined, "cta-s")}
      </nav>
    </header>
  );
}
