const {themes} = require('prism-react-renderer');

module.exports = {
  title: 'Integración de sistemas',
  tagline: 'Laboratorio de Django, HTTP y React',
  url: 'http://localhost:8088',
  baseUrl: '/',
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
