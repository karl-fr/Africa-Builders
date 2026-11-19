// @ts-nocheck — portage fidèle de membre.js (texte qui s'allume, chiffres qui comptent, trait du parcours)
"use client";
import { useEffect } from "react";

export default function MembreBehaviors() {
  useEffect(() => {
    const ac = new AbortController(); const sig = { signal: ac.signal };
    const reduce = matchMedia("(prefers-reduced-motion:reduce)").matches;
    const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
    document.querySelectorAll(".scrub").forEach((p) => {
      const words = p.textContent.trim().split(/\s+/); p.textContent = "";
      words.forEach((w, i) => { const s = document.createElement("span"); s.className = "w"; s.textContent = w + (i < words.length - 1 ? " " : ""); p.appendChild(s); });
    });
    const scrubs = [...document.querySelectorAll(".scrub")], routes = [...document.querySelectorAll(".route")];
    function onScroll() {
      const vh = innerHeight;
      scrubs.forEach((p) => { const r = p.getBoundingClientRect(), t = clamp((vh * 0.85 - r.top) / (r.height + vh * 0.35)), ws = p.children, n = ws.length; for (let i = 0; i < n; i++) ws[i].classList.toggle("on", reduce || i / n < t * 1.12); });
      routes.forEach((rt) => { const r = rt.getBoundingClientRect(), t = clamp((vh * 0.65 - r.top) / r.height); rt.style.setProperty("--p", reduce ? 1 : t.toFixed(3)); [...rt.children].forEach((li) => li.classList.toggle("on", reduce || li.getBoundingClientRect().top < vh * 0.65)); });
    }
    addEventListener("scroll", onScroll, { passive: true, signal: ac.signal }); addEventListener("resize", onScroll, sig); onScroll();
    const counters = [...document.querySelectorAll(".counts b")]; let io2;
    if (counters.length) {
      const run = (b) => { const n = +b.dataset.n, s = b.dataset.s || ""; if (reduce) { b.textContent = n + s; return; } const t0 = performance.now(), D = 1400; (function f(t) { if (ac.signal.aborted) return; const k = clamp((t - t0) / D), e = 1 - Math.pow(1 - k, 3); b.textContent = Math.round(n * e) + s; if (k < 1) requestAnimationFrame(f); })(t0); };
      counters.forEach((b) => { b.textContent = "0" + (b.dataset.s || ""); });
      io2 = new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { run(e.target); io2.unobserve(e.target); } }), { threshold: 0.6 }); counters.forEach((b) => io2.observe(b));
    }
    return () => { ac.abort(); io2 && io2.disconnect(); };
  }, []);
  return null;
}
