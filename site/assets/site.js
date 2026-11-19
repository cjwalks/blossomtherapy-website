// Mobile menu
document.addEventListener('DOMContentLoaded', function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Get started picker (tabs)
  var tabs = document.querySelectorAll('.picker [role="tab"]');
  tabs.forEach(function (tab) {
    tab.addEventListener('click', function () { select(tab); });
    tab.addEventListener('keydown', function (e) {
      var list = Array.prototype.slice.call(tabs);
      var i = list.indexOf(tab);
      if (e.key === 'ArrowRight') { e.preventDefault(); select(list[(i + 1) % list.length], true); }
      if (e.key === 'ArrowLeft') { e.preventDefault(); select(list[(i - 1 + list.length) % list.length], true); }
    });
  });
  function select(tab, focus) {
    tabs.forEach(function (t) {
      var on = t === tab;
      t.setAttribute('aria-selected', on ? 'true' : 'false');
      t.tabIndex = on ? 0 : -1;
      document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
    });
    if (focus) tab.focus();
  }

  // Open the right tab from a link like /#get-started?referrer
  var hash = window.location.hash;
  if (hash.indexOf('#start-') === 0) {
    var t = document.getElementById('tab-' + hash.replace('#start-', ''));
    if (t) { select(t); }
  }
});

// Instagram posts: load Instagram's embed script only when the section is near the screen
(function () {
  var box = document.querySelector('[data-insta]');
  if (!box) return;
  function load() {
    if (window.__igLoaded) return; window.__igLoaded = true;
    var s = document.createElement('script'); s.async = true; s.src = 'https://www.instagram.com/embed.js';
    document.body.appendChild(s);
  }
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (e) { if (e[0].isIntersecting) { load(); io.disconnect(); } }, { rootMargin: '400px' });
    io.observe(box);
  } else { load(); }
})();
