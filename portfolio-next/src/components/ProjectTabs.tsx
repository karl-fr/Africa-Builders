"use client";
import { useEffect, useRef, useState } from "react";

export type ProjectView = {
  slug: string; name: string; tag: string; status: string; tagline: string; lead: string;
  paragraphs: string[]; linkLabel: string | null; linkUrl: string | null; chips: string[];
  stageTitle: string; stageNote: string; steps: { title: string; text: string }[]; stageSvg: string;
};

// Onglets de projets : un schéma animé en 3 étapes par projet, qui avance seul tant qu'il est visible.
export default function ProjectTabs({ projects }: { projects: ProjectView[] }) {
  const [tab, setTab] = useState(0);
  const [stage, setStage] = useState(0);
  const [locked, setLocked] = useState(false);
  const [visible, setVisible] = useState(false);
  const sec = useRef<HTMLDivElement>(null);
  const panes = useRef<(HTMLElement | null)[]>([]);

  useEffect(() => {
    const io = new IntersectionObserver((es) => es.forEach((e) => setVisible(e.isIntersecting)), { threshold: 0.3 });
    if (sec.current) io.observe(sec.current);
    return () => io.disconnect();
  }, []);

  useEffect(() => {
    if (locked || !visible || matchMedia("(prefers-reduced-motion:reduce)").matches) return;
    const t = setInterval(() => setStage((s) => (s + 1) % 3), 3600);
    return () => clearInterval(t);
  }, [locked, visible, tab]);

  useEffect(() => {
    panes.current[tab]?.querySelectorAll(".stg").forEach((g, k) => g.classList.toggle("on", k === stage));
  }, [tab, stage]);

  const select = (i: number) => { setTab(i); setStage(0); setLocked(false); };
  const keys = (e: React.KeyboardEvent, i: number) => {
    if (e.key !== "ArrowRight" && e.key !== "ArrowLeft") return;
    const n = (i + (e.key === "ArrowRight" ? 1 : projects.length - 1)) % projects.length;
    select(n); document.getElementById("tab-" + projects[n].slug)?.focus();
  };

  return (
    <div ref={sec}>
      <div className="ptabs" role="tablist" aria-label="Nos projets">
        {projects.map((p, i) => (
          <button key={p.slug} className={"ptab" + (i === tab ? " on" : "")} role="tab" id={"tab-" + p.slug}
            aria-controls={"pane-" + p.slug} aria-selected={i === tab} tabIndex={i === tab ? 0 : -1}
            onClick={() => select(i)} onKeyDown={(e) => keys(e, i)}>
            <span className={"pt-tag " + p.status}>{p.tag}</span><b>{p.name}</b><em>{p.tagline}</em>
          </button>
        ))}
      </div>
      <div className="panes">
        {projects.map((p, i) => (
          <article key={p.slug} ref={(el) => { panes.current[i] = el; }} className={"pane" + (i === tab ? " on" : "")}
            id={"pane-" + p.slug} role="tabpanel" aria-labelledby={"tab-" + p.slug} hidden={i !== tab}>
            <div className="pj-stage" aria-hidden="true">
              <span className="cm tl"></span><span className="cm tr"></span><span className="cm bl"></span><span className="cm br"></span>
              <div className="st-top"><span>{p.stageTitle}</span><span className="pj-count">{(i === tab ? stage : 0) + 1} / 3</span></div>
              <div dangerouslySetInnerHTML={{ __html: p.stageSvg }} />
              <div className="pj-bar"><i style={{ transform: `scaleX(${(((i === tab ? stage : 0) + 1) / 3).toFixed(3)})` }}></i></div>
              <p className="pj-note">{p.stageNote}</p>
            </div>
            <div className="pj-text">
              <p className="pj-lead">{p.lead}</p>
              {p.paragraphs.map((t, k) => <p key={k}>{t}</p>)}
              <ol className="psl">
                {p.steps.map((s, k) => (
                  <li key={k}>
                    <button type="button" className={"sb" + (k === stage ? " on" : "")} onClick={() => { setLocked(true); setStage(k); }}>
                      <b>{String(k + 1).padStart(2, "0")}</b><span><strong>{s.title}</strong><em>{s.text}</em></span>
                    </button>
                  </li>
                ))}
              </ol>
              {p.linkUrl && <a className="link" href={p.linkUrl} target="_blank" rel="noopener">{p.linkLabel}</a>}
              {p.chips.length > 0 && <ul className="chips">{p.chips.map((c, k) => <li key={k}>{c}</li>)}</ul>}
            </div>
          </article>
        ))}
      </div>
    </div>
  );
}
