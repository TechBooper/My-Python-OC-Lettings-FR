# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'oc_lettings_site_doc'
copyright = '2025, 1057'
author = '1057'
release = '10/01/2025'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # If you use Google or NumPy docstrings
    'sphinx.ext.autosummary'
]

autosummary_generate = True  # To let Sphinx generate stubs

templates_path = ['_templates']
exclude_patterns = ["venv/*",
    "_build",
    "Thumbs.db",
    ".DS_Store",
    ]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
