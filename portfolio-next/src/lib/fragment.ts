import { readFileSync } from "node:fs";
import { join } from "node:path";

// Blocs HTML/SVG statiques (écrits par nous) lus au rendu serveur.
export function fragment(name: string): string {
  return readFileSync(join(process.cwd(), "src", "fragments", name), "utf8");
}
