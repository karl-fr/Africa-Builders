"use client";
import { useEffect } from "react";

// Héro : libellé qui suit la pièce survolée, lueur du pointeur, transition d'avatar vers le profil.
export default function HeroBehaviors() {
  useEffect(() => {
    const ac = new AbortController(); const sig = { signal: ac.signal };
    const label = document.getElementById("piece-label");
    if (label) {
      const def = label.innerHTML;
      document.querySelectorAll<HTMLElement>(".piece").forEach((p) => {
        const on = () => { label.innerHTML = "<b>" + p.dataset.name + "</b><span>" + p.dataset.sub + " →</span>"; };
        const off = () => { label.innerHTML = def; };
        p.addEventListener("pointerenter", (e) => { if (e.pointerType === "mouse") on(); }, sig);
        p.addEventListener("pointerleave", off, sig);
        p.addEventListener("focus", on, sig);
        p.addEventListener("blur", off, sig);
      });
    }
    const target = (x: Element) => (x.querySelector(".hx") as HTMLElement) || (x as HTMLElement);
    const clear = () => document.querySelectorAll("[data-vt]").forEach((x) => { target(x).style.viewTransitionName = ""; });
    document.addEventListener("click", (e) => {
      const a = (e.target as Element).closest<HTMLElement>("[data-vt]"); if (!a) return;
      clear(); target(a).style.viewTransitionName = "av-" + a.dataset.vt;
    }, sig);
    addEventListener("pageshow", clear, sig);
    const hero = document.querySelector<HTMLElement>(".hero");
    if (hero && matchMedia("(pointer:fine)").matches)
      hero.addEventListener("pointermove", (e) => {
        const r = hero.getBoundingClientRect();
        hero.style.setProperty("--mx", e.clientX - r.left + "px"); hero.style.setProperty("--my", e.clientY - r.top + "px");
      }, sig);
    return () => ac.abort();
  }, []);
  return null;
}
