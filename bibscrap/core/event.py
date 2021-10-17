"""Provides the :py:mod:`asyncio` framework for Bibscrap events, their delivery, and handling."""

from abc import ABC
from abc import abstractmethod
from typing import Awaitable
from typing import Callable
from typing import Generic
from typing import TypeVar


class Event(ABC):
    """The base class for all event objects."""

    pass


#: Generic type variable for :py:class:`Event` objects.
EventType = TypeVar("EventType", bound=Event)

#: Type of a :py:class:`Callable` that handles some :py:data:`EventType`.
EventHandler = Callable[[EventType], Awaitable[None]]


class EventExecutor(ABC):
    """Represents objects that execute :py:data:`EventHandler` functions."""

    @abstractmethod
    async def execute(self, handler: EventHandler, event: EventType) -> None:
        """Calls ``handler(event)`` at some time in the future.Dispatches the specified `event`."""
        pass
