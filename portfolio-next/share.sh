#!/usr/bin/env bash
# Partage temporaire du site via un tunnel Cloudflare (adresse https://....trycloudflare.com).
# Usage : ./share.sh [port]      Arrêt : Ctrl+C (le site et le tunnel s'arrêtent ensemble).
set -euo pipefail
cd "$(dirname "$0")"
PORT="${1:-3000}"

command -v cloudflared >/dev/null || { echo "cloudflared est introuvable. Installation : https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/downloads/"; exit 1; }
[ -f .env ] || { echo "Fichier .env manquant : copiez .env.example en .env puis lancez MySQL (XAMPP/WAMP)."; exit 1; }
[ -d node_modules ] || npm install

# version de production (plus rapide et plus fiable à partager qu'un serveur de dev)
npm run build
LOG="$(mktemp)"
PORT="$PORT" npm run start -- -p "$PORT" >/dev/null 2>&1 &
SITE=$!
cleanup() { kill "$SITE" "${TUN:-}" 2>/dev/null || true; rm -f "$LOG"; }
trap cleanup EXIT INT TERM

for _ in $(seq 1 40); do curl -fs "http://localhost:$PORT" >/dev/null && break; sleep 0.5; done
curl -fs "http://localhost:$PORT" >/dev/null || { echo "Le site ne démarre pas (la base MySQL est-elle lancée ?)."; exit 1; }

cloudflared tunnel --no-autoupdate --url "http://localhost:$PORT" >"$LOG" 2>&1 &
TUN=$!
URL=""
for _ in $(seq 1 40); do
  URL="$(grep -o 'https://[a-z0-9-]*\.trycloudflare\.com' "$LOG" | head -1 || true)"
  [ -n "$URL" ] && break; sleep 0.5
done
[ -n "$URL" ] || { echo "Tunnel indisponible :"; cat "$LOG"; exit 1; }

echo
echo "  Site partagé : $URL"
echo "  (adresse temporaire, valable tant que ce script tourne ; Ctrl+C pour arrêter)"
echo
wait "$TUN"
