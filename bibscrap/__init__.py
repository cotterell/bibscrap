"""Semi-automated tools for systematic literature reviews."""

import argparse

__import__("pkg_resources").declare_namespace(__name__)

__version__ = "0.0.4.dev1"
__version_info__ = __version__.split(".")

__arg_parser = argparse.ArgumentParser(
    prog="bibscrap",
    description="Semi-automated tools for systematic literature reviews.",
    epilog="""
Submit bugs, issues, and feature requests at
https://github.com/cotterell/bibscrap/issues.
""",
)

__arg_parser.add_argument(
    "--version",
    action="version",
    version=f"%(prog)s {__version__}",
)


def main() -> int:
    args = __arg_parser.parse_args()
    __arg_parser.parse_args(["--version"])
    return 0
