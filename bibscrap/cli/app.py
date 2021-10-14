from importlib import import_module
from typing import Optional

from bibscrap import __version__
from bibscrap.util import get_optional

from cleo.application import Application as CleoApplication
from cleo.io.io import IO


class Application(CleoApplication):
    """Application."""

    def __init__(self) -> None:
        super().__init__("bibscrap", get_optional(__version__))


def main() -> int:
    return Application().run()


if __name__ == "__main__":
    main()
