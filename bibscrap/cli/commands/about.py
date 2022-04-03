"""about.py - 'bibscrap about' command module."""

from .command import Command


class AboutCommand(Command):
    """The 'bibscrap about' command."""

    name = "about"

    description = "Shows information about Bibscrap."

    def handle(self) -> None:
        """Execute the command."""
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
