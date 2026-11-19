"use client";
import { useEffect } from "react";

// Fait apparaître les éléments .reveal quand ils entrent à l'écran.
export default function Reveal({ stagger = true }: { stagger?: boolean }) {
  useEffect(() => {
    const els = [...document.querySelectorAll<HTMLElement>(".reveal")];
    if (!("IntersectionObserver" in window)) { els.forEach((e) => e.classList.add("in")); return; }
    const io = new IntersectionObserver(
      (es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }),
      { threshold: 0.12 },
    );
    els.forEach((el, i) => { if (stagger) el.style.transitionDelay = (i % 4) * 90 + "ms"; io.observe(el); });
    return () => io.disconnect();
  }, [stagger]);
  return null;
}
