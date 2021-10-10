"""The `bibscrap.app` module provides the :py:class:`BibscrapApp` class."""

from __future__ import annotations
from bibscrap.errors import BibscrapError, BibscrapExtensionTypeError
from gettext import gettext as _
from typing import Callable, NewType, Optional, Union
from types import ModuleType

import argparse
import importlib
import logging
import sys

#: The list of Bibscrap extension modules that are loaded by
#: :py:func:`BibscrapApp.load_builtin_extensions`.
builtin_extensions = [
    "bibscrap.fetch",
]


class BibscrapApp:
    """The main application class and extensibility interface."""

    PROG = _("bibscrap")
    VERSION = None
    VERSION_INFO = None

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
        self.command_parsers = self.arg_parser.add_subparsers(
            title="commands",
            dest="command",
            metavar="<command>",
            required=True,
        )
        self.commands = dict()

    def register_command(
        self,
        command: str,
        brief: str,
        description: str,
        func: Callable[["BibscrapApp"], None],
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
        return self.command_parsers.add_parser(
            command,
            help=brief,
            description=description,
        )

    def load_extension(self, module: Union[str, ModuleType]) -> None:
        """Load a Bibscrap extension module.

        Bibscrap extension modules are regular Python modules that contain
        the following module-level function:

        .. code:: python

            def setup(app: BibscrapApp) -> None:
                ...

        If `module` was created since the interpreter began execution, then you
        may need to call :python:`importlib.invalidate_caches` in order for the
        new module to be noticed by the import system.

        Args:
            module: The Bibscrap extension module to load.

        Raises:
            BibscrapExtensionTypeError: If the module is missing a ``setup(app)``
                function.
        """
        if isinstance(module, str):
            extension = importlib.import_module(module)
        elif isinstance(module, ModuleType):
            extension = module

        if hasattr(extension, "setup"):
            extension.setup(self)
        else:
            raise BibscrapExtensionTypeError(
                f"{extension} is not a Bibscrap extension (missing setup(app))",
            )

    def load_builtin_extensions(self) -> None:
        """Load all of the extensions in :py:data:`bibscrap.builtin_extensions`."""
        for module in builtin_extensions:
            self.load_extension(module)

    def command(self, args: "argparse.Namespace") -> None:
        """Execute a command registered by a Bibscrap extension.

        Args:
            args: A namespace containing command-line arguments for the command.

        Raises:
            BibscrapError: If invalid arguments are supplied.
        """
        try:
            func = self.commands.get(args.command, None)
            func(self, args)
        except Exception as e:
            raise BibscrapError()
