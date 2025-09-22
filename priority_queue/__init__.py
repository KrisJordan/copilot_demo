"""Priority queue package public API.

This module re-exports the core types from the internal implementation module
to provide a clean, stable import path:

    from priority_queue import PriorityQueue, Item
"""

from __future__ import annotations

from .priority_queue import Item, PriorityQueue

__all__ = ["Item", "PriorityQueue"]
