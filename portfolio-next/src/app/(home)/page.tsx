import { fragment } from "@/lib/fragment";
import { getContact, getMembers, getProjects, photoUrl } from "@/lib/data";
import { EmblemDefs, BigMark } from "@/components/Emblem";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Progress from "@/components/Progress";
import Reveal from "@/components/Reveal";
import { hiveSvg } from "@/lib/hive";
import HeroBehaviors from "@/components/HeroBehaviors";
import ProjectTabs, { type ProjectView } from "@/components/ProjectTabs";
import Collaborations from "@/components/Collaborations";
import ContactForm from "@/components/ContactForm";

export const revalidate = 300; // le contenu vient de la base : rafraîchi toutes les 5 minutes

export default async function Home() {
  const [members, projects, contact] = await Promise.all([getMembers(), getProjects(), getContact()]);
  const team = members.filter((m) => m.role === "MEMBER");
  const collabs = members.filter((m) => m.role === "COLLABORATOR");

  const views: ProjectView[] = projects.map((p) => ({
    slug: p.slug, name: p.name, tag: p.tag, status: p.status, tagline: p.tagline, lead: p.lead,
    paragraphs: p.paragraphs.split("\n").filter(Boolean), linkLabel: p.linkLabel, linkUrl: p.linkUrl,
    chips: (p.chips ?? "").split("\n").filter(Boolean), stageTitle: p.stageTitle, stageNote: p.stageNote,
    steps: p.steps.map((s) => ({ title: s.title, text: s.text })),
    stageSvg: (() => { try { return fragment(`stage-${p.slug}.html`); } catch { return ""; } })(),
  }));

  const links: [string, string, string][] = [
    ["email", "Écrire un mail", contact.email ? "mailto:" + contact.email : ""],
    ["github", "GitHub", contact.github], ["linkedin", "LinkedIn", contact.linkedin], ["instagram", "Instagram", contact.instagram],
  ];
  const shown = links.filter(([, , href]) => href);
  const hero = fragment("hero.html").replace(/<svg class="hive"[^>]*><\/svg>/, hiveSvg());

  return (
    <>
      <a className="skip" href="#contenu">Aller au contenu</a>
      <Progress />
      <Header page="home" />
      <EmblemDefs />
      <main id="contenu">
        <div dangerouslySetInnerHTML={{ __html: hero + fragment("band.html") + fragment("teaser.html") }} style={{ display: "contents" }} />

        <section className="sec light" id="projets" aria-labelledby="t-projets">
          <div className="wrap">
            <p className="kick">NOS PROJETS</p>
            <h2 id="t-projets" className="reveal">Ce que nous construisons.</h2>
            <ProjectTabs projects={views} />
          </div>
        </section>

        <section className="sec ink" id="equipe" aria-labelledby="t-eq">
          <div className="wrap">
            <p className="kick">ÉQUIPE</p>
            <h2 id="t-eq" className="reveal">Les quatre bâtisseurs.</h2>
            <p className="eq-p reveal">Quatre profils différents qui se complètent. Cliquez sur l&apos;un d&apos;eux pour le découvrir.</p>
            <ul className="team">
              {team.map((m) => {
                const img = photoUrl(m.photo);
                const st = { ["--c" as string]: m.color, ...(img ? { ["--img" as string]: `url(${img})`, ["--pos" as string]: m.photoPos } : {}) } as React.CSSProperties;
                return (
                  <li className="reveal" key={m.slug}>
                    <a className="mlink" href={`/membres/${m.slug}`} data-vt={m.slug}>
                      <span className={"hx" + (img ? " has" : "")} style={st}>{m.initials}</span>
                      <b>{m.name}</b><small>Voir le profil →</small>
                    </a>
                  </li>
                );
              })}
            </ul>
          </div>
        </section>

        <section className="sec collab2" id="collaborations" aria-labelledby="t-col">
          <Collaborations collabs={collabs.map((c) => ({ slug: c.slug, name: c.name, initials: c.initials, color: c.color, text: c.extra ?? c.bio, photoUrl: photoUrl(c.photo) }))} />
        </section>

        <section className="sec cta" id="contact" aria-labelledby="t-ct">
          <div className="wrap narrow">
            <BigMark />
            <h2 id="t-ct">Un projet à construire&nbsp;?</h2>
            <p>Un hackathon, un défi, une collaboration, une démonstration : écrivez-nous. Nous aimons construire avec d&apos;autres.</p>
            <ContactForm />
            <div className="contact" id="contact-links">
              {shown.map(([k, label, href]) => (
                <a key={k} href={href} {...(k !== "email" ? { target: "_blank", rel: "noopener" } : {})}>{label}</a>
              ))}
            </div>
          </div>
        </section>
      </main>
      <Footer />
      <Reveal />
      <HeroBehaviors />
    </>
  );
}
