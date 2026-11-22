(function () {
  'use strict';

  // ---------------------------------------------------------------------
  // Sticky / compact header on scroll
  // ---------------------------------------------------------------------
  var header = document.getElementById('site-header');
  if (header) {
    var onScroll = function () {
      if (window.scrollY > 24) {
        header.classList.add('is-scrolled');
      } else {
        header.classList.remove('is-scrolled');
      }
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // ---------------------------------------------------------------------
  // Desktop mega-menu (click-to-open, closes on outside click / Escape)
  // ---------------------------------------------------------------------
  var menuTriggers = document.querySelectorAll('[data-megamenu-trigger]');
  function closeAllMegaMenus(except) {
    menuTriggers.forEach(function (trigger) {
      if (trigger === except) return;
      trigger.setAttribute('aria-expanded', 'false');
      var panelId = trigger.getAttribute('aria-controls');
      var panel = panelId ? document.getElementById(panelId) : null;
      if (panel) panel.classList.add('hidden');
    });
  }
  menuTriggers.forEach(function (trigger) {
    trigger.addEventListener('click', function (e) {
      e.preventDefault();
      var expanded = trigger.getAttribute('aria-expanded') === 'true';
      closeAllMegaMenus(trigger);
      trigger.setAttribute('aria-expanded', String(!expanded));
      var panelId = trigger.getAttribute('aria-controls');
      var panel = panelId ? document.getElementById(panelId) : null;
      if (panel) panel.classList.toggle('hidden', expanded);
    });
  });
  document.addEventListener('click', function (e) {
    if (!e.target.closest('[data-megamenu-wrapper]')) closeAllMegaMenus();
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeAllMegaMenus();
  });

  // ---------------------------------------------------------------------
  // Mobile full-screen nav
  // ---------------------------------------------------------------------
  var mobileToggle = document.getElementById('mobile-nav-toggle');
  var mobileNav = document.getElementById('mobile-nav');
  if (mobileToggle && mobileNav) {
    mobileToggle.addEventListener('click', function () {
      var isOpen = mobileNav.classList.toggle('open');
      mobileToggle.setAttribute('aria-expanded', String(isOpen));
      document.body.classList.toggle('overflow-hidden', isOpen);
    });
    mobileNav.querySelectorAll('[data-mobile-submenu-toggle]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var submenu = btn.nextElementSibling;
        var expanded = btn.getAttribute('aria-expanded') === 'true';
        btn.setAttribute('aria-expanded', String(!expanded));
        if (submenu) submenu.classList.toggle('hidden', expanded);
      });
    });
  }

  // ---------------------------------------------------------------------
  // Cookie consent banner
  // ---------------------------------------------------------------------
  var COOKIE_KEY = 'vaultreck_cookie_consent';
  var banner = document.getElementById('cookie-banner');
  if (banner) {
    var stored = null;
    try { stored = localStorage.getItem(COOKIE_KEY); } catch (err) { /* ignore */ }
    if (!stored) banner.classList.remove('hidden');

    function setConsent(value) {
      try { localStorage.setItem(COOKIE_KEY, value); } catch (err) { /* ignore */ }
      banner.classList.add('hidden');
      var settingsPanel = document.getElementById('cookie-settings-panel');
      if (settingsPanel) settingsPanel.classList.add('hidden');
    }

    var acceptBtn = document.getElementById('cookie-accept');
    var rejectBtn = document.getElementById('cookie-reject');
    var settingsBtn = document.getElementById('cookie-settings-toggle');
    var settingsPanel = document.getElementById('cookie-settings-panel');
    var settingsSave = document.getElementById('cookie-settings-save');

    if (acceptBtn) acceptBtn.addEventListener('click', function () { setConsent('accepted'); });
    if (rejectBtn) rejectBtn.addEventListener('click', function () { setConsent('rejected-non-essential'); });
    if (settingsBtn && settingsPanel) {
      settingsBtn.addEventListener('click', function () {
        settingsPanel.classList.toggle('hidden');
      });
    }
    if (settingsSave) settingsSave.addEventListener('click', function () { setConsent('custom'); });
  }

  // ---------------------------------------------------------------------
  // Multi-step "Report a Fraud" form
  // ---------------------------------------------------------------------
  var wizard = document.getElementById('fraud-wizard');
  if (wizard) {
    var steps = Array.prototype.slice.call(wizard.querySelectorAll('[data-step]'));
    var dots = Array.prototype.slice.call(wizard.querySelectorAll('[data-step-indicator]'));
    var currentStep = 0;

    function showStep(index) {
      steps.forEach(function (step, i) {
        step.classList.toggle('hidden', i !== index);
      });
      dots.forEach(function (dot, i) {
        dot.classList.toggle('bg-cargo-500', i <= index);
        dot.classList.toggle('text-ink-950', i <= index);
        dot.classList.toggle('bg-ink-950/10', i > index);
        dot.classList.toggle('text-ink-950/40', i > index);
      });
      wizard.querySelectorAll('[data-progress-fill]').forEach(function (fill) {
        fill.style.width = (index / (steps.length - 1)) * 100 + '%';
      });
      currentStep = index;
      wizard.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    function validateStep(index) {
      var step = steps[index];
      var requiredFields = step.querySelectorAll('[required]');
      var valid = true;
      requiredFields.forEach(function (field) {
        if (!field.checkValidity()) {
          field.reportValidity();
          valid = false;
        }
      });
      return valid;
    }

    wizard.querySelectorAll('[data-step-next]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        if (!validateStep(currentStep)) return;
        if (currentStep < steps.length - 1) showStep(currentStep + 1);
      });
    });
    wizard.querySelectorAll('[data-step-prev]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        if (currentStep > 0) showStep(currentStep - 1);
      });
    });

    var form = wizard.querySelector('form');
    if (form) {
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        if (!validateStep(currentStep)) return;

        // ------------------------------------------------------------
        // PLACEHOLDER: no backend is wired up yet. Replace this block
        // with a real fetch()/POST to your case-intake API endpoint,
        // e.g.:
        //   fetch('/api/case-intake/', { method: 'POST', body: new FormData(form) })
        //     .then(...)
        // ------------------------------------------------------------

        form.classList.add('hidden');
        var confirmation = document.getElementById('fraud-wizard-confirmation');
        if (confirmation) confirmation.classList.remove('hidden');
        var progress = document.getElementById('fraud-wizard-progress');
        if (progress) progress.classList.add('hidden');
      });
    }

    showStep(0);
  }

  // ---------------------------------------------------------------------
  // Insights hub category filter
  // ---------------------------------------------------------------------
  var filterBar = document.getElementById('insights-filter');
  if (filterBar) {
    var cards = document.querySelectorAll('[data-insight-category]');
    filterBar.querySelectorAll('[data-filter]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        var value = btn.getAttribute('data-filter');
        filterBar.querySelectorAll('[data-filter]').forEach(function (b) {
          b.classList.remove('bg-ink-950', 'text-white');
          b.classList.add('bg-transparent', 'text-ink-950');
        });
        btn.classList.add('bg-ink-950', 'text-white');
        btn.classList.remove('bg-transparent', 'text-ink-950');
        cards.forEach(function (card) {
          var show = value === 'all' || card.getAttribute('data-insight-category') === value;
          card.style.display = show ? '' : 'none';
        });
      });
    });
  }
})();
