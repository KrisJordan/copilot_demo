from __future__ import annotations

import pytest

from priority_queue import PriorityQueue


def test_add_single_item_orders_correctly() -> None:
    pq = PriorityQueue()
    pq.add((5, "a"))
    # Accessing internal _items for test purposes.
    assert pq._items == [(5, "a")]  # pyright: ignore[reportPrivateUsage]


def test_add_multiple_items_keeps_sorted_and_stable() -> None:
    pq = PriorityQueue()
    items = [(5, "a"), (3, "b"), (5, "c"), (1, "d"), (4, "e")]
    for it in items:
        pq.add(it)
    # Accessing internal _items for test purposes.
    assert pq._items == [  # pyright: ignore[reportPrivateUsage]
        (1, "d"),
        (3, "b"),
        (4, "e"),
        (5, "a"),
        (5, "c"),
    ]


def test_peek_empty_queue_raises_index_error() -> None:
    pq = PriorityQueue()
    with pytest.raises(IndexError, match="peek from empty priority queue"):
        pq.peek()


def test_peek_single_item_returns_that_item() -> None:
    pq = PriorityQueue()
    pq.add((5, "a"))
    assert pq.peek() == (5, "a")


def test_peek_multiple_items_returns_minimum_priority() -> None:
    pq = PriorityQueue()
    items = [(5, "a"), (3, "b"), (1, "d"), (4, "e")]
    for item in items:
        pq.add(item)
    assert pq.peek() == (1, "d")


def test_peek_same_priority_returns_first_added_stable() -> None:
    pq = PriorityQueue()
    pq.add((5, "first"))
    pq.add((3, "second"))
    pq.add((5, "third"))
    pq.add((1, "fourth"))
    assert pq.peek() == (1, "fourth")


def test_peek_does_not_modify_queue() -> None:
    pq = PriorityQueue()
    items = [(5, "a"), (3, "b"), (1, "d")]
    for item in items:
        pq.add(item)

    # Peek multiple times
    first_peek = pq.peek()
    second_peek = pq.peek()

    # Should return same item both times
    assert first_peek == second_peek == (1, "d")

    # Queue should remain unchanged
    assert pq._items == [
        (1, "d"),
        (3, "b"),
        (5, "a"),
    ]  # pyright: ignore[reportPrivateUsage]


def test_peek_after_adding_lower_priority_item() -> None:
    pq = PriorityQueue()
    pq.add((5, "a"))
    pq.add((3, "b"))
    assert pq.peek() == (3, "b")

    # Add even lower priority item
    pq.add((1, "c"))
    assert pq.peek() == (1, "c")
