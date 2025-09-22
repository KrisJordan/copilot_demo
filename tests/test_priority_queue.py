from priority_queue import PriorityQueue


def test_add_single_item_orders_correctly() -> None:
    pq = PriorityQueue()
    pq.add((5, "a"))
    # Accessing internal _items for test purposes.
    assert pq._items == [(5, "a")]  # pyright: ignore[reportPrivateUsage]


def test_add_multiple_items_keeps_sorted_and_stable() -> None:
    pq = PriorityQueue()
    items = [(5, "a"), (3, "b"), (5, "c"), (1, "d"),
             (4, "e"), (3, "f"), (3, "g")]
    for it in items:
        pq.add(it)
    # Accessing internal _items for test purposes.
    assert pq._items == [  # pyright: ignore[reportPrivateUsage]
        (1, "d"),
        (3, "b"),
        (3, "f"),
        (3, "g"),
        (4, "e"),
        (5, "a"),
        (5, "c"),
    ]
