"""
.. versionadded:: 1.0.0

   Initial :ref:`api:Public API` release.

"""

from pathlib import Path
from pkgutil import extend_path
from single_source import get_version
from typing import cast, List

__path__: List[str] = extend_path(__path__, __name__)

#: Bibscrap :ref:`version <api:Versions>` number.
__version__: str = cast(str, get_version(__name__, Path(__file__).parent.parent))
