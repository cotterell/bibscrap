"""Semi-automated tools for systematic literature reviews."""

import argparse

__import__("pkg_resources").declare_namespace(__name__)

__version__ = "0.0.3.dev3"

__arg_parser = argparse.ArgumentParser(
    prog="bibscrap",
    description="Semi-automated tools for systematic literature reviews.",
    epilog="""
Submit bugs, issue, and feature requests at
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
    print("Coming soon!")
    return 0
