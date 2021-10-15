from typing import Callable
from typing import Optional
from typing import Type
from typing import TypeVar


T = TypeVar("T")


def get_optional(arg: Optional[T]) -> T:
    """Return the value for `arg` if not :py:const:`None`, else raise an :py:exc:`AssertionError`.

    Args:
        arg: The :py:class:`Optional`.

    Returns:
        The value held by `arg`.

    Raises:
        AssertionError: If there is no value present in `arg` (i.e., ``arg is None``).

    References:
        `@gvanrossum <https://github.com/gvanrossum>`__ Jun 11, 2019. Comment in
        `python/typing#645 <https://github.com/python/typing/issues/645#issuecomment-501057220>`__.
    """
    assert arg is not None
    return arg
