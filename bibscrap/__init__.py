"""Semi-automated tools for systematic literature reviews."""

from gettext import gettext as _
from typing import AnyStr, Callable, Optional

import argparse
import importlib
import logging
import sys

__import__("pkg_resources").declare_namespace(__name__)

__version__ = "0.0.5.dev1"
__version_info__ = __version__.split(".")

logger = logging.getLogger(__name__)

builtin_extensions = [
    "bibscrap.fetch",
]


class BibscrapException(Exception):
    pass


class BibscrapApp:
    """The main application class and extensibility interface."""

    PROG = _("bibscrap")
    VERSION = __version__
    VERSION_INFO = __version_info__

    def __init__(self):
        self.arg_parser = argparse.ArgumentParser(
            prog=BibscrapApp.PROG,
            description=_("Semi-automated tools for systematic literature reviews."),
            epilog=_(
                """
            Submit bugs, issues, and feature requests at
            https://github.com/cotterell/bibscrap/issues.
            """
            ),
        )
        self.arg_parser.add_argument(
            "--version",
            action="version",
            version=f"{BibscrapApp.PROG} {BibscrapApp.VERSION}",
        )
        self.command_subparsers = self.arg_parser.add_subparsers(
            title="commands",
            dest="command",
            metavar="<command>",
            required=True,
        )
        self.commands = dict()

    def register_command(
        self,
        command: AnyStr,
        brief: AnyStr,
        description: AnyStr,
        func: Optional[Callable[["bibscrap.BibscrapApp"], None]] = None,
    ) -> argparse.ArgumentParser:
        """Register a Bibscrap command.

        Extensions can register command's for Bibscrap command-line
        interface::

            bibscrap <command> args ...

        Args:
            command: The command string.
            brief: A brief description of what the command does.
            description: Text to display before the command's help message.
            func: The function to call when the command is invoked.

        Returns:
            argparse.ArgumentParser: The argument parser for the registered
                Bibscrap command.
        """
        self.commands[command] = func
        return self.command_subparsers.add_parser(
            command,
            help=brief,
            description=description,
        )

    def load_builtin_extensions(self) -> None:
        """Load all of the extensions in :py:data:`bibscrap.builtin_extensions`.

        Raises:
            BibscrapException: If a module in ``bibscrap.builtin_extensions` is
                missing a ``setup(app)`` function.
        """
        for extension_name in builtin_extensions:
            extension = importlib.import_module(extension_name)
            if hasattr(extension, "setup"):
                extension.setup(self)
            else:
                raise BibscrapException(
                    f"{extension} is not a Bibscrap extension (missing setup(app))",
                )

    def command(self, args: "argparse.Namespace") -> None:
        """Execute a command registered by a Bibscrap extension.

        Args:
            args: A namespace containing command-line arguments for the command.

        Raises:
            BibscrapException: If invalid arguments are supplied.
        """
        try:
            func = self.commands.get(args.command, None)
            func(self, args)
        except Exception as e:
            raise BibscrapException()


app = BibscrapApp()
app.load_builtin_extensions()


def main() -> int:  # pragma: no cover
    args = app.arg_parser.parse_args()
    app.command(args)
    return 0


if __name__ == "__main__":
    sys.exit(bibscrap.main())
