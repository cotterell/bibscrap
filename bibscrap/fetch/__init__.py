"""bibscrap.fetch - fetch references."""


def command(app: "bibscrap.BibscrapApp", args: "argparse.Namespace") -> None:
    print("fetching...")
    print(args)


def setup(app: "bibscrap.BibscrapApp") -> None:

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
