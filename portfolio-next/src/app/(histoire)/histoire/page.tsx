import { fragment } from "@/lib/fragment";
import { EmblemDefs } from "@/components/Emblem";
import Header from "@/components/Header";
import Footer from "@/components/Footer";
import Progress from "@/components/Progress";
import Reveal from "@/components/Reveal";
import HistoireBehaviors from "@/components/HistoireBehaviors";

export default function Histoire() {
  return (
    <>
      <a className="skip" href="#contenu">Aller au contenu</a>
      <Progress />
      <Header page="histoire" />
      <EmblemDefs />
      <main id="contenu" dangerouslySetInnerHTML={{ __html: fragment("histoire.html") }} />
      <Footer />
      <Reveal />
      <HistoireBehaviors />
    </>
  );
}
