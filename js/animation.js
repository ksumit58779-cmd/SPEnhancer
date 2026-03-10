/* ============================================
   animation.js — Shimmer sweep animation engine
   AI Prompt Enhancer
   ============================================ */

// ── Shimmer Sweep ──
const shimmerBar = document.getElementById('shimmerBar');

function runShimmer(el) {
  return new Promise(resolve => {
    if (!shimmerBar) return resolve();
    shimmerBar.classList.remove('sweep');
    void shimmerBar.offsetWidth; // force reflow
    shimmerBar.classList.add('sweep');
    setTimeout(resolve, 760);
  });
}

// ── Sparkle Particles ──
function spawnSparkles(el) {
  if (!el) return;
  const rect   = el.getBoundingClientRect();
  const colors = ['#f4c95d', '#7c6aff', '#a78bfa', '#ffffff', '#4ade80', '#fb7185'];

  for (let i = 0; i < 20; i++) {
    const sp  = document.createElement('div');
    sp.className = 'sparkle';

    const x  = rect.left + Math.random() * rect.width;
    const y  = rect.top  + Math.random() * rect.height + window.scrollY;
    const dx = (Math.random() - 0.5) * 70 + 'px';
    const dy = (Math.random() - 0.5) * 70 + 'px';
    const color = colors[Math.floor(Math.random() * colors.length)];
    const size  = Math.random() * 4 + 3;
    const delay = Math.random() * 0.2;

    sp.style.cssText = `
      left: ${x}px;
      top: ${y}px;
      background: ${color};
      width: ${size}px;
      height: ${size}px;
      --dx: ${dx};
      --dy: ${dy};
      animation-delay: ${delay}s;
    `;

    document.body.appendChild(sp);
    setTimeout(() => sp.remove(), 800);
  }
}

// ── Wave Visualizer ──
const waveWrap = document.getElementById('waveWrap');
let   waveInterval = null;

function buildWave() {
  if (!waveWrap) return;
  waveWrap.innerHTML = '';
  for (let i = 0; i < 16; i++) {
    const bar = document.createElement('div');
    bar.className = 'wave-bar';
    bar.style.height = '3px';
    waveWrap.appendChild(bar);
  }
}

function animateWave(on) {
  if (!waveWrap) return;
  if (!on) {
    clearInterval(waveInterval);
    waveWrap.querySelectorAll('.wave-bar')
      .forEach(b => b.style.height = '3px');
    return;
  }
  waveInterval = setInterval(() => {
    waveWrap.querySelectorAll('.wave-bar').forEach(bar => {
      bar.style.height = (Math.random() * 14 + 3) + 'px';
    });
  }, 90);
}

// ── Card Entrance ──
function animateCards(selector, delayStep = 0.05) {
  document.querySelectorAll(selector).forEach((card, i) => {
    card.style.animationDelay = (i * delayStep) + 's';
    card.classList.add('animate-card');
  });
}

// ── Staggered Fade In ──
function staggerFadeIn(elements, delayStep = 0.08) {
  elements.forEach((el, i) => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(14px)';
    el.style.transition = `opacity 0.4s ease ${i * delayStep}s, transform 0.4s ease ${i * delayStep}s`;
    setTimeout(() => {
      el.style.opacity = '1';
      el.style.transform = 'translateY(0)';
    }, 50);
  });
}

// ── Page Load Animation ──
function animatePageLoad() {
  const hero = document.querySelector('.hero');
  if (hero) {
    hero.style.opacity = '0';
    hero.style.transform = 'translateY(24px)';
    hero.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    requestAnimationFrame(() => {
      setTimeout(() => {
        hero.style.opacity = '1';
        hero.style.transform = 'translateY(0)';
      }, 100);
    });
  }
}

// ── Initialize ──
document.addEventListener('DOMContentLoaded', () => {
  buildWave();
  animatePageLoad();
});
document.addEventListener("DOMContentLoaded", () => {

  const elements = document.querySelectorAll(
    ".hero, .chat-window, .input-area"
  );

  elements.forEach((el,i)=>{
      el.style.opacity="0";
      el.style.transform="translateY(20px)";

      setTimeout(()=>{
          el.style.transition="all 0.6s ease";
          el.style.opacity="1";
          el.style.transform="translateY(0)";
      },200 + i*120);
  });

});