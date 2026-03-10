/* ============================================
   library.js — Prompt library search & filter
   AI Prompt Enhancer
   ============================================ */

// ── State ──
let allPrompts  = [];
let filtered    = [];
let activeCat   = 'all';
let searchQuery = '';
let modalPrompt = null;

// ── Init ──
document.addEventListener('DOMContentLoaded', () => {
  loadLibrary();
  setupSearch();
  setupCategoryTabs();
  setupModal();
});

// ── Load Library from API ──
async function loadLibrary() {
  try {
    const res  = await fetch('/api/library?category=all');
    allPrompts = await res.json();
    updateCounts();
    applyFilters();
  } catch (err) {
    console.error('Library load error:', err);
    document.getElementById('promptsGrid').innerHTML = `
      <div class="empty-state">
        <div class="empty-icon">⚠️</div>
        <div class="empty-title">Could not load library</div>
        <p class="empty-sub">Make sure the server is running on port 5000.</p>
      </div>`;
  }
}

// ── Update Category Counts ──
function updateCounts() {
  const countMap = {
    all:       allPrompts.length,
    coding:    allPrompts.filter(p => p.category === 'coding').length,
    writing:   allPrompts.filter(p => p.category === 'writing').length,
    business:  allPrompts.filter(p => p.category === 'business').length,
    education: allPrompts.filter(p => p.category === 'education').length,
    creative:  allPrompts.filter(p => p.category === 'creative').length,
    marketing: allPrompts.filter(p => p.category === 'marketing').length,
  };

  Object.entries(countMap).forEach(([key, val]) => {
    const el = document.getElementById('count' + capitalize(key));
    if (el) el.textContent = val;
  });
}

// ── Apply Filters + Search ──
function applyFilters() {
  filtered = allPrompts;

  if (activeCat !== 'all') {
    filtered = filtered.filter(p => p.category === activeCat);
  }

  if (searchQuery) {
    const q = searchQuery.toLowerCase();
    filtered = filtered.filter(p =>
      p.title.toLowerCase().includes(q) ||
      p.prompt.toLowerCase().includes(q)
    );
  }

  renderGrid();
}

// ── Render Grid ──
function renderGrid() {
  const grid = document.getElementById('promptsGrid');
  const info = document.getElementById('resultsInfo');
  if (!grid) return;

  if (info) {
    info.innerHTML = `Showing <span>${filtered.length}</span> prompt${filtered.length !== 1 ? 's' : ''}${
      searchQuery ? ` for "<span>${escHtml(searchQuery)}</span>"` : ''
    }`;
  }

  if (filtered.length === 0) {
    grid.innerHTML = `
      <div class="empty-state">
        <div class="empty-icon">🔍</div>
        <div class="empty-title">No prompts found</div>
        <p class="empty-sub">Try a different search term or category.</p>
      </div>`;
    return;
  }

  grid.innerHTML = '';

  filtered.forEach((p, i) => {
    const card = document.createElement('div');
    card.className = 'prompt-card';
    card.style.animationDelay = (i * 0.04) + 's';
    card.innerHTML = `
      <div class="card-top" style="display:flex;align-items:flex-start;justify-content:space-between;gap:0.5rem;">
        <div class="prompt-title">${escHtml(p.title)}</div>
        <span class="cat-badge ${p.category}">${p.category}</span>
      </div>
      <div class="prompt-preview">${escHtml(p.prompt)}</div>
      <div class="card-actions" style="display:flex;gap:0.4rem;padding-top:0.5rem;border-top:1px solid var(--border);">
        <button class="btn-use" onclick="openModal(${p.id})">✦ View & Use</button>
        <button class="btn-copy-card" title="Copy" onclick="copyPromptCard(${p.id}, event)">📋</button>
      </div>
    `;
    grid.appendChild(card);
  });
}

// ── Setup Search ──
function setupSearch() {
  const input = document.getElementById('searchInput');
  const clear = document.getElementById('searchClear');
  if (!input) return;

  input.addEventListener('input', () => {
    searchQuery = input.value;
    if (clear) clear.classList.toggle('show', searchQuery.length > 0);
    applyFilters();
  });

  if (clear) {
    clear.addEventListener('click', () => {
      input.value = '';
      searchQuery = '';
      clear.classList.remove('show');
      applyFilters();
      input.focus();
    });
  }
}

// ── Setup Category Tabs ──
function setupCategoryTabs() {
  document.querySelectorAll('.cat-tab').forEach(btn => {
    btn.addEventListener('click', () => {
      document.querySelectorAll('.cat-tab').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      activeCat = btn.dataset.cat;
      applyFilters();
    });
  });
}

// ── Open Modal ──
function openModal(id) {
  modalPrompt = allPrompts.find(p => p.id === id);
  if (!modalPrompt) return;

  const titleEl = document.getElementById('modalTitle');
  const textEl  = document.getElementById('modalText');
  const overlay = document.getElementById('modalOverlay');

  if (titleEl) titleEl.textContent = modalPrompt.title;
  if (textEl)  textEl.textContent  = modalPrompt.prompt;
  if (overlay) overlay.classList.add('show');
}

// ── Setup Modal ──
function setupModal() {
  const overlay   = document.getElementById('modalOverlay');
  const closeBtn  = document.getElementById('modalClose');
  const copyBtn   = document.getElementById('modalCopy');
  const useBtn    = document.getElementById('modalUse');

  if (closeBtn) {
    closeBtn.addEventListener('click', closeModal);
  }

  if (overlay) {
    overlay.addEventListener('click', e => {
      if (e.target === overlay) closeModal();
    });
  }

  // Close on Escape
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') closeModal();
  });

  if (copyBtn) {
    copyBtn.addEventListener('click', () => {
      if (!modalPrompt) return;
      navigator.clipboard.writeText(modalPrompt.prompt)
        .then(() => showToast('✓ Copied!'));
    });
  }

  if (useBtn) {
    useBtn.addEventListener('click', () => {
      if (!modalPrompt) return;
      localStorage.setItem('reuse_prompt', modalPrompt.prompt);
      window.location.href = '/';
    });
  }
}

function closeModal() {
  const overlay = document.getElementById('modalOverlay');
  if (overlay) overlay.classList.remove('show');
}

// ── Copy Prompt from Card ──
function copyPromptCard(id, e) {
  e.stopPropagation();
  const p = allPrompts.find(p => p.id === id);
  if (!p) return;
  navigator.clipboard.writeText(p.prompt)
    .then(() => showToast('✓ Copied!'));
}

// ── Helpers ──
function escHtml(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;');
}

function capitalize(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

function showToast(msg) {
  const t = document.getElementById('toast');
  if (!t) return;
  t.textContent = msg;
  t.classList.add('show');
  setTimeout(() => t.classList.remove('show'), 2500);
}