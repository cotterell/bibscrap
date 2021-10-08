"""Semi-automated tools for systematic literature reviews."""

import abc
import argparse
import importlib

__import__("pkg_resources").declare_namespace(__name__)

__version__ = "0.0.5.dev0"
__version_info__ = __version__.split(".")

DEFAULT_EXTENSIONS = [
    "bibscrap.fetch",
]


class BibscrapApp:

    VERSION = __version__
    VERSION_INFO = __version_info__

    def __init__(self):
        self.arg_parser = argparse.ArgumentParser(
            prog="bibscrap",
            description="Semi-automated tools for systematic literature reviews.",
            epilog="""
            Submit bugs, issues, and feature requests at
            https://github.com/cotterell/bibscrap/issues.
            """,
        )
        self.arg_parser.add_argument(
            "--version",
            action="version",
            version=f"%(prog)s {BibscrapApp.VERSION}",
        )
        self.command_subparsers = self.arg_parser.add_subparsers(
            title="command",
            metavar="<command>",
            description="These are common Bibscrap commands used in various situations:",
        )

    def register_arg_parser(
        self, command: str, help: str = None, description: str = None
    ) -> argparse.ArgumentParser:
        return self.command_subparsers.add_parser(
            command,
            help=help,
            description=description,
        )


__app = BibscrapApp()

for extension_name in DEFAULT_EXTENSIONS:
    extension = importlib.import_module(extension_name)
    extension.setup(__app)


def main() -> int:
    args = __app.arg_parser.parse_args()
    __app.arg_parser.parse_args(["--version"])
    return 0
