# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SUNGWOONG_TOUR'
copyright = '2024, YOONSUNGWOONG'
author = 'YOONSUNGWOONG'
release = "1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",  # Google Style Python Docstrings 사용 시 추가
]

# add_module_names = False  # 문서에 클래스 및 함수를 표시할 때 경로 생략 시 추가

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

## 추가
import os
import sys
sys.path.insert(0, os.path.abspath('./../../src/my_package'))