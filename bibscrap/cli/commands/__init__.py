from typing import Callable
from typing import Dict

from cleo.exceptions import LogicException
from cleo.loaders.factory_command_loader import FactoryCommandLoader


class CommandLoader(FactoryCommandLoader):
    def __init__(self, factories: Dict[str, Callable] = {}) -> None:
        super().__init__(factories)

    def register_factory(self, command_name: str, factory: Callable) -> None:
        if command_name in self._factories:
            raise LogicException(f'The command "{command_name}" already exists.')

        self._factories[command_name] = factory
