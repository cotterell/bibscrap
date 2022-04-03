from .command import Command


class AboutCommand(Command):

    name = "about"

    description = "Shows information about Bibscrap."

    def handle(self) -> None:
        self.line(
            "<info>Bibscrap - Semi-automated Tools for Systematic Literature Reviews</info>"
        )
        self.line_blank()
        self.line(
            "<comment>"
            "Bibscrap provides tools that help researchers prepare rigorous systematic "
            "literature reviews."
            "</comment>"
        )
        self.line_blank()
        self.render_table(
            headers=["Resource", "URL"],
            rows=[
                ["Documentation", "<info>https://bibscrap.readthedocs.io/</info>"],
                ["GitHub", "<info>https://github.com/cotterell/bibscrap</info>"],
            ],
        )
