from .command import Command


class AboutCommand(Command):

    name = "about"

    description = "Shows information about Bibscrap."

    def handle(self) -> None:
        self.info(
            "Bibscrap - Semi-automated Tools for Systematic Literature Reviews</info>"
        )
        self.line_blank()
        self.comment(
            "Bibscrap provides tools that help researchers prepare rigorous systematic "
            "literature reviews."
        )
        self.line_blank()
        self.comment(
            "See <fg=blue>https://github.com/cotterell/bibscrap/</fg> for more information."
        )
