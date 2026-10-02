/* Read only after a reader presses Listen. No accounts or external API. */
(() => {
  const supported = 'speechSynthesis' in window && 'SpeechSynthesisUtterance' in window;
  let active = null;
  let utterance = null;
  const status = document.createElement('p');
  status.className = 'listen-status';
  status.setAttribute('role', 'status');
  document.querySelector('.a11y-bar').after(status);
  const reset = () => {
    if (active) { active.textContent = '🔊 Listen'; active.setAttribute('aria-pressed', 'false'); active.setAttribute('aria-label', active.dataset.listenLabel); }
    active = null;
    utterance = null;
  };
  const stop = () => { reset(); if (supported) window.speechSynthesis.cancel(); };
  const cleanText = node => {
    const copy = node.cloneNode(true);
    copy.querySelectorAll('.listen-button,textarea,input,.nav-row,.section-badge').forEach(el => el.remove());
    return copy.textContent.replace(/\s+/g, ' ').trim();
  };
  function addControls() {
    document.querySelectorAll('.q-text,.style-q-text,.spark-title,.section-header,#results-content').forEach(prompt => {
      if (prompt.querySelector('.listen-button') || !prompt.textContent.trim()) return;
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'listen-button';
      button.textContent = '🔊 Listen';
      const label = prompt.id === 'results-content' ? 'Listen to your report' : `Listen: ${cleanText(prompt)}`;
      button.dataset.listenLabel = label;
      button.setAttribute('aria-label', label);
      button.setAttribute('aria-pressed', 'false');
      button.addEventListener('click', () => {
        if (active === button) { stop(); status.textContent = 'Reading stopped.'; return; }
        stop();
        if (!supported) { status.textContent = 'Read-aloud is not available in this browser. Try your device’s reading tools or another browser.'; return; }
        // Include the answer choices for grouped prompts, but never typed notes.
        let target = prompt;
        if (prompt.matches('.style-q-text,.spark-title')) target = prompt.parentElement;
        if (prompt.closest('#s2') && prompt.matches('.section-header')) target = prompt.closest('.section');
        const text = cleanText(target);
        const speech = new SpeechSynthesisUtterance(text);
        speech.lang = document.documentElement.lang || 'en-US';
        speech.rate = 0.9;
        utterance = speech;
        active = button;
        button.textContent = '⏹ Stop';
        button.setAttribute('aria-label', 'Stop reading');
        button.setAttribute('aria-pressed', 'true');
        status.textContent = 'Reading aloud. Press Stop to stop reading.';
        speech.onend = () => { if (utterance === speech) { reset(); status.textContent = 'Reading finished.'; } };
        speech.onerror = () => { if (utterance === speech) { reset(); status.textContent = 'Reading could not start. Try another voice or your device’s reading tools.'; } };
        try { window.speechSynthesis.speak(speech); } catch (_) { speech.onerror(); }
      });
      prompt.appendChild(button);
    });
  }
  document.addEventListener('DOMContentLoaded', addControls);
  // Rebuilt questions and reports need their own fresh controls.
  new MutationObserver(addControls).observe(document.querySelector('main'), {childList:true,subtree:true});
  document.addEventListener('click', event => { if (event.target.closest('.nav-row')) { stop(); status.textContent = ''; } });
  window.addEventListener('pagehide', stop);
  window.addEventListener('beforeprint', stop);
  addControls();
})();
