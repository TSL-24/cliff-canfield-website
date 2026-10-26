/* Purlin — site interactions */
(function () {
  'use strict';

  const header = document.querySelector('.site-header');
  const backToTop = document.getElementById('backToTop');
  const navCollapseEl = document.getElementById('mainNav');

  /* ---------- Header shadow + back-to-top visibility ---------- */
  function onScroll() {
    const y = window.scrollY;
    header.classList.toggle('scrolled', y > 10);
    backToTop.classList.toggle('show', y > 600);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  backToTop.addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  /* ---------- Close the mobile menu after choosing a link ---------- */
  if (navCollapseEl && window.bootstrap) {
    const collapse = bootstrap.Collapse.getOrCreateInstance(navCollapseEl, { toggle: false });
    navCollapseEl.addEventListener('show.bs.collapse', function () { header.classList.add('menu-open'); });
    navCollapseEl.addEventListener('hidden.bs.collapse', function () { header.classList.remove('menu-open'); });
    navCollapseEl.querySelectorAll('a').forEach(function (link) {
      if (link.classList.contains('dropdown-toggle')) return; // opening the Services menu shouldn't close the mobile nav
      link.addEventListener('click', function () {
        if (navCollapseEl.classList.contains('show')) collapse.hide();
      });
    });
  }

  /* ---------- Highlight the nav link for the section in view ---------- */
  const navLinks = Array.from(document.querySelectorAll('.navbar-nav .nav-link'));
  const sections = navLinks
    .map(function (l) {
      const href = l.getAttribute('href') || '';
      return href.charAt(0) === '#' && href.length > 1 ? document.querySelector(href) : null;
    })
    .filter(Boolean);

  if ('IntersectionObserver' in window) {
    const spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        navLinks.forEach(function (l) {
          if (l.getAttribute('aria-current') === 'page') return; // keep the current page highlighted
          l.classList.toggle('active', l.getAttribute('href') === '#' + entry.target.id);
        });
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    sections.forEach(function (s) { spy.observe(s); });
  }

  /* ---------- Service pages: highlight the "On this page" link for the section in view ---------- */
  const tocLinks = Array.from(document.querySelectorAll('.svc-toc a[href^="#"]'));
  if (tocLinks.length && 'IntersectionObserver' in window) {
    const tocSpy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        tocLinks.forEach(function (l) {
          l.classList.toggle('active', l.getAttribute('href') === '#' + entry.target.id);
        });
      });
    }, { rootMargin: '-30% 0px -60% 0px' });
    tocLinks.forEach(function (l) {
      const target = document.querySelector(l.getAttribute('href'));
      if (target) tocSpy.observe(target);
    });
  }

  /* ---------- Reveal-on-scroll ---------- */
  const revealTargets = document.querySelectorAll(
    '.service-card, .process-card, .about-card, .info-card, .why-item, .estimate-card, .consider-list, .work-tile, .area-card, .review-card, .faq-accordion, .cta-band, .section-title, .rating-band, .featured-review'
  );
  if ('IntersectionObserver' in window) {
    revealTargets.forEach(function (el) { el.classList.add('reveal'); });
    const revealer = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    revealTargets.forEach(function (el) { revealer.observe(el); });
  }

  /* ---------- Count-up for the "roofs installed" stat ---------- */
  const counter = document.querySelector('[data-count]');
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (counter && !reduceMotion) {
    const target = parseInt(counter.dataset.count, 10);
    const duration = 1400;
    const start = performance.now();
    (function tick(now) {
      const p = Math.min((now - start) / duration, 1);
      const eased = 1 - Math.pow(1 - p, 3);
      counter.textContent = Math.round(target * eased).toLocaleString('en-US');
      if (p < 1) requestAnimationFrame(tick);
    })(start);
  }

  /* ---------- Quote form (home page only) ---------- */
  const form = document.getElementById('quoteForm');
  if (form) {
    const formWrap = document.getElementById('quoteFormWrap');
    const success = document.getElementById('quoteSuccess');
    const phone = document.getElementById('phone');
    const zip = document.getElementById('zip');

    // Format phone as (512) 555-0142 while typing
    phone.addEventListener('input', function () {
      const digits = phone.value.replace(/\D/g, '').slice(0, 10);
      let out = digits;
      if (digits.length > 6) out = '(' + digits.slice(0, 3) + ') ' + digits.slice(3, 6) + '-' + digits.slice(6);
      else if (digits.length > 3) out = '(' + digits.slice(0, 3) + ') ' + digits.slice(3);
      else if (digits.length > 0) out = '(' + digits;
      phone.value = out;
    });

    // Digits only for ZIP
    zip.addEventListener('input', function () {
      zip.value = zip.value.replace(/\D/g, '').slice(0, 5);
    });

    // Live character count for the project details box
    const details = document.getElementById('projectDetails');
    const detailsCount = document.getElementById('detailsCount');
    function updateCount() {
      if (details && detailsCount) detailsCount.textContent = details.value.length + ' / ' + details.maxLength;
    }
    if (details) details.addEventListener('input', updateCount);

    // Re-validate a field as soon as the user fixes it
    form.querySelectorAll('input, select, textarea').forEach(function (field) {
      ['input', 'change'].forEach(function (evt) {
        field.addEventListener(evt, function () {
          if (form.classList.contains('was-validated')) field.checkValidity();
        });
      });
    });

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      form.classList.add('was-validated');
      if (!form.checkValidity()) {
        const firstInvalid = form.querySelector(':invalid');
        if (firstInvalid) firstInvalid.focus();
        return;
      }

      const btn = form.querySelector('button[type="submit"]');
      const original = btn.innerHTML;
      btn.disabled = true;
      btn.innerHTML = '<span class="spinner-border spinner-border-sm me-2" aria-hidden="true"></span>Sending…';

      // Replace this timeout with a real request (fetch to your form endpoint / CRM).
      setTimeout(function () {
        const first = document.getElementById('fullName').value.trim().split(' ')[0];
        document.getElementById('successName').textContent = first || 'neighbor';
        formWrap.classList.add('d-none');
        success.classList.remove('d-none');
        btn.disabled = false;
        btn.innerHTML = original;
      }, 900);
    });

    document.getElementById('resetQuote').addEventListener('click', function () {
      form.reset();
      form.classList.remove('was-validated');
      updateCount();
      success.classList.add('d-none');
      formWrap.classList.remove('d-none');
      document.getElementById('fullName').focus();
    });
  }

  /* ---------- Footer year ---------- */
  const year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();
})();
