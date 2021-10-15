from __future__ import annotations

from cleo.commands.command import Command as BaseCommand


class Command(BaseCommand):
    """Bibscrap command class."""

    def line_blank(self) -> None:
        """Write a blank line as output."""
        self.line("")
