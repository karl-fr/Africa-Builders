// ===== À REMPLIR : vos coordonnées. Laissez "" pour masquer un bouton. =====
const CONTACT = {
  email: "",      // ex. "bonjour@votre-domaine.com"
  github: "",     // ex. "https://github.com/votre-organisation"
  linkedin: "",   // ex. "https://www.linkedin.com/company/..."
  instagram: ""   // ex. "https://www.instagram.com/..."
};
// ===========================================================================
(function () {
  const box = document.getElementById("contact-links");
  const items = [["email", "Écrire un mail", v => "mailto:" + v], ["github", "GitHub", v => v], ["linkedin", "LinkedIn", v => v], ["instagram", "Instagram", v => v]];
  let n = 0;
  items.forEach(([k, label, href]) => { if (CONTACT[k]) { const a = document.createElement("a"); a.href = href(CONTACT[k]); a.textContent = label; if (k !== "email") { a.target = "_blank"; a.rel = "noopener"; } box.appendChild(a); n++; } });
  if (!n) { const p = document.createElement("p"); p.className = "empty"; p.textContent = "Les coordonnées arrivent bientôt."; box.appendChild(p); }
  document.getElementById("yr").textContent = new Date().getFullYear();
  // menu mobile
  const b = document.querySelector(".burger"), nav = document.getElementById("nav");
  b.addEventListener("click", () => { const o = nav.classList.toggle("open"); b.setAttribute("aria-expanded", o); });
  nav.addEventListener("click", e => { if (e.target.tagName === "A") { nav.classList.remove("open"); b.setAttribute("aria-expanded", false); } });
  // apparition au défilement
  const els = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }), { threshold: .12 });
    els.forEach((el, i) => { el.style.transitionDelay = (i % 4) * 90 + "ms"; io.observe(el); });
  } else els.forEach(el => el.classList.add("in"));
  // nid d'abeille du héro
  const svg = document.querySelector(".hive"), S3 = Math.sqrt(3), R = 54; let d = "";
  const hex = (cx, cy) => { let p = []; for (let k = 0; k < 6; k++) { const a = Math.PI / 180 * (30 + 60 * k); p.push((cx + R * Math.cos(a)).toFixed(1) + " " + (cy + R * Math.sin(a)).toFixed(1)); } return "M" + p.join("L") + "Z"; };
  for (let y = -1; y < 9; y++) for (let x = -1; x < 16; x++) d += hex(x * S3 * R + (y % 2 ? S3 * R / 2 : 0), y * 1.5 * R);
  svg.innerHTML = '<path d="' + d + '" fill="none" stroke="#2a2e57" stroke-width="1.6"/>';
  // ===== v3 : emblème vivant, transitions de pages, en-tête, navigation active =====
  const label = document.getElementById("piece-label");
  if (label) {
    const def = label.innerHTML;
    document.querySelectorAll(".piece").forEach(p => {
      const on = () => { label.innerHTML = "<b>" + p.dataset.name + "</b><span>" + p.dataset.sub + " →</span>"; };
      const off = () => { label.innerHTML = def; };
      p.addEventListener("pointerenter", e => { if (e.pointerType === "mouse") on(); });
      p.addEventListener("pointerleave", off); p.addEventListener("focus", on); p.addEventListener("blur", off);
    });
  }
  // la pièce ou l'alvéole cliquée devient l'avatar du profil (transition entre pages)
  document.addEventListener("click", e => {
    const a = e.target.closest("[data-vt]"); if (!a) return;
    document.querySelectorAll("[data-vt]").forEach(x => { const t = x.querySelector(".hx") || x; t.style.viewTransitionName = ""; });
    const t = a.querySelector(".hx") || a; t.style.viewTransitionName = "av-" + a.dataset.vt;
  });
  window.addEventListener("pageshow", () => document.querySelectorAll("[data-vt]").forEach(x => { const t = x.querySelector(".hx") || x; t.style.viewTransitionName = ""; }));
  const top = document.getElementById("top"); const sc = () => top.classList.toggle("scrolled", scrollY > 12); sc(); addEventListener("scroll", sc, { passive: true });
  // lueur qui suit le pointeur dans le héro
  const hero = document.querySelector(".hero");
  if (hero && matchMedia("(pointer:fine)").matches) hero.addEventListener("pointermove", e => { const r = hero.getBoundingClientRect(); hero.style.setProperty("--mx", (e.clientX - r.left) + "px"); hero.style.setProperty("--my", (e.clientY - r.top) + "px"); });
  // lien actif dans le menu
  const links = [...document.querySelectorAll("nav a[href^='#']")];
  const spy = new IntersectionObserver(es => es.forEach(en => { if (en.isIntersecting) links.forEach(l => l.classList.toggle("on", l.getAttribute("href") === "#" + en.target.id)); }), { rootMargin: "-45% 0px -50% 0px" });
  links.forEach(l => { const t = document.querySelector(l.getAttribute("href")); if (t) spy.observe(t); });
})();

// ===== Projets : onglets + schémas de principe animés =====
(function () {
  const sec = document.getElementById("projets"); if (!sec) return;
  const tabs = [...sec.querySelectorAll(".ptab")], panes = [...sec.querySelectorAll(".pane")];
  const reduce = matchMedia("(prefers-reduced-motion:reduce)").matches;
  let cp = 0, stage = 0, timer = 0, lock = false, visible = false;
  function setStage(s) {
    stage = s; const pane = panes[cp];
    pane.querySelectorAll(".stg").forEach((g, k) => g.classList.toggle("on", k === s));
    pane.querySelectorAll(".sb").forEach((b, k) => b.classList.toggle("on", k === s));
    pane.querySelector(".pj-count").textContent = (s + 1) + " / 3";
    pane.querySelector(".pj-bar i").style.transform = "scaleX(" + ((s + 1) / 3).toFixed(3) + ")";
  }
  function setProject(i) {
    cp = i; lock = false;
    tabs.forEach((t, k) => { t.classList.toggle("on", k === i); t.setAttribute("aria-selected", k === i); t.tabIndex = k === i ? 0 : -1; });
    panes.forEach((p, k) => { p.hidden = k !== i; p.classList.toggle("on", k === i); });
    setStage(0); restart();
  }
  function restart() { clearInterval(timer); if (reduce || lock || !visible) return; timer = setInterval(() => setStage((stage + 1) % 3), 3600); }
  tabs.forEach((t, i) => { t.addEventListener("click", () => setProject(i)); t.addEventListener("keydown", e => { if (e.key === "ArrowRight" || e.key === "ArrowLeft") { const n = (i + (e.key === "ArrowRight" ? 1 : tabs.length - 1)) % tabs.length; setProject(n); tabs[n].focus(); } }); });
  panes.forEach(p => p.querySelectorAll(".sb").forEach(b => b.addEventListener("click", () => { lock = true; clearInterval(timer); setStage(+b.dataset.s); })));
  new IntersectionObserver(es => es.forEach(en => { visible = en.isIntersecting; restart(); }), { threshold: .3 }).observe(sec);
})();

// ===== Collaborations : alvéoles + détail =====
(function () {
  const cl = document.getElementById("cx-cluster"), panel = document.getElementById("cx-panel"); if (!cl) return;
  const INFO = {
    dossou: { c: "#FFB81C", chip: "Collaborateur", t: "Dossou Kajarnak Lokossou", p: "L'idée de la comptabilité vocale en fon est née ensemble avec l'équipe, et nous y travaillons. Le logiciel sera présenté au GPU Challenge 2026.", href: "membres/dossou.html", cta: "Voir le profil" },
    libre: { c: "#C4532D", chip: "Place libre", t: "Une alvéole pour vous", p: "Un défi, une idée, un projet à construire : l'équipe s'ouvre à d'autres talents. Écrivez-nous et racontez-nous ce que vous voulez bâtir.", href: "#contact", cta: "Nous écrire" }
  };
  const def = panel.innerHTML; let cur = "dossou";
  function show(k) { if (k === cur) return; cur = k; const i = INFO[k]; panel.style.setProperty("--c", i.c); panel.innerHTML = '<span class="cx-chip">' + i.chip + "</span><h3>" + i.t + "</h3><p>" + i.p + '</p><a href="' + i.href + '">' + i.cta + " →</a>"; panel.classList.remove("swap"); void panel.offsetWidth; panel.classList.add("swap"); }
  cl.querySelectorAll(".cx").forEach(el => { const k = el.dataset.k; el.addEventListener("pointerenter", e => { if (e.pointerType === "mouse") show(k); }); el.addEventListener("focus", () => show(k)); });
  cl.querySelectorAll(".cx.open").forEach(el => el.addEventListener("click", () => { show("libre"); document.getElementById("contact").scrollIntoView({ behavior: "smooth" }); }));
  if ("IntersectionObserver" in window) new IntersectionObserver((es, o) => es.forEach(e => { if (e.isIntersecting) { cl.classList.add("in"); o.disconnect(); } }), { threshold: .3 }).observe(cl); else cl.classList.add("in");
})();
