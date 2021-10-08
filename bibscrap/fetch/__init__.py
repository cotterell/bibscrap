"""bibscrap.fetch - fetch references."""


def setup(app: "BibscrapApp") -> None:

    arg_parser = app.register_arg_parser(
        command="fetch",
        help="fetch references",
    )

    arg_parser.add_argument(
        "bar",
        type=int,
        help="bar help",
    )
