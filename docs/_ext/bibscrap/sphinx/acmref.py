"""ACM Reference Format style for |sphinxcontrib_bibtex|_.

The :mod:`bibscrap.sphinx.acmref` module provides a configurable |pybtex|_ style
class (``ACMRefStyle``) that closely mimics the |acm_style|_ described in
:cite:t:`acmart`, the public domain |LaTeX| package for typesetting publications
of the |acm|_ using |BibTeX|. The module itself is also a Sphinx extension that
registers the styles for use by the |sphinxcontrib_bibtex|_ extension.

Install the module with pip install sphinxcontrib-bibtex, or from source using pip install -e .. Then add:

extensions = ['sphinxcontrib.bibtex']

.. |acm_style| replace:: ACM Citation Style and Reference Formats
.. _acm_style: https://www.acm.org/publications/authors/reference-formatting

.. |sphinxcontrib_bibtex| replace:: sphinxcontrib-bibtex
.. _sphinxcontrib_bibtex: https://github.com/mcmtroffaes/sphinxcontrib-bibtex

.. |pybtex| replace:: Pybtex
.. _pybtex: https://pybtex.org/

.. |acm| replace:: Association for Computing Machinery
.. _acm: https://www.acm.org/
"""

from pybtex import plugin as pybtex_plugin
from pybtex.style.formatting import unsrt
from sphinx.locale import __
from sphinx.util import logging
from sphinx.util.console import bold

logger = logging.getLogger(__name__)


class ACMRefStyle(unsrt.Style):
    """ACM Reference Format style."""

    def __init__(self):
        super().__init__()


def setup(app):
    logger.info(
        bold(__("enabling 'acmref' style for sphinxcontrib-bibtex... ")), nonl=True
    )
    app.require_sphinx("4.1")
    app.setup_extension("sphinxcontrib.bibtex")
    pybtex_plugin.register_plugin("pybtex.style.formatting", "acmref", ACMRefStyle)
    logger.info(__("done"))
    return {
        "version": "0.0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
