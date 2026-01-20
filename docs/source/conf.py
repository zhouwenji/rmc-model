# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'RMC'
author = 'School of Applied Economics, Renmin University of China'
copyright = f'2025, {author}'
release = 'v0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',       # 支持 Markdown
    # 'sphinx_markdown_tables', # 支持 Markdown 表格
    'sphinx.ext.mathjax', # 数学公式
    'sphinx.ext.autosectionlabel',  # 交叉引用
]

myst_enable_extensions = [
    "amsmath",    # 支持LaTeX数学环境（如 \begin{align}）
    "dollarmath", # 支持美元符号数学（如 $...$ 和 $$...$$）
    "colon_fence",
    "deflist",
]

# MathJax 3.x 路径（用于渲染数学公式）
mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"

mathjax3_config = {
    'tex': {
        'inlineMath': [['$', '$'], ['\\(', '\\)']],
        'displayMath': [['$$', '$$'], ['\\[', '\\]']],
        'processEscapes': True,
    },
}

# 指定哪些文件后缀会被解析
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}



templates_path = ['_templates']
exclude_patterns = []

# mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

# RTD 主题配置
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'titles_only':  False,
}

import sys
from pathlib import Path

# 获取当前文件(conf.py)的路径
current_dir = Path(__file__).resolve().parent
# 计算项目根目录的路径（假设项目根目录在 docs 的上一级）
project_root = current_dir.parent.parent
# 将项目根目录添加到 sys.path
sys.path.insert(0, str(project_root))
# # 如果你的模型代码在项目下的某个子目录，例如 'src'，也可以单独添加
# sys.path.insert(0, str(project_root / 'src'))
