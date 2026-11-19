(function () {
  const RES = [["linkedin", "LinkedIn"], ["instagram", "Instagram"], ["youtube", "YouTube"], ["kaggle", "Kaggle"], ["zindi", "Zindi"], ["portfolio", "Portfolio"]];
  const box = document.querySelector(".socials");
  if (box) {
    const data = (typeof LIENS !== "undefined" && LIENS[box.dataset.m]) || {};
    RES.forEach(([k, label]) => {
      const v = data[k], li = document.createElement("li"), el = document.createElement(v ? "a" : "span");
      el.className = "soc" + (v ? "" : " off"); el.textContent = label;
      if (v) { el.href = v; el.target = "_blank"; el.rel = "noopener"; }
      else { el.setAttribute("aria-disabled", "true"); el.title = label + " : bientôt"; }
      li.appendChild(el); box.appendChild(li);
    });
  }
  document.getElementById("yr").textContent = new Date().getFullYear();
  const b = document.querySelector(".burger"), nav = document.getElementById("nav");
  b.addEventListener("click", () => { const o = nav.classList.toggle("open"); b.setAttribute("aria-expanded", o); });
  nav.addEventListener("click", e => { if (e.target.tagName === "A") nav.classList.remove("open"); });
  const els = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) { const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }), { threshold: .1 }); els.forEach(el => io.observe(el)); } else els.forEach(el => el.classList.add("in"));
  const top = document.getElementById("top"); const sc = () => top.classList.toggle("scrolled", scrollY > 12); sc(); addEventListener("scroll", sc, { passive: true });
  // ---- description : texte qui s'allume, chiffres qui comptent, trait du parcours ----
  const reduce = matchMedia("(prefers-reduced-motion:reduce)").matches;
  const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
  document.querySelectorAll(".scrub").forEach(p => {
    const words = p.textContent.trim().split(/\s+/); p.textContent = "";
    words.forEach((w, i) => { const s = document.createElement("span"); s.className = "w"; s.textContent = w + (i < words.length - 1 ? " " : ""); p.appendChild(s); });
  });
  const scrubs = [...document.querySelectorAll(".scrub")], routes = [...document.querySelectorAll(".route")];
  function onScroll() {
    const vh = innerHeight;
    scrubs.forEach(p => { const r = p.getBoundingClientRect(), t = clamp((vh * 0.85 - r.top) / (r.height + vh * 0.35)), ws = p.children, n = ws.length; for (let i = 0; i < n; i++) ws[i].classList.toggle("on", reduce || i / n < t * 1.12); });
    routes.forEach(rt => { const r = rt.getBoundingClientRect(), t = clamp((vh * 0.65 - r.top) / r.height); rt.style.setProperty("--p", reduce ? 1 : t.toFixed(3)); [...rt.children].forEach(li => li.classList.toggle("on", reduce || li.getBoundingClientRect().top < vh * 0.65)); });
  }
  addEventListener("scroll", onScroll, { passive: true }); addEventListener("resize", onScroll); onScroll();
  const counters = [...document.querySelectorAll(".counts b")];
  if (counters.length) {
    const run = b => { const n = +b.dataset.n, s = b.dataset.s || ""; if (reduce) { b.textContent = n + s; return; } const t0 = performance.now(), D = 1400; (function f(t) { const k = clamp((t - t0) / D), e = 1 - Math.pow(1 - k, 3); b.textContent = Math.round(n * e) + s; if (k < 1) requestAnimationFrame(f); })(t0); };
    counters.forEach(b => { b.textContent = "0" + (b.dataset.s || ""); });
    const io2 = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { run(e.target); io2.unobserve(e.target); } }), { threshold: .6 }); counters.forEach(b => io2.observe(b));
  }
})();
