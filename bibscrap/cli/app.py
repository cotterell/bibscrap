from importlib import import_module
from typing import TYPE_CHECKING
from typing import Callable
from typing import Optional
from typing import Type

from cleo.application import Application as CleoApplication

from bibscrap import __version__
from bibscrap.cli.commands import CommandLoader
from bibscrap.cli.commands.command import Command
from bibscrap.util import get_optional

BUILTIN_COMMANDS_MODULE = "bibscrap.cli.commands"

BUILTIN_COMMANDS = [
    "about",
]


class Application(CleoApplication):
    """Bibscrap application class."""

    def __init__(self) -> None:
        super().__init__("bibscrap", get_optional(__version__))
        self.set_command_loader(CommandLoader())
        for name in BUILTIN_COMMANDS:
            self.load_command(name)

    def load_command(self, name: str) -> Callable:
        """TODO."""
        module = import_module(f"{BUILTIN_COMMANDS_MODULE}.{name}")
        command_class = getattr(module, f"{name.title()}Command")
        self.command_loader.register_factory(name, command_class)

    @property
    def command_loader(self) -> CommandLoader:
        return self._command_loader


def main() -> int:
    return Application().run()


if __name__ == "__main__":
    main()
