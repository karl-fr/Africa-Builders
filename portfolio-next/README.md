# Portfolio Africa Builders (Next.js + MySQL)

Next.js 15 (App Router) · Prisma · MySQL/MariaDB · hébergement Vercel.
Le contenu (profils, contributions, projets, coordonnées) vit dans la base ; les messages du formulaire y sont enregistrés.

## 1. En local avec XAMPP ou WAMP

1. Démarrez **MySQL** dans XAMPP/WAMP (port 3306, utilisateur `root`, sans mot de passe par défaut).
2. Dans ce dossier :
   ```bash
   npm install
   cp .env.example .env        # sous Windows : copy .env.example .env
   npm run db:setup            # crée la base africa_builders, les tables, puis le contenu
   npm run dev                 # http://localhost:3000
   ```
3. Modifier le contenu : phpMyAdmin (livré avec XAMPP/WAMP) ou `npm run db:studio`.
   - Tables `Member`, `Contribution`, `Fact`, `Source`, `Project`, `ProjectStep` : textes du site.
   - Table `Link` : réseaux d'un membre (`kind` = linkedin, instagram, youtube, kaggle, zindi, portfolio). Ligne absente = bouton grisé « bientôt ».
   - Table `Setting` : `email`, `github`, `linkedin`, `instagram` (vide = bouton masqué).
   - Table `Message` : messages reçus par le formulaire.
   - Les pages se rafraîchissent seules toutes les 5 minutes (`revalidate = 300`).
4. Photo d'un membre : déposer `nom.jpg` (carré, ~520×520) dans `public/assets/photos/` et renseigner `Member.photo`.

> `npm run db:seed` remet le contenu éditorial à l'état du dépôt (les réseaux saisis et les messages sont conservés).

## Partager le site temporairement (Cloudflare)

```bash
npm run share      # ou ./share.sh 3000
```
Construit le site, le lance et affiche une adresse `https://….trycloudflare.com` à envoyer. Elle disparaît à l'arrêt (Ctrl+C). Nécessite `cloudflared` et MySQL démarré.

## 2. Mise en ligne sur Vercel

Vercel ne peut pas joindre le MySQL de votre PC : il faut une **base MySQL hébergée** (offres gratuites : TiDB Cloud Serverless, Aiven, Railway…).

1. Créez la base chez le fournisseur et copiez l'URL de connexion :
   `mysql://UTILISATEUR:MOTDEPASSE@HOTE:PORT/africa_builders?sslaccept=strict`
2. Créez les tables et le contenu **une fois**, depuis votre PC, vers cette base :
   ```bash
   DATABASE_URL="mysql://..." npm run db:setup      # Windows PowerShell : $env:DATABASE_URL="mysql://..."; npm run db:setup
   ```
3. Poussez le dossier sur GitHub, puis sur vercel.com : *Add New → Project → importer le dépôt*.
4. Variables d'environnement du projet Vercel :
   - `DATABASE_URL` : l'URL de l'étape 1 (obligatoire, aussi pour le build)
   - `NEXT_PUBLIC_SITE_URL` : l'adresse finale, ex. `https://africa-builders.vercel.app` (aperçus sur les réseaux)
5. *Deploy*. Les anciennes adresses `.html` redirigent vers les nouvelles.

## Structure

- `src/app/(home)`, `(histoire)`, `(membre)` : trois groupes de pages, chacun avec sa balise `<body>` (le style du site en dépend).
- `src/app/api/contact` : enregistre les messages (champ piège anti-spam, 3 messages / 10 min / IP).
- `src/components` : en-tête, onglets de projets, collaborations (React) ; `*Behaviors` = animations au défilement portées du site statique.
- `src/fragments` : blocs HTML/SVG statiques (héro, histoire, schémas de projets).
- `prisma/schema.prisma` et `prisma/seed.ts` : modèle de données et contenu initial.
