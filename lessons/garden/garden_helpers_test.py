"""Test my garden functions."""

__author__ = "730720425"

from lessons.garden.garden_helpers import add_by_kind
from lessons.garden.garden_helpers import add_by_date
from lessons.garden.garden_helpers import lookup_by_kind_and_date


def test_add_by_kind_use() -> None:
    """Test use case."""
    test: dict[str, list[str]] = {"flower": ["red flower", "yellow flower"], "vegetable": ["bok choy"]}
    add_by_kind(test, "flower", "green flower")
    assert test == {'flower': ['red flower', 'yellow flower', 'green flower'], 'vegetable': ['bok choy']}


def test_add_by_kind_edge() -> None:
    """Test edge case."""
    test: dict[str, list[str]] = {"flower": ["red flower", "yellow flower"], "vegetable": ["bok choy"]}
    add_by_kind(test, "fruit", "apple")
    assert test == {'flower': ['red flower', 'yellow flower'], 'vegetable': ['bok choy'], 'fruit': ['apple']}


def test_add_by_date_use() -> None:
    """Test use case."""
    test: dict[str, list[str]] = {"April": ["red flower"], "June": ["bok choy"]}
    add_by_date(test, "April", "yellow flower")
    assert test == {'April': ['red flower', 'yellow flower'], 'June': ['bok choy']}


def test_add_by_date_edge() -> None:
    """Test edge case."""
    test: dict[str, list[str]] = {"April": ["red flower"], "June": ["bok choy"]}
    add_by_date(test, "May", "apple")
    assert test == {'April': ['red flower'], 'June': ['bok choy'], 'May': ['apple']}


def test_lookup_by_kind_and_date_use() -> None:
    """Test use case."""
    kind: dict[str, list[str]] = {"flower": ["red flower", "yellow flower"], "vegetable": ["bok choy"]}
    date: dict[str, list[str]] = {"April": ["red flower"], "June": ["bok choy"]}
    assert lookup_by_kind_and_date(kind, date, "flower", "April") == "flower to plant in April: ['red flower']"


def test_lookup_by_kind_and_date_edge() -> None:
    """Test edge case."""
    kind: dict[str, list[str]] = {"flower": ["red flower", "yellow flower"], "vegetable": ["bok choy"]}
    date: dict[str, list[str]] = {"April": ["red flower"], "June": ["bok choy"]}
    assert lookup_by_kind_and_date(kind, date, "flower", "June") == 'No flowers to plant in June.'