# World Product Gallery / 世界产品画廊 / Weltproduktgalerie

> A bottom-up Qingming Riverside Scene (清明上河图) of world products and supply chains

Eine von unten nach oben aufgebaute Qingming-Flusslandschaft (清明上河图) der Weltprodukte und Lieferketten

从底向上的世界产品及供应链的清明上河图

---

## Overview / Übersicht / 概述

The **World Product Gallery** is a comprehensive documentation project that analyzes products from around the world through detailed supply chain analysis. Inspired by the famous Chinese painting "Along the River During the Qingming Festival" (清明上河图), which captures intricate details of daily life and commerce, this project aims to create a detailed "map" of modern global supply chains.

Each product entry provides:
- **Product Description** - Detailed specifications and characteristics
- **Market Analysis** - Market positioning, trends, and competitive landscape
- **Manufacturer Information** - Company details, location, and history
- **Market Entities** - Key stakeholders and market participants
- **Supply Chain Analysis** - Raw materials, production processes, distribution networks
- **Geographic Visualizations** - Maps showing manufacturing locations and supply chain routes
- **Business Insights** - Comprehensive guides on building similar businesses

All content is presented in **three languages**: German, English, and Chinese.

---

## Project Structure / Projektstruktur / 项目结构

```
world-product-gallery/
├── README.md                    # This file / Diese Datei / 本文件
├── LICENSE                      # MIT License
├── fast_commit.ps1             # Git commit helper script
│
├── paper/                       # Project documentation / Projektdokumentation / 项目文档
│   └── main.tex                # Project statement and overview
│
└── product-tex/                # Product documentation / Produktdokumentation / 产品文档
    └── {country}/
        └── {city}/
            ├── {product}.tex   # Main LaTeX document
            ├── {product}.jpg   # Product images
            ├── generate_map.py # Map generation script
            ├── requirements.txt# Python dependencies
            └── README.md       # Product-specific instructions
```

### Current Products / Aktuelle Produkte / 当前产品

- **Germany / Deutschland / 德国**
  - **Hamburg**: Fritz-Kola - A German cola brand with high caffeine content

---

## Getting Started / Erste Schritte / 入门指南

### Prerequisites / Voraussetzungen / 先决条件

1. **LaTeX Distribution** (with XeLaTeX support)
   - **Windows**: MiKTeX or TeX Live
   - **macOS**: MacTeX
   - **Linux**: TeX Live

2. **Python 3.7+** (for map generation)
   - Required packages: `matplotlib`, `numpy`, `cartopy` (optional)

3. **Chinese Fonts** (for Chinese character support)
   - Recommended: Noto Sans CJK SC
   - Alternatives: FandolSong, SimSun, STSong

### Installation / Installation / 安装

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/world-product-gallery.git
   cd world-product-gallery
   ```

2. **Install Python dependencies** (for map generation):
   ```bash
   cd product-tex/germany/hamburg
   pip install -r requirements.txt
   ```

3. **Generate maps** (optional):
   ```bash
   python generate_map_simple.py
   # or
   python generate_map.py  # if cartopy is installed
   ```

### Compiling Documents / Dokumente kompilieren / 编译文档

**Important / Wichtig / 重要**: All LaTeX documents must be compiled with **XeLaTeX** (not pdfLaTeX) to support Chinese characters.

#### Using Overleaf:

1. Upload the `.tex` file to Overleaf
2. Go to Menu → Compiler → Select **XeLaTeX**
3. Click "Recompile"

#### Using Command Line:

```bash
cd product-tex/germany/hamburg
xelatex fritz-kola.tex
xelatex fritz-kola.tex  # Run twice for correct references
```

#### Using VS Code with LaTeX Workshop:

Add to your `settings.json`:
```json
{
  "latex-workshop.latex.recipes": [
    {
      "name": "xelatex",
      "tools": ["xelatex", "xelatex"]
    }
  ],
  "latex-workshop.latex.tools": [
    {
      "name": "xelatex",
      "command": "xelatex",
      "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "%DOC%"
      ]
    }
  ]
}
```

---

## Adding New Products / Neue Produkte hinzufügen / 添加新产品

To add a new product to the gallery:

1. **Create directory structure:**
   ```
   product-tex/{country}/{city}/
   ```

2. **Create the main LaTeX file:**
   - Copy `fritz-kola.tex` as a template
   - Update all content sections
   - Ensure trilingual content (German, English, Chinese)

3. **Add product images:**
   - `{product}.jpg` - Main product image
   - `{product}-details.jpg` - Detailed view (optional)

4. **Create map generation script** (if geographic visualization is needed):
   - Copy `generate_map_simple.py` as a template
   - Update coordinates and locations
   - Run to generate map images

5. **Create product-specific README.md:**
   - Document any special requirements
   - Include compilation instructions

### Template Structure / Vorlagenstruktur / 模板结构

Each product document should include:

- **Product Description** (DE/EN/ZH)
- **Market Analysis** (DE/EN/ZH)
- **Manufacturer Information** (DE/EN/ZH)
- **Market Entities** (DE/EN/ZH)
- **Supply Chain Analysis** (DE/EN/ZH)
  - Raw materials sourcing
  - Production processes
  - Distribution networks
  - Transportation methods
- **Market Analysis** (DE/EN/ZH)
- **Visualizations**
  - Supply chain diagrams (TikZ)
  - Geographic maps (Python-generated)
  - Cost distribution charts
  - Process flow diagrams
- **Business Guide** (DE/EN/ZH)
  - How to build a similar business
  - Startup costs
  - Timeline
  - Requirements

---

## Features / Funktionen / 功能

### Visualizations / Visualisierungen / 可视化

- **TikZ Diagrams**: Supply chain flows, cost distributions, process flows
- **Geographic Maps**: Manufacturer locations, supply chain routes
- **Charts**: Pie charts, bar charts, flow diagrams
- **Tables**: Cost breakdowns, specifications, comparisons

### Content / Inhalt / 内容

- **Trilingual**: All content in German, English, and Chinese
- **Comprehensive**: Detailed analysis from raw materials to end consumers
- **Visual**: Rich diagrams and maps for better understanding
- **Practical**: Business guides for entrepreneurs

---

## Contributing / Beitragen / 贡献

Contributions are welcome! Please follow these guidelines:

1. **Language**: Maintain trilingual content (DE/EN/ZH)
2. **Structure**: Follow the existing directory structure
3. **Quality**: Ensure accurate information and proper citations
4. **Visuals**: Include high-quality images and diagrams
5. **Documentation**: Update README files as needed

### Contribution Process / Beitragsprozess / 贡献流程

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-product`)
3. Add your product documentation
4. Commit changes (`git commit -m 'Add new product: ProductName'`)
5. Push to branch (`git push origin feature/new-product`)
6. Open a Pull Request

---

## License / Lizenz / 许可证

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments / Danksagungen / 致谢

- Inspired by the Chinese painting "Along the River During the Qingming Festival" (清明上河图)
- Built with LaTeX, TikZ, Python, and open-source tools

---

## Contact / Kontakt / 联系方式

For questions, suggestions, or contributions, please open an issue on GitHub.

---

## Project Status / Projektstatus / 项目状态

**Status**: Prototype / Prototyp / 原型

This is an active project. New products and features are being added regularly.

---

**Last Updated / Zuletzt aktualisiert / 最后更新**: 2026
