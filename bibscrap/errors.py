"""Bibscrap-related errors."""


class BibscrapError(Exception):
    """The base class for the exceptions that are raised by Bibscrap."""

    pass


class BibscrapExtensionTypeError(BibscrapError, TypeError):
    """Raised when `load_extension` imports a module that is not a Bibscrap extension module."""

    pass
