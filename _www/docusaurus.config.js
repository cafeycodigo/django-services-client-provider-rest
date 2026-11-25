const {themes} = require('prism-react-renderer');

module.exports = {
  title: 'Integración de sistemas',
  tagline: 'Laboratorio de Django, HTTP y React',
  url: process.env.DOCUSAURUS_URL || 'http://localhost:8088',
  baseUrl: `${(process.env.DOCUSAURUS_BASE_PATH || '').replace(/\/+$/, '')}/`,
  onBrokenLinks: 'throw',
  i18n: {defaultLocale: 'es', locales: ['es']},
  presets: [
    ['classic', {
      docs: {routeBasePath: '/', sidebarPath: require.resolve('./sidebars.js')},
      blog: false,
    }],
  ],
  themeConfig: {
    navbar: {title: 'Integración de sistemas'},
    prism: {theme: themes.github, darkTheme: themes.dracula, additionalLanguages: ['python', 'powershell']},
  },
};
