/* Browser-only review drafts. No network requests or application actions. */
(() => {
  "use strict";
  const key = "premium-pos-review-2026-10-18-v1";
  function init() {
    const sections = [...document.querySelectorAll(".review-choice")];
    if (!sections.length || sections[0].dataset.initialized) return;
    let choices = {};
    try { choices = JSON.parse(localStorage.getItem(key) || "{}"); } catch (_) { choices = {}; }
    if (!choices || Array.isArray(choices) || typeof choices !== "object") choices = {};
    const status = document.querySelector("[data-review-status]");
    function update(message) {
      const selected = sections.filter(s => s.querySelector("select").value).length;
      if (status) status.textContent = message || `${selected} of ${sections.length} choices saved locally`;
    }
    function highlight(id, value) {
      document.querySelectorAll(".review-option").forEach(el => {
        if (el.dataset.reviewFinding === id) el.classList.toggle("is-selected", el.dataset.reviewOption === value);
      });
    }
    for (const section of sections) {
      section.dataset.initialized = "true";
      const id = section.dataset.reviewId;
      const select = section.querySelector("select");
      if ([...select.options].some(o => o.value === choices[id])) select.value = choices[id];
      highlight(id, select.value);
      select.addEventListener("change", () => {
        choices[id] = select.value;
        highlight(id, select.value);
        try { localStorage.setItem(key, JSON.stringify(choices)); update(); }
        catch (_) { update("Browser storage unavailable; export choices before leaving."); }
      });
    }
    document.querySelector("[data-review-export]")?.addEventListener("click", () => {
      const records = sections.map(section => {
        const select = section.querySelector("select");
        const selected = select.selectedOptions[0];
        return {finding: section.dataset.reviewId, title: section.dataset.reviewTitle,
          option: select.value || null, label: select.value ? selected.textContent : "Not chosen"};
      });
      const payload = {schema_version: 1, source_review: "2026-10-18", exported_at: new Date().toISOString(),
        status: "Review draft only; no approval submitted and no POS changes executed", choices: records};
      const url = URL.createObjectURL(new Blob([JSON.stringify(payload, null, 2) + "\n"], {type: "application/json"}));
      const link = document.createElement("a"); link.href = url; link.download = "premium-pos-review-choices.json";
      document.body.appendChild(link); link.click(); link.remove();
      setTimeout(() => URL.revokeObjectURL(url), 1000); update("Review draft exported; no application changes made.");
    });
    document.querySelector("[data-review-clear]")?.addEventListener("click", () => {
      choices = {};
      try { localStorage.removeItem(key); } catch (_) { /* Selection remains usable. */ }
      for (const section of sections) { section.querySelector("select").value = ""; highlight(section.dataset.reviewId, ""); }
      update();
    });
    update();
  }
  if (typeof document$ !== "undefined") document$.subscribe(init);
  else if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
