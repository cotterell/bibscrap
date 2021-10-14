"""The `bibscrap.app` module provides the :py:class:`BibscrapApp` class."""

from __future__ import annotations
from bibscrap.errors import BibscrapError, BibscrapExtensionTypeError
from gettext import gettext as _
from typing import Callable, NewType, Optional, Union
from types import ModuleType

import argparse
import bibscrap
import importlib
import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#: The list of Bibscrap extension modules that are loaded by
#: :py:func:`BibscrapApp.load_builtin_extensions`.
builtin_extensions = [
    "bibscrap.fetch",
]


class BibscrapCommand:
    def __init__(self, **kwargs):
        pass


class BibscrapApp:
    """The main application class and extensibility interface."""

    def __init__(self):
        self.__prog = _("bibscrap")
        self.__version = bibscrap.__version__
        self.__version_info = bibscrap.__version_info__
        self.__init_arg_parsers()
        self.__extensions = dict()
        self.commands = dict()

    def __init_arg_parsers(self):
        self.arg_parser = argparse.ArgumentParser(
            prog=self.__prog,
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
            version=f"{self.prog} {self.version}",
        )
        self.command_parsers = self.arg_parser.add_subparsers(
            title="commands",
            dest="command",
            metavar="<command>",
            required=True,
        )

    @property
    def prog(self) -> str:
        return self.__prog

    @property
    def version(self) -> str:
        return self.__version

    @property
    def extensions(self) -> list:
        """list: List of loaded extensions."""
        return [
            (name, record.get("version", None))
            for name, record in self.__extensions.items()
        ]

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

    def load_extension(self, name: str, package: str = None) -> None:
        """Load a Bibscrap extension module.

        Bibscrap extension modules are regular Python modules that contain
        the following module-level function:

        .. code:: python

            def setup(app: BibscrapApp) -> BibscrapExtension:
                ...

        If `module` was created since the interpreter began execution, then you
        may need to call :python:`importlib.invalidate_caches` in order for the
        new module to be noticed by the import system.

        Args:
            module: The Bibscrap extension module to load.
        """
        extension = importlib.import_module(name, package)
        extension_name = extension.__name__
        extension_info = extension.setup(self)
        self.__extensions[extension_name] = extension_info

    def load_builtin_extensions(self) -> None:
        """Load all of the extensions in :py:data:`bibscrap.builtin_extensions`."""
        for module in builtin_extensions:
            self.load_extension(module)

    def execute_command(self, args: dict) -> None:
        """Execute a command registered by a Bibscrap extension.

        Args:
            args: A namespace containing command-line arguments for the command.

        Raises:
            BibscrapError: If invalid arguments are supplied.
        """
        try:
            command = args.get("command")
            func = self.commands.get(command, None)
            func(self, args)
        except Exception as e:
            raise BibscrapError()
