import pytest
import heapq
from copy import deepcopy

from intro.basics import OurHeap


def test_heap_init():
    items = [30, 20, 10, 11, 5, 3, 8]
    heap_computer = OurHeap(items) 

    # check with heapq.heapify
    heap = heap_computer.heap[1:] # exclude None
    heap_copy = deepcopy(heap)
    heapq.heapify(heap_copy)

    assert heap == heap_copy


def test_heap_update():
    items = [3, 5, 8, 11, 20, 10, 30]
    heap_computer = OurHeap(items)
    heap_computer.update(8, 40)

    assert heap_computer.rank[40] == 6
    assert heap_computer.heap == [None, 3, 5, 10, 11, 20, 40, 30]