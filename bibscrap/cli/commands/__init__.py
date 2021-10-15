from typing import Callable
from typing import Dict
from typing import Optional
from typing import Tuple

from cleo.exceptions import LogicException
from cleo.loaders.factory_command_loader import FactoryCommandLoader


class CommandLoader(FactoryCommandLoader):
    def __init__(self, factories: Dict[str, Callable] = {}) -> None:
        super().__init__(factories)

    def resolve(
        self,
        command_class: str,
        module: Optional[str] = None,
        package: Optional[str] = None,
    ) -> Tuple[str, str, Optional[str]]:
        if module is None:  # command_class is an FQN
            fqn_parts = command_class.split(".")
            module = ".".join(fqn_parts[:-1])  # all but last part
            command_class = fqn_parts[-1]  # last part

        return command_class, module, package

    def register_factory(self, command_name: str, factory: Callable) -> None:
        if command_name in self._factories:
            raise LogicException(f'The command "{command_name}" already exists.')

        self._factories[command_name] = factory
