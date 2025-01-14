window.MathJax = {
    tex: {
      inlineMath: [["\\(", "\\)"], ["$", "$"]],
      displayMath: [["\\[", "\\]"], ["$$", "$$"]],
      processEscapes: true,
      processEnvironments: true
    },
    options: {
      ignoreHtmlClass: "tex2jax_ignore", // Standard MathJax ignore class
      processHtmlClass: ".*" // Process all elements
    }
  };
  
  
  document$.subscribe(() => { 
    MathJax.startup.output.clearCache();
    MathJax.typesetClear();
    MathJax.texReset();
    MathJax.typesetPromise();
  });
  