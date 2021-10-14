"""bibscrap.fetch - fetch references."""

from __future__ import annotations


def command(app: BibscrapApp, args: dict) -> None:
    print("fetching.....")
    print(args)


def setup(app: BibscrapApp) -> dict:

    arg_parser = app.register_command(
        command="fetch",
        brief="Fetch references.",
        description="Fetch references for a set of articles across a number of horizons.",
        func=command,
    )

    arg_parser.add_argument(
        "h",
        type=int,
        help="The number of horizons.",
    )

    return {
        "version": "0.1.1",
    }
