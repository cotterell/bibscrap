"""Defines the API for Bibscrap's command-line interface (CLI) application."""

from importlib import import_module
from typing import TYPE_CHECKING
from typing import Callable
from typing import Optional
from typing import Type

from cleo.application import Application as CleoApplication
from cleo import commands as cleo_commands

from bibscrap import __version__
from bibscrap.cli.commands import CommandLoader
from bibscrap.cli.commands.command import Command

BUILTIN_COMMANDS_MODULE = "bibscrap.cli.commands"

BUILTIN_COMMANDS = [
    "about",
]


class Application(CleoApplication):
    """Bibscrap application class."""

    def __init__(self) -> None:
        """Construct a Bibscrap ``Application`` object."""
        super().__init__("bibscrap", __version__)
        self.set_command_loader(CommandLoader())
        for builtin_command in BUILTIN_COMMANDS:
            self.register_builtin_command(builtin_command)
        self.unhide_completions_command()
        self.auto_exits(False)

    def unhide_completions_command(self) -> None:
        """Unhide the "completions" command provided by Cleo."""
        completions_class = cleo_commands.completions_command.CompletionsCommand
        completions_command = self.get(completions_class.name)
        completions_command.hidden = False

    def register_command(
        self,
        command: str,
        command_class: str,
        module: Optional[str] = None,
        package: Optional[str] = None,
    ) -> None:
        """Register a command with the command loader.

        Args:
            command: The command to register.
            command_class: The command's :py:class:`Command` class name.
            module: The module containing the command's :py:class:`Command` class. If
                :py:const:`None`, then `command_class` must be a fully qualified name.
            package: Used to anchor the import when `module` is specified in relative terms.
        """
        command_class, module, package = self.command_loader.resolve(
            command_class, module, package
        )

        def _deferred() -> Callable:
            imported_module = import_module(module, package)
            imported_command_class = getattr(imported_module, command_class)
            return imported_command_class()

        self.command_loader.register_factory(command, _deferred)

    def register_builtin_command(self, command: str) -> None:
        """Register a builtin Bibscrap command.

        Args:
            command: The builtin command to register.
        """
        parts = command.split(" ")
        submodule = ".".join(parts)
        command_class = "{}Command".format("".join(map(str.title, parts)))
        fqn = f"{BUILTIN_COMMANDS_MODULE}.{submodule}.{command_class}"
        self.register_command(command, fqn)

    @property
    def command_loader(self) -> CommandLoader:
        """Return the application's command loader."""
        return self._command_loader


def main() -> int:
    """Execute Bibscrap's command-line interface (CLI) application."""
    app = Application()
    exit_status = app.run()
    return exit_status
