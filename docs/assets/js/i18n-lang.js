/* ========================================================================
   i18n-lang.js
   Sincroniza <html lang> y <html dir> con el idioma activo del i18n.
   - Soporta RTL automático (ar, he, fa, ur)
   - Escucha eventos 'languageChanged' emitidos por i18n.js
   - Sincroniza entre pestañas vía storage events
   - Como red de seguridad, observa cambios en lang con MutationObserver
   ======================================================================== */
(function () {
  'use strict';

  var RTL_LANGS = ['ar', 'he', 'fa', 'ur'];
  var STORAGE_KEY = 'cdpn-lang';

  function getCurrentLang() {
    // Prioridad: localStorage > atributo lang ya puesto por i18n.js > 'es'
    try {
      var stored = localStorage.getItem(STORAGE_KEY);
      if (stored) return stored;
    } catch (e) { /* localStorage puede estar bloqueado */ }
    return (document.documentElement.lang || 'es');
  }

  function syncHtmlLang() {
    var lang = getCurrentLang().toLowerCase().split('-')[0];
    var root = document.documentElement;
    if (root.lang !== lang) root.lang = lang;
    var dir = RTL_LANGS.indexOf(lang) !== -1 ? 'rtl' : 'ltr';
    if (root.dir !== dir) root.dir = dir;
  }

  // Sync inicial
  syncHtmlLang();

  // i18n.js puede emitir este evento al cambiar idioma
  window.addEventListener('languageChanged', syncHtmlLang);
  window.addEventListener('cdpn:lang-changed', syncHtmlLang);

  // Sincronización entre pestañas
  window.addEventListener('storage', function (e) {
    if (e.key === STORAGE_KEY) syncHtmlLang();
  });

  // Red de seguridad: si algo cambia lang sin disparar el evento, lo detectamos
  if (typeof MutationObserver !== 'undefined') {
    new MutationObserver(syncHtmlLang).observe(document.documentElement, {
      attributes: true,
      attributeFilter: ['lang']
    });
  }
})();
