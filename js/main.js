/* ============================================
   main.js — App logic, button handlers, API calls
   AI Prompt Enhancer
   ============================================ */

// ── State ──
let currentMode   = 'normal';
let currentResult = '';

// ── DOM Elements ──
const promptInput = document.getElementById('promptInput');
const charCount   = document.getElementById('charCount');
const enhanceBtn  = document.getElementById('enhanceBtn');
const btnText     = document.getElementById('btnText');

// ── Init ──
document.addEventListener('DOMContentLoaded', () => {
  setupModeSelector();
  setupCharCount();
  setupEnhanceBtn();
  setupOutputActions();
  checkReusePrompt();
});

// ── Mode Selector ──
function setupModeSelector() {
  document.querySelectorAll('.mode-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.mode-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      currentMode = btn.dataset.mode;
    });
  });
}

// ── Char Count ──
function setupCharCount() {
  if (!promptInput || !charCount) return;
  promptInput.addEventListener('input', () => {
    charCount.textContent = promptInput.value.length;
  });
}

// ── Enhance Button ──
function setupEnhanceBtn() {
  if (!enhanceBtn) return;
  enhanceBtn.addEventListener('click', handleEnhance);

  // Allow Ctrl+Enter to submit
  promptInput.addEventListener('keydown', (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
      handleEnhance();
    }
  });
}

// ── Main Enhance Handler ──
async function handleEnhance() {
  const prompt = promptInput.value.trim();
  if (!prompt) {
    showToast('⚠️ Please enter a prompt first!');
    promptInput.focus();
    return;
  }

  setLoading(true);
  showLoadingState();

  try {
    const result = await enhanceAPI(prompt, currentMode);

    if (!result.success) {
      showToast('❌ Error: ' + result.error);
      resetOutput();
      return;
    }

    currentResult = result.enhanced_prompt;
    await runReveal(result.enhanced_prompt);

  } catch (err) {
    console.error('Enhance error:', err);
    showToast('🔌 Connection error. Is the server running?');
    resetOutput();
  } finally {
    setLoading(false);
  }
}

// ── API Call ──
async function enhanceAPI(prompt, mode) {
  const res = await fetch('/api/enhance', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ prompt, mode })
  });
  return await res.json();
}

// ── Loading State ──
let loadingMsgInterval = null;
const loadingMessages = [
  'Analyzing your prompt...',
  'Applying AI magic...',
  'Optimizing structure...',
  'Polishing the output...',
  'Almost ready...'
];

function showLoadingState() {
  const placeholder  = document.getElementById('outputPlaceholder');
  const loadingWrap  = document.getElementById('loadingWrap');
  const outputContent = document.getElementById('outputContent');
  const loadingText  = document.getElementById('loadingText');

  if (placeholder)   placeholder.style.display = 'none';
  if (outputContent) outputContent.classList.remove('active');
  if (loadingWrap)   loadingWrap.classList.add('active');

  let mi = 0;
  if (loadingText) {
    loadingText.textContent = loadingMessages[0];
    loadingMsgInterval = setInterval(() => {
      mi = (mi + 1) % loadingMessages.length;
      loadingText.textContent = loadingMessages[mi];
    }, 900);
  }
}

function hideLoadingState() {
  clearInterval(loadingMsgInterval);
  const loadingWrap = document.getElementById('loadingWrap');
  if (loadingWrap) loadingWrap.classList.remove('active');
}

function resetOutput() {
  hideLoadingState();
  const placeholder = document.getElementById('outputPlaceholder');
  if (placeholder) placeholder.style.display = 'flex';
}

function setLoading(state) {
  if (!enhanceBtn) return;
  enhanceBtn.disabled = state;
  if (btnText) btnText.textContent = state ? 'Enhancing...' : 'Enhance Prompt';
}

// ── Reveal Animation ──
async function runReveal(text) {
  hideLoadingState();

  const outputWrap    = document.getElementById('outputWrap');
  const outputContent = document.getElementById('outputContent');
  const outputText    = document.getElementById('outputText');
  const outputBadge   = document.getElementById('outputBadge');

  // Sweep 1
  playWhoosh();
  await runShimmer(outputWrap);
  spawnSparkles(outputWrap);
  playSparkleChimes();

  await sleep(80);

  // Sweep 2 + reveal
  playWhoosh();
  await runShimmer(outputWrap);

  outputContent.classList.add('active');
  outputText.classList.remove('visible');
  outputText.textContent = text;

  await sleep(60);
  outputText.classList.add('visible');

  // Badge
  const modeLabels = {
    normal:        '⚡ Normal',
    pro:           '🚀 Pro',
    extremely_pro: '💎 Extremely Pro'
  };
  outputBadge.textContent = modeLabels[currentMode] || 'Enhanced';
  outputBadge.className   = `output-badge ${currentMode}`;
  setTimeout(() => outputBadge.classList.add('show'), 100);

  // Magic sound + wave
  playMagicSound();
  animateWave(true);
  setTimeout(() => animateWave(false), 2200);
}

// ── Output Actions ──
function setupOutputActions() {
  const copyBtn  = document.getElementById('copyBtn');
  const clearBtn = document.getElementById('clearBtn');

  if (copyBtn) {
    copyBtn.addEventListener('click', () => {
      if (!currentResult) return;
      navigator.clipboard.writeText(currentResult)
        .then(() => showToast('✓ Copied to clipboard!'))
        .catch(() => showToast('❌ Copy failed.'));
    });
  }

  if (clearBtn) {
    clearBtn.addEventListener('click', () => {
      document.getElementById('outputContent').classList.remove('active');
      document.getElementById('outputPlaceholder').style.display = 'flex';
      document.getElementById('outputBadge').classList.remove('show');
      document.getElementById('outputText').classList.remove('visible');
      currentResult = '';
      animateWave(false);
    });
  }
}

// ── Check Reuse Prompt (from library/history) ──
function checkReusePrompt() {
  const reuse = localStorage.getItem('reuse_prompt');
  if (reuse && promptInput) {
    promptInput.value = reuse;
    charCount.textContent = reuse.length;
    localStorage.removeItem('reuse_prompt');
    promptInput.focus();
    showToast('✓ Prompt loaded from library!');
  }
}

// ── Toast ──
function showToast(msg) {
  const t = document.getElementById('toast');
  if (!t) return;
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2500);
}

// ── Sleep helper ──
function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}