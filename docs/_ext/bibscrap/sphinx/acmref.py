"""ACM Reference Format style for |sphinxcontrib_bibtex|_.

The :mod:`bibscrap.sphinx.acmref` module provides a configurable |pybtex|_ style
class (``ACMRefStyle``) that closely mimics the |acm_style|_ described in
:cite:t:`acmart`, the public domain |LaTeX| package for typesetting publications
of the |acm|_ using |BibTeX|. The module itself is also a Sphinx extension that
registers the styles for use by the |sphinxcontrib_bibtex|_ extension.

.. |acm_style| replace:: ACM Citation Style and Reference Formats
.. _acm_style: https://www.acm.org/publications/authors/reference-formatting

.. |sphinxcontrib_bibtex| replace:: sphinxcontrib-bibtex
.. _sphinxcontrib_bibtex: https://github.com/mcmtroffaes/sphinxcontrib-bibtex

.. |pybtex| replace:: Pybtex
.. _pybtex: https://pybtex.org/

.. |acm| replace:: Association for Computing Machinery
.. _acm: https://www.acm.org/
"""

from enum import Enum, unique, auto
from pybtex import plugin as pybtex_plugin
from pybtex.style.formatting import unsrt
from sphinx.locale import __
from sphinx.util import logging
from sphinx.util.console import bold

INTERACTIVE = True

logger = logging.getLogger(__name__)

ABBREVIATIONS = {
    "ACM Computing Surveys": "Comput. Surveys",
    "ACM Transactions on Mathematical Software": "ACM Trans. Math. Software",
    "ACM SIGNUM Newsletter": "ACM SIGNUM Newslett.",
    "American Journal of Sociology": "Amer. J. Sociology",
    "American Mathematical Monthly": "Amer. Math. Monthly",
    "American Mathematical Society Translations": "Amer. Math. Soc. Transl.",
    "Applied Mathematics and Computation": "Appl. Math. Comput.",
    "British Journal of Mathematical and Statistical Psychology": "Brit. J. Math. Statist. Psych.",
    "Bulletin of the American Mathematical Society": "Bull. Amer. Math. Soc.",
    "Canadian Mathematical Bulletin": "Canad. Math. Bull.",
    "Communications of the ACM": "Commun. ACM",
    "Communications of the {ACM}": "Commun. ACM",
    "Computers and Structures": "Comput. & Structures",
    "Contemporary Mathematics": "Contemp. Math.",
    "Crelle's Journal": "Crelle's J.",
    "Giornale di Mathematiche": "Giorn. Mat.",
    "IEEE Transactions on Aerospace and Electronic Systems": "IEEE Trans. Aerospace Electron. Systems",
    "IEEE Transactions on Automatic Control": "IEEE Trans. Automat. Control",
    "IEEE Transactions on Computers": "IEEE Trans. Comput.",
    "IMA Journal of Numerical Analysis": "IMA J. Numer. Anal.",
    "Information Processing Letters": "Inform. Process. Lett.",
    "International Journal for Numerical Methods in Engineering": "Internat. J. Numer. Methods Engrg.",
    "International Journal of Control": "Internat. J. Control",
    "International Journal of Supercomputing Applications": "Internat. J. Supercomputing Applic.",
    "Journal of Computational Physics": "J. Comput. Phys.",
    "Journal of Computational and Applied Mathematics": "J. Comput. Appl. Math.",
    "Journal of Computer and System Sciences": "J. Comput. System Sci.",
    "Journal of Mathematical Analysis and Applications": "J. Math. Anal. Appl.",
    "Journal of Mathematical Physics": "J. Math. Phys.",
    "Journal of Parallel and Distributed Computing": "J. Parallel and Distrib. Comput.",
    "Journal of Research of the National Bureau of Standards": "J. Res. Nat. Bur. Standards",
    "Journal of VLSI and Computer Systems": "J. VLSI Comput. Syst.",
    "Journal of {VLSI} and Computer Systems": "J. VLSI Comput. Syst.",
    "Journal of the ACM": "J. ACM",
    "Journal of the American Statistical Association": "J. Amer. Statist. Assoc.",
    "Journal of the Institute of Mathematics and its Applications": "J. Inst. Math. Appl.",
    "Journal of the Society for Industrial and Applied Mathematics": "J. Soc. Indust. Appl. Math.",
    "Journal of the Society for Industrial and Applied Mathematics, Series B, Numerical Analysis": "J. Soc. Indust. Appl. Math. Ser. B Numer. Anal.",
    "Linear Algebra and its Applications": "Linear Algebra Appl.",
    "Mathematica Scandinavica": "Math. Scand.",
    "Mathematical Tables and Other Aids to Computation": "Math. Tables Aids Comput.",
    "Mathematics of Computation": "Math. Comp.",
    "Mathematische Annalen": "Math. Ann.",
    "Numerische Mathematik": "Numer. Math.",
    "Pacific Journal of Mathematics": "Pacific J. Math.",
    "Parallel Computing": "Parallel Comput.",
    "Philosophical Magazine": "Philos. Mag.",
    "Proceedings of the American Mathematical Society": "Proc. Amer. Math. Soc.",
    "Proceedings of the IEEE": "Proc. IEEE",
    "Proceedings of the {IEEE}": "Proc. IEEE",
    "Proceedings of the National Academy of Sciences of the USA": "Proc. Nat. Acad. Sci. U. S. A.",
    "Quarterly Journal of Mathematics, Oxford, Series (2)": "Quart. J. Math. Oxford Ser. (2)",
    "Quarterly of Applied Mathematics": "Quart. Appl. Math.",
    "Review of the International Statisical Institute": "Rev. Inst. Internat. Statist.",
    "SIAM Journal on Algebraic and Discrete Methods": "SIAM J. Algebraic Discrete Methods",
    "SIAM Journal on Applied Mathematics": "SIAM J. Appl. Math.",
    "SIAM Journal on Computing": "SIAM J. Comput.",
    "SIAM Journal on Matrix Analysis and Applications": "SIAM J. Matrix Anal. Appl.",
    "SIAM Journal on Numerical Analysis": "SIAM J. Numer. Anal.",
    "SIAM Journal on Scientific and Statistical Computing": "SIAM J. Sci. Statist. Comput.",
    "SIAM Review": "SIAM Rev.",
    "Software Practice and Experience": "Software Prac. Experience",
    "Statistical Science": "Statist. Sci.",
    "The Computer Journal": "Comput. J.",
    "Transactions of the American Mathematical Society": "Trans. Amer. Math. Soc.",
    "USSR Computational Mathematics and Mathematical Physics": "U. S. S. R. Comput. Math. and Math. Phys.",
    "Zeitschrift fur Angewandte Mathematik und Mechanik": "Z. Angew. Math. Mech.",
    "Zeitschrift fur Angewandte Mathematik und Physik": "Z. Angew. Math. Phys.",
}  # ABBREVIATIONS


class ACMRefStyle(unsrt.Style):
    """ACM Reference Format style.

    Args:
        abbreviate (bool) : Whether or not to convert ``journal`` and
            ``booktitle`` entry keys to their canonical abbreviations, defaults
            to :python:`False`.
    """

    def __init__(self, abbreviate: bool = False):
        super().__init__()

    def format_names(self, role, as_sentence=True):
        """ """
        return super().format_names(role, as_sentence)


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
