{
  // Ruta al navegador para exportar con Puppeteer
  "puppeteerExecutablePath": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe", 

  // Configuración de KaTeX (fórmulas rápidas)
  "katexConfig": {
    "macros": {
      "\\RR": "\\mathbb{R}",   // ejemplo: \RR → ℝ
      "\\NN": "\\mathbb{N}"    // ejemplo: \NN → ℕ
    }
  },

  // Configuración de MathJax (si prefieres este motor en lugar de KaTeX)
  "mathjaxConfig": {
    "tex": {
      "inlineMath": [["$", "$"], ["\\(", "\\)"]],
      "displayMath": [["$$", "$$"], ["\\[", "\\]"]]
    },
    "options": {},
    "loader": {}
  },

  // Configuración de Mermaid
  "mermaidConfig": {
    "startOnLoad": true,
    "theme": "default"
  },

  // Otros ajustes útiles
  "printBackground": true,   // Exporta el fondo y colores al PDF
  "pdfOptions": {
    "format": "A4",
    "margin": {
      "top": "20mm",
      "right": "20mm",
      "bottom": "20mm",
      "left": "20mm"
    }
  }
}
