/** @type {import('next').NextConfig} */
export default {
  poweredByHeader: false,
  async redirects() {
    // anciennes adresses du site statique
    return [
      { source: "/index.html", destination: "/", permanent: true },
      { source: "/histoire.html", destination: "/histoire", permanent: true },
      { source: "/membres/:slug.html", destination: "/membres/:slug", permanent: true },
    ];
  },
};
