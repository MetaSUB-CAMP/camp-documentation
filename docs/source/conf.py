# Configuration file for the Sphinx documentation builder.

from recommonmark.parser import CommonMarkParser

source_parsers = {'.md': CommonMarkParser}

source_suffix = ['.rst', '.md']

# -- Project information

project = 'The MetaSUB CAMP'
copyright = '2022, MetaSUB Consortium'
author = 'Braden T Tierney, Lauren Mak'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
