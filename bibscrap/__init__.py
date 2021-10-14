from pathlib import Path
from pkgutil import extend_path
from single_source import get_version
from typing import List, Optional

__path__: List[str] = extend_path(__path__, __name__)
__version__: Optional[str] = get_version(__name__, Path(__file__).parent.parent)
