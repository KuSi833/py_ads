from typing import Union, TypeVar, Any
from typing_extensions import TypeAlias, Protocol
from abc import abstractmethod

Value: TypeAlias = Union[str, int, float, complex, bool]
C = TypeVar("C", bound="Comparable")
A = TypeVar("A", bound="Addable")
AC = TypeVar("AC", bound="AddableAndComparable")


class Comparable(Protocol):
    @abstractmethod
    def __eq__(self, other: Any) -> bool:
        pass

    @abstractmethod
    def __lt__(self: C, other: C) -> bool:
        pass

    def __gt__(self: C, other: C) -> bool:
        return (not self < other) and self != other

    def __le__(self: C, other: C) -> bool:
        return self < other or self == other

    def __ge__(self: C, other: C) -> bool:
        return (not self < other)


class Addable(Protocol):
    @abstractmethod
    def __add__(self, other):
        pass


class AddableAndComparable(Comparable, Addable):
    pass
