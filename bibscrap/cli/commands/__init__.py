"""bibscrap.cli.commands - builtin Bibscrap commands."""

from typing import Callable
from typing import Dict
from typing import Optional
from typing import Tuple

from cleo.exceptions import LogicException
from cleo.loaders.factory_command_loader import FactoryCommandLoader


class CommandLoader(FactoryCommandLoader):
    """Bibscrap's command loader using factories to instantiate commands lazily."""

    def __init__(self, factories: Dict[str, Callable] = {}) -> None:
        """Construct a ``CommandLoader`` object.

        Args:
            factories: A mapping from command names to their callable factories.
        """
        super().__init__(factories)

    def resolve(
        self,
        command_class: str,
        module: Optional[str] = None,
        package: Optional[str] = None,
    ) -> Tuple[str, str, Optional[str]]:
        """Resolve the class name, module, and package for a Bibscrap command.

        If ``module`` is ``None``, then ``command_class`` is assumed to be the
        fully-qualified name (FQN) of the command's class.

        Args:
            command_class: Command class name or FQN.
            module: Module name.
            package: Package name.
        """
        if module is None:  # command_class is an FQN
            fqn_parts = command_class.split(".")
            module = ".".join(fqn_parts[:-1])  # all but last part
            command_class = fqn_parts[-1]  # last part

        return command_class, module, package

    def register_factory(self, command_name: str, factory: Callable) -> None:
        """Register a callable factory for a Bibscrap command.

        Args:
            command_name: Command name.
            factory: Command factory.
        """
        if command_name in self._factories:
            raise LogicException(f'The command "{command_name}" already exists.')

        self._factories[command_name] = factory
