// Booking workflow: choose a path, then step through the form.
// Without JS every step and every form shows, so it still works.
(function () {
  var page = document.querySelector('.book-body');
  if (!page) return;
  document.documentElement.classList.add('js-booking');

  var chooser = document.getElementById('chooser');
  var panels = Array.prototype.slice.call(document.querySelectorAll('.path-panel'));

  function showPath() {
    var key = (location.hash || '').replace('#', '');
    var found = false;
    panels.forEach(function (p) {
      var on = p.getAttribute('data-panel') === key;
      p.hidden = !on;
      if (on) found = true;
    });
    chooser.hidden = found;
    window.scrollTo(0, 0);
    if (found) {
      var h = document.querySelector('#path-' + key + ' h2');
      if (h) { h.setAttribute('tabindex', '-1'); h.focus(); }
    }
  }
  document.querySelectorAll('.path-card').forEach(function (a) {
    a.setAttribute('href', '#' + a.getAttribute('data-path'));
  });
  document.querySelectorAll('.js-change-path').forEach(function (a) {
    a.addEventListener('click', function (e) { e.preventDefault(); history.pushState('', '', location.pathname); showPath(); });
  });
  window.addEventListener('hashchange', showPath);
  window.addEventListener('popstate', showPath);

  // Show/hide follow-up questions (e.g. NDIS details)
  function syncReveals(form) {
    form.querySelectorAll('.reveal').forEach(function (block) {
      var trigger = form.querySelector('input[data-reveal="' + block.id + '"]');
      var on = !!(trigger && trigger.checked);
      block.hidden = !on;
      block.querySelectorAll('input,select,textarea').forEach(function (el) { el.disabled = !on; });
    });
  }

  function labelFor(field) {
    var l = field.querySelector('legend, label');
    return l ? l.textContent.replace('*', '').trim() : '';
  }

  function valueOf(field) {
    var els = field.querySelectorAll('input,select,textarea');
    var vals = [];
    els.forEach(function (el) {
      if (el.disabled) return;
      if ((el.type === 'radio' || el.type === 'checkbox')) { if (el.checked) vals.push(el.value); }
      else if (el.type === 'file') { if (el.files && el.files[0]) vals.push(el.files[0].name); }
      else if (el.value) { vals.push(el.type === 'date' ? el.value.split('-').reverse().join('/') : el.value); }
    });
    return vals.join(', ');
  }

  document.querySelectorAll('.booking-form').forEach(function (form) {
    var steps = Array.prototype.slice.call(form.querySelectorAll('.step'));
    var back = form.querySelector('.js-back');
    var next = form.querySelector('.js-next');
    var submit = form.querySelector('.js-submit');
    var bar = form.querySelector('.progress span');
    var count = form.querySelector('.step-count');
    var i = 0;

    form.addEventListener('change', function () { syncReveals(form); });
    syncReveals(form);

    function render() {
      steps.forEach(function (s, n) { s.hidden = n !== i; });
      back.hidden = i === 0;
      next.hidden = i === steps.length - 1;
      submit.hidden = i !== steps.length - 1;
      bar.style.width = Math.round(((i + 1) / steps.length) * 100) + '%';
      count.textContent = 'Step ' + (i + 1) + ' of ' + steps.length;
      if (i === steps.length - 1) buildSummary();
    }

    function valid(stepEl) {
      var els = stepEl.querySelectorAll('input,select,textarea');
      for (var k = 0; k < els.length; k++) {
        var el = els[k];
        if (el.disabled || el.closest('[hidden]')) continue;
        if (!el.checkValidity()) { el.reportValidity(); el.focus(); return false; }
      }
      return true;
    }

    function buildSummary() {
      var dl = form.querySelector('.summary');
      dl.innerHTML = '';
      steps.slice(0, -1).forEach(function (s) {
        s.querySelectorAll('.fields > .field, .fields > .reveal .field').forEach(function (field) {
          if (field.closest('[hidden]') && !field.closest('.step')) return;
          if (field.closest('.reveal') && field.closest('.reveal').hidden) return;
          var v = valueOf(field);
          if (!v) return;
          var dt = document.createElement('dt'); dt.textContent = labelFor(field);
          var dd = document.createElement('dd'); dd.textContent = v;
          dl.appendChild(dt); dl.appendChild(dd);
        });
      });
    }

    next.addEventListener('click', function () {
      if (!valid(steps[i])) return;
      i = Math.min(i + 1, steps.length - 1); render();
      form.scrollIntoView({ behavior: 'smooth', block: 'start' });
      var first = steps[i].querySelector('input:not([type=hidden]),select,textarea');
      if (first && i < steps.length - 1) first.focus({ preventScroll: true });
    });
    back.addEventListener('click', function () { i = Math.max(i - 1, 0); render(); form.scrollIntoView({ block: 'start' }); });
    form.addEventListener('submit', function (e) {
      if (!valid(steps[i])) { e.preventDefault(); }
    });
    render();
  });

  showPath();
})();
