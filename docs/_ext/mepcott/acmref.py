from pybtex import plugin as pybtex_plugin
from pybtex.style.formatting import unsrt
from sphinx.locale import __
from sphinx.util import logging
from sphinx.util.console import bold

logger = logging.getLogger(__name__)


class ACMRefStyle(unsrt.Style):
    """..."""

    pass


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
