# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Sphinxの練習'
copyright = '2024, hikaru'
author = 'hikaru'
release = '2024.1.11'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'ja'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'bizstyle'

html_sidebars = {
   '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html']
}

# 下記オプションでバックグラウンドの色を変更できます。※必須ではありません
html_theme_options = {
                        'maincolor' : "#705DA8",
                        }

html_static_path = ['_static']