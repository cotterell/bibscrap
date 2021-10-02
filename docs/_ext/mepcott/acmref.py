from sphinx.util import logging
from sphinx.util.console import bold

logger = logging.getLogger(__name__)


def setup(app):
    logger.info(
        bold(f"enabling ACM Reference Format (acmref) for sphinxcontrib-bibtex... ")
        + "done"
    )
    app.setup_extension("sphinxcontrib.bibtex")
    app.require_sphinx("4.1")
    return {
        "version": "0.0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
