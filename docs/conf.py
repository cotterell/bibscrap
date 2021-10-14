from datetime import datetime

import importlib
import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

sys.path.insert(0, os.path.abspath(".."))  # bibscrap source code
sys.path.append(os.path.abspath("./_ext"))  # custom sphinx extensions

# -- Project information -----------------------------------------------------

project = "Bibscrap"
years = f"2020–{datetime.now().year}"
author = "Michael E. Cotterell"
copyright = f"{years}, {author} and the University of Georgia"
version = importlib.import_module("bibscrap").__version__
revision = os.popen("git rev-parse --short HEAD").read().strip()

licenses = {
    "documentation": {
        "name": "CC BY-NC 4.0",
        "url": "https://creativecommons.org/licenses/by-nc/4.0/",
    },
    "code": {
        "name": "MIT",
        "url": f"https://github.com/cotterell/bibscrap/blob/main/LICENSE.rst",
    },
}

# -- General configuration ---------------------------------------------------

# Refuse to build if Sphinx is too old.
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-needs_sphinx
needs_sphinx = "4.2"

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-extensions
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.todo",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx_rtd_theme",
    "sphinxcontrib.bibtex",
]

# Refuse to build if certain extensions are too old.
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-needs_extensions
needs_extensions = {
    "sphinxcontrib.bibtex": "2.4.1",
}

# Add any paths that contain templates here, relative to this directory.
templates_path = [
    "_templates",
]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files. This pattern also affects
# html_static_path and html_extra_path.
#
exclude_patterns = [
    "_build",  # output directory
    "_ext",  # custom Sphinx extensions
    "_templates",  # custom Sphinx templates
    "Thumbs.db",  # Windows thumbnail cache
    ".DS_Store",  # macOS Desktop Services Store
    "**/*~",  # Emacs backup file
    "**/#*#",  # Emaxs autosave file
]

rst_prolog = """
.. role:: python(code)
   :class: highlight
   :language: python

.. _issue_tracker: https://github.com/cotterell/bibscrap/issues
.. _issue_tracker_new: https://github.com/cotterell/bibscrap/issues/new/choose

.. admonition:: Development Status :: 2 - Pre-Alpha
   :class: danger alert

   Bibscrap is still in its **pre-alpha** development phase. This is the
   earliest stage of software development. The project is still establishing its
   requirement, and it contains code that is not yet feature-complete.

----
"""

rst_epilog = """
.. |LaTeX| replace:: :math:`{\mathrm{\LaTeX}}`
.. |BibTeX| replace:: :math:`{\mathrm{B{\scriptstyle{IB}} \! T\!_{\displaystyle E} \! X}}`
"""

# -- Options for sphinx.ext.autosectionlabel ----------------------------------

autosectionlabel_prefix_document = True

# -- Options for sphinx.ext.extlinks -----------------------------------------

extlinks = {
    "issue": (
        "https://github.com/cotterell/bibscrap/issues/%s",
        "issue %s",
    ),
    "docs_latest": (
        "https://bibscrap.readthedocs.io/en/latest/%s.html",
        "https://bibscrap.readthedocs.io/en/latest/%s.html",
    ),
}

# -- Options for sphinx.ext.intersphinx --------------------------------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_theme
html_theme = "sphinx_rtd_theme"

html_logo = "_static/img/bibscrap.svg"

# Dictionary of options that influence the look and feel of the selected theme.
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_theme_options
# https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html#theme-options
html_theme_options = {
    "logo_only": True,
    "includehidden": False,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    "vcs_pageview_mode": "blob",
    "style_nav_header_background": "var(--uga-creamery)",
}

# Dictionary of values to pass into the template engine’s context for all pages.
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_context
html_context = {
    "licenses": licenses,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_static_path
html_static_path = [
    "_static",
]

# A list of CSS files. The entry must be a *filename* string or a tuple
# containing the *filename* string and the *attributes* dictionary. The
# *filename* must be relative to the ``html_static_path``, or a full URI with
# scheme (eg. ``"https://..."``). The *attributes* dictionary is used to set
# attributes of the corresponding ``<link>`` tag (it defaults to an empty list).
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_css_files
html_css_files = [
    "css/colors.css",
    "css/rtd.css",
    "css/todolist.css",
    "css/refs.css",
]

# -- Options for sphinx.ext.todo ---------------------------------------------

# If ``todo_include_todos`` is ``True``, the ``.. todo::`` and ``.. todolist::``
# directives produce output, else they produce nothing (default is ``False``).
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#confval-todo_include_todos
todo_include_todos = True

# If ``todo_link_only`` is ``True``, the ``.. todolist::`` directive produces
# output without file path and line (default is ``False``).
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#confval-todo_link_only
todo_link_only = True

# -- Options for sphinxcontrib-bibtex ----------------------------------------

bibtex_bibfiles = [
    "refs.bib",
]

bibtex_default_style = "plain"

# -- Options for sphinx.ext.autodoc ------------------------------------------

autodoc_typehints = "both"

autoclass_content = "both"

autodoc_type_aliases = {
    "Command": "bibscrap.app.Command",
}
