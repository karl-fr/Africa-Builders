"use client";
import { useState } from "react";

// Formulaire : le message est enregistré dans la base (table Message).
export default function ContactForm() {
  const [state, setState] = useState<"idle" | "sending" | "ok" | "error">("idle");
  const [err, setErr] = useState("");

  async function submit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const form = e.currentTarget;
    const data = Object.fromEntries(new FormData(form)) as Record<string, string>;
    setState("sending"); setErr("");
    try {
      const r = await fetch("/api/contact", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(data) });
      const j = await r.json().catch(() => ({}));
      if (!r.ok) { setErr(j.error || "Une erreur est survenue. Réessayez dans un instant."); setState("error"); return; }
      form.reset(); setState("ok");
    } catch { setErr("Connexion impossible. Réessayez dans un instant."); setState("error"); }
  }

  if (state === "ok")
    return <p className="cf-ok" role="status">Merci, votre message est bien arrivé. Nous vous répondons vite.</p>;

  return (
    <form className="cform" onSubmit={submit} noValidate>
      <div className="cf-row">
        <label>Votre nom<input name="name" autoComplete="name" required maxLength={120} /></label>
        <label>Votre e-mail<input name="email" type="email" autoComplete="email" required maxLength={200} /></label>
      </div>
      <label>Votre message<textarea name="message" rows={5} required minLength={10} maxLength={4000} placeholder="Un défi, une idée, un projet à construire…" /></label>
      <input className="cf-hp" name="website" tabIndex={-1} autoComplete="off" aria-hidden="true" />
      <button className="cf-btn" disabled={state === "sending"}>{state === "sending" ? "Envoi…" : "Envoyer le message"}</button>
      {state === "error" && <p className="cf-err" role="alert">{err}</p>}
    </form>
  );
}
