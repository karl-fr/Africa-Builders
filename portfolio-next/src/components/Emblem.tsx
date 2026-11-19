// Emblème : 4 pièces (les membres) + cœur doré (l'idée). Défini une fois, réutilisé par <use>.
export function EmblemDefs() {
  return (
    <svg width="0" height="0" style={{ position: "absolute" }} aria-hidden="true">
      <defs>
        <g id="emblem">
          <g fill="none" strokeWidth="26" strokeMiterlimit="10">
            <path className="p1" d="M-52 -86.6 L-100 0 L-52 86.6" stroke="#3D5AFE" />
            <path className="p2" d="M52 -86.6 L100 0 L52 86.6" stroke="#FF5A4E" />
          </g>
          <path className="p3" d="M-34 -86.6 H34" stroke="#1FC8A1" strokeWidth="26" />
          <path className="p4" d="M-34 86.6 H34" stroke="#9B6BFF" strokeWidth="26" />
          <path className="core" d="M34 0 L17 29.4 L-17 29.4 L-34 0 L-17 -29.4 L17 -29.4 Z" fill="#FFB81C" stroke="#FFB81C" strokeWidth="6" strokeLinejoin="round" />
        </g>
      </defs>
    </svg>
  );
}

export function LogoSmall() {
  return (
    <svg className="lg" viewBox="-122 -104 244 208" aria-hidden="true">
      <g fill="none" strokeWidth="26" strokeMiterlimit="10">
        <path d="M-52 -86.6 L-100 0 L-52 86.6" stroke="#3D5AFE" />
        <path d="M52 -86.6 L100 0 L52 86.6" stroke="#FF5A4E" />
      </g>
      <path d="M-34 -86.6 H34" stroke="#1FC8A1" strokeWidth="26" />
      <path d="M-34 86.6 H34" stroke="#9B6BFF" strokeWidth="26" />
      <path d="M34 0 L17 29.4 L-17 29.4 L-34 0 L-17 -29.4 L17 -29.4 Z" fill="#FFB81C" stroke="#FFB81C" strokeWidth="6" strokeLinejoin="round" />
    </svg>
  );
}

export function BigMark({ className = "mk big" }: { className?: string }) {
  return (
    <svg className={className} viewBox="-122 -104 244 208" aria-hidden="true">
      <use href="#emblem" />
    </svg>
  );
}
