# Fritz-Kola LaTeX Dokumentation

## Übersicht / Overview / 概述

Dieses Verzeichnis enthält die LaTeX-Dokumentation für Fritz-Kola mit trilingualen Inhalten (Deutsch, Englisch, Chinesisch).

This directory contains the LaTeX documentation for Fritz-Kola with trilingual content (German, English, Chinese).

此目录包含 Fritz-Kola 的 LaTeX 文档，包含三种语言（德语、英语、中文）。

## Dateien / Files / 文件

- `fritz-kola.tex` - Haupt-LaTeX-Dokument / Main LaTeX document / 主 LaTeX 文档
- `fritz-kola.jpg` - Produktbild / Product image / 产品图片
- `fritz-kola-details.jpg` - Detailbild / Detail image / 详情图片
- `generate_map.py` - Python-Skript zur Kartenerstellung / Python script for map generation / 地图生成 Python 脚本
- `requirements.txt` - Python-Abhängigkeiten / Python dependencies / Python 依赖项

## Karten generieren / Generate Maps / 生成地图

Um die geografischen Karten zu generieren, führen Sie das Python-Skript aus:

To generate the geographic maps, run the Python script:

要生成地理地图，请运行 Python 脚本：

```bash
# Abhängigkeiten installieren / Install dependencies / 安装依赖
pip install -r requirements.txt

# Karten generieren / Generate maps / 生成地图
python generate_map.py
```

Dies erstellt zwei Karten:
- `fritz-kola-manufacturer-map.png` - Herstellerstandort in Hamburg
- `fritz-kola-supply-chain-map.png` - Supply Chain Karte mit Verteilungszentren

This creates two maps:
- `fritz-kola-manufacturer-map.png` - Manufacturer location in Hamburg
- `fritz-kola-supply-chain-map.png` - Supply chain map with distribution centers

这将创建两张地图：
- `fritz-kola-manufacturer-map.png` - 汉堡制造商位置
- `fritz-kola-supply-chain-map.png` - 带分销中心的供应链地图

**Hinweis / Note / 注意**: Das Skript funktioniert auch ohne `cartopy`, verwendet dann aber eine einfachere Kartenvisualisierung.

The script also works without `cartopy`, but will use a simpler map visualization.

脚本在没有 `cartopy` 的情况下也能工作，但会使用更简单的地图可视化。

## LaTeX kompilieren / Compile LaTeX / 编译 LaTeX

**Wichtig / Important / 重要**: Dieses Dokument muss mit **XeLaTeX** kompiliert werden (nicht pdfLaTeX).

This document must be compiled with **XeLaTeX** (not pdfLaTeX).

此文档必须使用 **XeLaTeX** 编译（不是 pdfLaTeX）。

### In Overleaf:
1. Menü → Compiler → **XeLaTeX** auswählen
2. Kompilieren

### Lokal / Locally / 本地:
```bash
xelatex fritz-kola.tex
xelatex fritz-kola.tex  # Zweimal für korrekte Referenzen / Twice for correct references / 两次以获得正确的引用
```

## Schriftarten / Fonts / 字体

Falls Sie Fehler bei chinesischen Schriftarten erhalten, können Sie den Font-Namen in `fritz-kola.tex` (Zeilen 23-40) anpassen.

If you get errors with Chinese fonts, you can adjust the font name in `fritz-kola.tex` (lines 23-40).

如果您在中文字体方面遇到错误，可以在 `fritz-kola.tex`（第 23-40 行）中调整字体名称。

Häufig verfügbare Fonts / Commonly available fonts / 常用字体:
- `Noto Sans CJK SC` (empfohlen für Overleaf / recommended for Overleaf / Overleaf 推荐)
- `FandolSong`
- `SimSun`
- `STSong`
