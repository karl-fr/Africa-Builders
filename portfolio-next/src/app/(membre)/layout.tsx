import type { Metadata, Viewport } from "next";
import "../globals.css";

export const metadata: Metadata = {
  metadataBase: new URL(process.env.NEXT_PUBLIC_SITE_URL || "http://localhost:3000"),
  icons: { icon: "/assets/favicon.svg" },
};

export const viewport: Viewport = { themeColor: "#12142B" };

export default function Layout({ children }: { children: React.ReactNode }) {
  return <html lang="fr"><body className="membre">{children}</body></html>;
}
