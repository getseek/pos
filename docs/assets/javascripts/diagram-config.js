/* Preserve theme colors while keeping diagrams at readable intrinsic dimensions. */
(() => {
  "use strict";
  const initialize = mermaid.initialize.bind(mermaid);
  mermaid.initialize = options => initialize({
    ...options,
    securityLevel: "strict",
    startOnLoad: false,
    flowchart: {...(options.flowchart || {}), useMaxWidth: false}
  });
})();
