import type { Metadata, Viewport } from "next";
import "../globals.css";

const site = process.env.NEXT_PUBLIC_SITE_URL || "http://localhost:3000";
export const metadata: Metadata = {
  metadataBase: new URL(site),
  title: "Africa Builders · Réunis par hasard, restés par choix",
  description: "Africa Builders : quatre étudiants à Epitech réunis par hasard pour un hackathon et restés ensemble par choix. 3e place au Hackathon IA & Musique, SIMA 2026.",
  icons: { icon: "/assets/favicon.svg", apple: "/assets/apple-touch-icon.png" },
  openGraph: { type: "website", title: "Africa Builders", description: "Réunis par hasard pour un hackathon, restés ensemble par choix. 3e place au Hackathon IA & Musique, SIMA 2026.", images: ["/assets/og.png"] },
  twitter: { card: "summary_large_image" },
};

export const viewport: Viewport = { themeColor: "#12142B" };

export default function Layout({ children }: { children: React.ReactNode }) {
  return <html lang="fr"><body>{children}</body></html>;
}
