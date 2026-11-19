// Nid d'abeille du héro : tracé calculé une fois côté serveur.
export function hiveSvg(): string {
  const S3 = Math.sqrt(3), R = 54; let d = "";
  const hex = (cx: number, cy: number) => {
    const p: string[] = [];
    for (let k = 0; k < 6; k++) { const a = (Math.PI / 180) * (30 + 60 * k); p.push((cx + R * Math.cos(a)).toFixed(1) + " " + (cy + R * Math.sin(a)).toFixed(1)); }
    return "M" + p.join("L") + "Z";
  };
  for (let y = -1; y < 9; y++) for (let x = -1; x < 16; x++) d += hex(x * S3 * R + (y % 2 ? (S3 * R) / 2 : 0), y * 1.5 * R);
  return `<svg class="hive" viewBox="0 0 1200 700" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><path d="${d}" fill="none" stroke="#2a2e57" stroke-width="1.6"/></svg>`;
}
