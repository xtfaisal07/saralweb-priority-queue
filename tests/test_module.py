import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from module import PriorityQueue


def test_insert():
    pq = PriorityQueue()
    pq.repo.clear()
    pq.heap.build_heap([])

    pq.insert("Task", 10)

    assert pq.peek()["min"].priority == 10


def test_extract_min():
    pq = PriorityQueue()
    pq.repo.clear()
    pq.heap.build_heap([])

    pq.insert("A", 20)
    pq.insert("B", 5)

    node = pq.extract_min()

    assert node.priority == 5


def test_is_empty():
    pq = PriorityQueue()
    pq.repo.clear()
    pq.heap.build_heap([])

    assert pq.is_empty()