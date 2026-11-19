(function () {
  const yr = document.getElementById("yr"); if (yr) yr.textContent = new Date().getFullYear();
  const b = document.querySelector(".burger"), nav = document.getElementById("nav");
  b.addEventListener("click", () => { const o = nav.classList.toggle("open"); b.setAttribute("aria-expanded", o); });
  nav.addEventListener("click", e => { if (e.target.tagName === "A") nav.classList.remove("open"); });
  const top = document.getElementById("top"); const sc = () => top.classList.toggle("scrolled", scrollY > 12); sc(); addEventListener("scroll", sc, { passive: true });
  const els = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) { const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } }), { threshold: .12 }); els.forEach((el, i) => { el.style.transitionDelay = (i % 4) * 90 + "ms"; io.observe(el); }); } else els.forEach(el => el.classList.add("in"));
})();
// ===== Histoire : le logo se construit au fil du défilement =====
(function () {
  const st = document.querySelector(".story"); if (!st) return;
  const chs = [...st.querySelectorAll(".chap")], cap = document.getElementById("story-cap"), cnt = document.getElementById("story-count"), fill = document.getElementById("story-fill");
  const anns = {}; st.querySelectorAll("[data-ann]").forEach(a => anns[a.dataset.ann] = a);
  const ps = [...st.querySelectorAll("[data-p]")], core = st.querySelector("[data-core]"), slots = st.querySelector(".slots"), num = st.querySelector(".core-num");
  const reduce = matchMedia("(prefers-reduced-motion:reduce)").matches;
  const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v)), sm = x => x * x * (3 - 2 * x);
  const CAPS = ["Quatre pièces séparées", "Elles s'assemblent", "Le cœur s'allume", "Et de la place pour d'autres"];
  let lastCap = -1, ticking = false;
  function render(t) {
    ps.forEach(g => {
      const i = +g.dataset.p, s = sm(clamp((t - 0.12 * i) / 0.55)), k = 1 - s;
      g.setAttribute("transform", "translate(" + (+g.dataset.ox * k).toFixed(2) + " " + (+g.dataset.oy * k).toFixed(2) + ") rotate(" + (+g.dataset.rot * k).toFixed(2) + " " + g.dataset.cx + " " + g.dataset.cy + ")");
      g.style.opacity = (0.55 + 0.45 * s).toFixed(2);
    });
    const c = sm(clamp((t - 1.55) / 0.4)); core.setAttribute("transform", "scale(" + (0.01 + 0.99 * c).toFixed(3) + ")"); core.style.opacity = c.toFixed(2);
    slots.style.opacity = sm(clamp((t - 2.4) / 0.5)).toFixed(2);
    const win = (a, b, c, d) => sm(clamp((t - a) / (b - a))) * (1 - sm(clamp((t - c) / (d - c))));
    if (anns.dim) anns.dim.style.opacity = win(0.55, 0.9, 1.55, 1.9).toFixed(2);
    if (anns.lead) anns.lead.style.opacity = win(1.7, 2.0, 2.5, 2.85).toFixed(2);
    if (anns.open) anns.open.style.opacity = sm(clamp((t - 2.5) / 0.4)).toFixed(2);
    fill.style.transform = "scaleX(" + (t / 3).toFixed(3) + ")";
    const ci = Math.round(t);
    if (ci !== lastCap) { lastCap = ci; cap.textContent = CAPS[ci]; cnt.textContent = "0" + (ci + 1) + " / 04"; chs.forEach((el, i) => el.classList.toggle("on", i === ci)); }
  }
  function update() {
    ticking = false; const mid = innerHeight * 0.5, cs = chs.map(e => { const r = e.getBoundingClientRect(); return r.top + r.height / 2; });
    let t = 0;
    if (mid >= cs[cs.length - 1]) t = cs.length - 1; else if (mid > cs[0]) { for (let i = 0; i < cs.length - 1; i++) if (mid >= cs[i] && mid <= cs[i + 1]) { t = i + (mid - cs[i]) / (cs[i + 1] - cs[i]); break; } }
    render(t);
  }
  const req = () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } };
  if (reduce) { render(3); chs.forEach(c => c.classList.add("on")); return; }
  addEventListener("scroll", req, { passive: true }); addEventListener("resize", req); update();
})();

// ===== Pierre à l'édifice : le mur se bâtit au fil du texte =====
(function () {
  const wall = document.getElementById("wall"); if (!wall) return;
  const steps = [...document.querySelectorAll(".pstep")], wc = document.getElementById("wc");
  const reduce = matchMedia("(prefers-reduced-motion:reduce)").matches;
  const COLS = 8, ROWS = 6, RANGE = [[0, 7], [0, 6], [1, 6], [1, 5], [2, 5], [2, 4]];
  const NAMED = { "0-2": ["karl", 1, "#3D5AFE"], "0-3": ["taoufic", 1, "#FF5A4E"], "0-4": ["christiano", 1, "#1FC8A1"], "0-5": ["dolores", 1, "#9B6BFF"], "1-2": ["traceson", 2, "#FFB81C"], "1-3": ["fon", 3, "#1FC8A1", "wip"], "1-4": ["dossou", 3, "#B79CFF"], "2-3": ["libre", 4, "#FFB81C", "open"], "2-4": ["libre", 4, "#FFB81C", "open"], "3-3": ["libre", 4, "#FFB81C", "open"] };
  let stones = [], cur = 0;
  function build() {
    wall.innerHTML = ""; stones = []; const W = wall.clientWidth, w = W / (COLS + 0.5), h = w * 1.1547, rowH = h * 0.75;
    wall.style.height = (rowH * (ROWS - 1) + h) + "px"; wall.style.setProperty("--w", w + "px");
    for (let r = 0; r < ROWS; r++) {
      for (let c = RANGE[r][0]; c <= RANGE[r][1]; c++) {
        const nm = NAMED[r + "-" + c], el = document.createElement("span");
        const step = nm ? nm[1] : (r === 0 ? 1 : 4);
        el.className = "stone " + (nm ? "named" + (nm[3] ? " " + nm[3] : "") : (r === 0 ? "base" : "empty"));
        el.style.width = w + "px"; el.style.height = h + "px"; el.style.left = (c * w + (r % 2 ? w / 2 : 0)) + "px"; el.style.top = ((ROWS - 1 - r) * rowH) + "px";
        if (nm) { el.style.setProperty("--c", nm[2]); el.dataset.k = nm[0]; }
        wall.appendChild(el); stones.push({ el, step, r, c, named: !!nm, key: nm && nm[0], color: nm ? nm[2] : "#2a2e57", x: c * w + (r % 2 ? w / 2 : 0) + w / 2, y: (ROWS - 1 - r) * rowH + h / 2 });
      }
    }
    apply(cur, false);
  }
  function ring(s) { const i = document.createElement("i"); i.className = "ring"; i.style.left = s.x + "px"; i.style.top = s.y + "px"; i.style.setProperty("--c", s.color); wall.appendChild(i); setTimeout(() => i.remove(), 1300); }
  function apply(i, animate) {
    cur = i; let n = 0, order = 0, count = 0;
    stones.forEach(s => {
      const on = s.step <= i && i > 0, was = s.el.classList.contains("laid");
      if (s.named && s.key !== "libre" && on) count++;
      if (on && !was) { s.el.style.setProperty("--ld", (reduce || !animate ? 0 : order++ * 130) + "ms"); s.el.classList.add("laid"); if (animate && !reduce && (s.named || s.r === 0)) setTimeout(() => ring(s), order * 130 + 650); }
      else if (!on && was) { s.el.style.setProperty("--ld", "0ms"); s.el.classList.remove("laid"); }
      s.el.classList.toggle("cur", s.named && s.step === i);
    });
    if (wc) wc.textContent = count;
    steps.forEach((el, k) => el.classList.toggle("on", k === i - 1));
  }
  function update() {
    const mid = innerHeight * 0.55; let idx = 0; steps.forEach((el, k) => { if (el.getBoundingClientRect().top <= mid) idx = k + 1; });
    if (idx !== cur) apply(idx, true);
  }
  let tk = false; const req = () => { if (!tk) { tk = true; requestAnimationFrame(() => { tk = false; update(); }); } };
  build(); if (reduce) apply(4, false); else { addEventListener("scroll", req, { passive: true }); update(); }
  let rt; addEventListener("resize", () => { clearTimeout(rt); rt = setTimeout(() => { build(); }, 150); });
  wall.addEventListener("click", e => { const t = e.target.closest(".named"); if (!t) return; const s = stones.find(x => x.el === t); if (s) steps[s.step - 1].scrollIntoView({ behavior: "smooth", block: "center" }); });
})();
