"""Semi-automated tools for systematic literature reviews."""

from __future__ import annotations
from bibscrap.app import BibscrapApp
from gettext import gettext as _

import logging
import sys

__import__("pkg_resources").declare_namespace(__name__)

__version__ = "0.0.6-dev0"
__version_info__ = __version__.split(".")

__logger = logging.getLogger(__name__)

__app = BibscrapApp()
__app.VERSION = __version__
__app.VERSION_INFO = __version_info__
__app.load_builtin_extensions()


def __arg_parser() -> argparse.ArgumentParser:  # pragma: no cover
    return __app.arg_parser


def main() -> int:  # pragma: no cover
    args = __app.arg_parser.parse_args()
    __app.command(args)
    return 0


if __name__ == "__main__":
    sys.exit(bibscrap.main())
