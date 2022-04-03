"""bibscrap.core.models - Bibscrap core data models."""

import builtins
import numbers
import typing

from datetime import date
from enum import Enum
from typing import NewType
from typing import NewType
from typing import Optional


class Identifier:
    """A value used to identify something."""

    value: str

    def __init__(self, value) -> None:
        """Construct an ``Identifier`` object."""
        self.value = value

    def resolve(self):
        """Resolve the identifier's value."""
        return self.value


class DOI(Identifier):
    """Digital Object Identifier."""

    RESOLVERS = {
        "doi.org": "https://doi.org/",
        "dx.doi.org": "https://dx.doi.org/",
        "hdl.handle.net": "http://hdl.handle.net/",
    }


class ISBN(Identifier):
    """The ISBN of the book."""

    pass


class BibItem:
    """The most generic type of item."""

    #: The name of the item.
    name: str

    #: A description of the item.
    description: str

    #:
    identifiers: list[Identifier]

    #: URL of a reference Web page that unambiguously indicates the item's
    #: identity. E.g. the URL of the item's Wikipedia page, Wikidata entry, or
    #: official website.
    sameAs: str


class CreativeWork:
    """The most generic kind of creative work."""

    pass
