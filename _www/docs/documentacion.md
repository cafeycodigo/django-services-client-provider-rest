---
title: "13. Mantener la documentación"
sidebar_position: 15
---

_www usa Docusaurus en modo documentación. El contenido de `docs/` se convierte en páginas estáticas. La barra lateral se genera usando `sidebar_position` y el resaltado permite copiar los ejemplos.

```powershell
cd _www
npm install
npm start
# Generar el sitio estático en build/
npm run build
```

Para añadir un capítulo, crea un Markdown con título y posición, enlázalo desde la lección relacionada y agrega un ejemplo comprobable. Indica si el fragmento viene del repositorio o es una ampliación propuesta. El estilo usa el tema Classic de Docusaurus.
