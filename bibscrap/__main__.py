"""bibscrap (main) - The top-level Bibscrap code environment."""

import sys

if __name__ == "__main__":
    from .cli.app import main

    sys.exit(main())
