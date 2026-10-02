/* Shared with career pages: textSize = normal/large/xl, theme = light/dark. */
(function () {
  'use strict';
  const root = document.documentElement;
  const system = window.matchMedia('(prefers-color-scheme: dark)');
  const get = key => { try { return localStorage.getItem(key); } catch { return null; } };
  const save = (key, value) => { try { localStorage.setItem(key, value); } catch {} };
  function size(value, persist = false) {
    value = ['large', 'xl'].includes(value) ? value : 'normal';
    root.dataset.textSize = value;
    document.body.classList.toggle('text-large', value === 'large');
    document.body.classList.toggle('text-xl', value === 'xl');
    document.querySelectorAll('.a11y-bar [data-text-size]').forEach(button => {
      button.setAttribute('aria-pressed', String(button.dataset.textSize === value));
    });
    if (persist) save('textSize', value);
  }
  function theme(value, persist = false) {
    value = ['light', 'dark'].includes(value) ? value : system.matches ? 'dark' : 'light';
    root.dataset.theme = value;
    document.getElementById('themeBtn').setAttribute('aria-pressed', String(value === 'dark'));
    if (persist) save('theme', value);
  }
  function restore() { size(get('textSize')); theme(get('theme')); }
  document.querySelectorAll('.a11y-bar [data-text-size]').forEach(button => {
    button.addEventListener('click', () => size(button.dataset.textSize, true));
  });
  document.getElementById('themeBtn').addEventListener('click', () => theme(root.dataset.theme === 'dark' ? 'light' : 'dark', true));
  system.addEventListener('change', () => theme(get('theme')));
  window.addEventListener('storage', event => { if (!event.key || ['theme', 'textSize'].includes(event.key)) restore(); });
  window.addEventListener('pageshow', restore);
  restore();
})();
