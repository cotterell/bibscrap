import argparse
import bibscrap
import sys


def main(args: list = None) -> int:
    print("Coming soon!")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="bibscrap",
        description="Semi-automated tools for systematic literature reviews.",
        epilog="""Submit bugs, issue, and feature requests at
        https://github.com/cotterell/bibscrap/issues.
        """,
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {bibscrap.__version__}",
    )
    args = parser.parse_args()
    sys.exit(main(args))
