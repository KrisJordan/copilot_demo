"""Simple priority queue skeleton.

Contract:
- Only accepts items as a tuple (priority: int, value: str)
- add(item) inserts into internal structure keeping min-priority first
- Other ops (pop/peek/len/iter) are unimplemented for now
"""

from .item import Item


class PriorityQueue:

    def __init__(self) -> None:
        # Internal storage: ascending by priority; stable for equal priorities
        self._items: list[Item] = []

    def add(self, item: Item) -> None:
        """Add an item, maintaining ascending priority order.

        Uses binary search to insert to keep O(log n) comparisons and O(n)
        shifts. Stable for equal priorities (insertion after existing equals).
        """
        priority, _value = item

        lo, hi = 0, len(self._items)
        while lo < hi:
            mid = (lo + hi) // 2
            if self._items[mid][0] <= priority:
                lo = mid + 1
            else:
                hi = mid
        self._items.insert(lo, item)

    # Placeholders for future API (intentionally not implemented)
    def pop(self) -> Item:  # pragma: no cover - not yet implemented
        raise NotImplementedError

    def peek(self) -> Item:  # pragma: no cover - not yet implemented
        raise NotImplementedError

    def __len__(self) -> int:  # pragma: no cover - not yet implemented
        raise NotImplementedError


__all__ = ["PriorityQueue"]
