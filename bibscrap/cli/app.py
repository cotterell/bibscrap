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


def load_command(name: str) -> Callable:
    """TODO."""

    def _load() -> Type[Command]:
        module = import_module(f"{BUILTIN_COMMANDS_MODULE}.{name}")
        command_class = getattr(module, f"{name.title()}Command")
        return command_class()

    return _load


class Application(CleoApplication):
    """Bibscrap application class."""

    def __init__(self) -> None:
        super().__init__("bibscrap", get_optional(__version__))
        self.set_command_loader(
            CommandLoader({name: load_command(name) for name in BUILTIN_COMMANDS}),
        )


def main() -> int:
    return Application().run()


if __name__ == "__main__":
    main()
