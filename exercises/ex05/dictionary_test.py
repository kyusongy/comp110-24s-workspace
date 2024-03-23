"""Dictionary test."""

__author__ = "730720425"

from exercises.ex05.dictionary import invert
from exercises.ex05.dictionary import favorite_color
from exercises.ex05.dictionary import count
from exercises.ex05.dictionary import alphabetizer
from exercises.ex05.dictionary import update_attendance


def test_invert_use1() -> None:
    """Invert use case 1."""
    test: dict[str, str] = {"Jack": "apple", "James": "orange"}
    assert invert(test) == {"apple": "Jack", "orange": "James"}


def test_invert_use2() -> None:
    """Invert use case 2."""
    test: dict[str, str] = {"Jack": "apple", "Jason": "peach", "James": "orange"}
    assert invert(test) == {"apple": "Jack", "peach": "Jason", "orange": "James"}


def test_invert_edge() -> None:
    """Invert edge case (only one key and one value)."""
    test: dict[str, str] = {"Jack": "apple"}
    assert invert(test) == {"apple": "Jack"}


def test_favorite_color_use1() -> None:
    """Fave use case 1."""
    test: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(test) == "blue"


def test_favorite_color_use2() -> None:
    """Fave use case 2."""
    test: dict[str, str] = {"Kyle": "blue", "Kylie": "red", "Kate": "red"}
    assert favorite_color(test) == "red"


def test_favorite_color_edge() -> None:
    """Fave edge case (draw)."""
    test: dict[str, str] = {"Kyle": "blue", "Kylie": "red", "Kate": "red", "Camen": "blue"}
    assert favorite_color(test) == "red"


def test_count_use1() -> None:
    """Count use case 1."""
    test: list[str] = ["red", "blue", "red", "red"]
    assert count(test) == {"red": 3, "blue": 1}


def test_count_use2() -> None:
    """Count use case 2."""
    test: list[str] = ["red", "yellow", "blue", "red", "red"]
    assert count(test) == {"red": 3, "yellow": 1, "blue": 1}


def test_count_edge() -> None:
    """Count edge case (empty input list)."""
    test: list[str] = []
    assert count(test) == []


def test_alphabetizer_use1() -> None:
    """Alphabetizer use case 1."""
    test: list[str] = ["cat", "apple", "boy", "angry", "bad", "car"]
    assert alphabetizer(test) == {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}


def test_alphabetizer_use2() -> None:
    """Alphabetizer use case2."""
    test: list[str] = ["pot", "call", "cat", "apple", "boy", "angry", "bad", "car"]
    assert alphabetizer(test) == {'p': ["pot"], 'c': ['call', 'cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}


def test_alphabetizer_edge() -> None:
    """Alphabetizer edge case (with CPITAL letter)."""
    test: list[str] = ["Python", "sugar", "Turtle", "party", "table"]
    assert alphabetizer(test) == {'p': ['Python', 'party'], 's': ['sugar'], 't': ['Turtle', 'table']}


def test_update_attendance_use1() -> None:
    """Update attendance use case 1."""
    test: dict[str, str] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(test, "Tuesday", "Vrinda")
    update_attendance(test, "Wednesday", "Kaleb")
    assert test == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda'], 'Wednesday': ['Kaleb']}


def test_update_attendance_use2() -> None:
    """Update attendance use case 2."""
    test: dict[str, str] = {"Monday": ["Vrinda", "Kyle", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(test, "Tuesday", "Vrinda")
    update_attendance(test, "Wednesday", "Kyle")
    assert test == {'Monday': ['Vrinda', 'Kyle', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda'], 'Wednesday': ['Kyle']}


def test_update_attendance_edge() -> None:
    """Update attendance edge case (duplicate student)."""
    test: dict[str, str] = {"Monday": ["Vrinda", "Kyle", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(test, "Monday", "Kyle")
    assert test == {"Monday": ["Vrinda", "Kyle", "Kaleb"], "Tuesday": ["Alyssa"]}