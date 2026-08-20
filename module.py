from heap.minmax_heap import MinMaxHeap
from heap.node import Node
from heap.exceptions import NodeNotFoundError
from database.repository import PriorityQueueRepository


class PriorityQueue:

    def __init__(self):
        self.repo = PriorityQueueRepository()
        self.heap = MinMaxHeap()
        self._load()

    def _load(self):
        rows = self.repo.get_all()

        nodes = [
            Node(r["id"], r["value"], r["priority"])
            for r in rows
        ]

        self.heap.build_heap(nodes)

    def insert(self, value, priority):
        node_id = self.repo.create(value, priority)
        node = Node(node_id, value, priority)
        self.heap.insert(node)
        return node

    def extract_min(self):
        node = self.heap.extract_min()
        self.repo.delete(node.id)
        return node

    def extract_max(self):
        node = self.heap.extract_max()
        self.repo.delete(node.id)
        return node

    def peek(self):
        return {
            "min": self.heap.peek_min(),
            "max": self.heap.peek_max()
        }

    def is_empty(self):
        return self.heap.is_empty()

    def display(self):
        return self.heap.display()

    def update(self, node_id, priority):
        self.repo.update(node_id, priority)
        self.heap.update_priority(node_id, priority)

    def delete(self, node_id):
        self.repo.delete(node_id)
        return self.heap.delete_by_id(node_id)