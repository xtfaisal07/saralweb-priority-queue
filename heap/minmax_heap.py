from math import log2, floor
from heap.node import Node
from heap.exceptions import EmptyQueueError


class MinMaxHeap:

    def __init__(self):
        self.heap = []
        self.position = {}

    def __len__(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def level(self, index):
        return floor(log2(index + 1))

    def is_min_level(self, index):
        return self.level(index) % 2 == 0

    def parent(self, i):
        return (i - 1) // 2

    def grandparent(self, i):
        return self.parent(self.parent(i))

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

        self.position[self.heap[i].id] = i
        self.position[self.heap[j].id] = j


    def has_grandparent(self, i):
        return i >= 3


    def bubble_up_min(self, i):
        while self.has_grandparent(i):
            gp = self.grandparent(i)
            if self.heap[i].priority < self.heap[gp].priority:
                self.swap(i, gp)
                i = gp
            else:
                break

    def bubble_up_max(self, i):
        while self.has_grandparent(i):
            gp = self.grandparent(i)
            if self.heap[i].priority > self.heap[gp].priority:
                self.swap(i, gp)
                i = gp
            else:
                break

    def insert(self, node: Node):
        """
        Insert a node into the Min-Max Heap.
        Time Complexity: O(log n)
        """
        self.heap.append(node)
        i = len(self.heap) - 1
        self.position[node.id] = i

        if i == 0:
            return

        p = self.parent(i)

        if self.is_min_level(i):
            if self.heap[i].priority > self.heap[p].priority:
                self.swap(i, p)
                self.bubble_up_max(p)
            else:
                self.bubble_up_min(i)
        else:
            if self.heap[i].priority < self.heap[p].priority:
                self.swap(i, p)
                self.bubble_up_min(p)
            else:
                self.bubble_up_max(i)

    def peek_min(self):
        if self.is_empty():
            raise EmptyQueueError("Priority Queue is empty.")
        return self.heap[0]

    def peek_max(self):
        if self.is_empty():
            raise EmptyQueueError("Priority Queue is empty.")

        if len(self.heap) == 1:
            return self.heap[0]

        if len(self.heap) == 2:
            return self.heap[1]

        return max(self.heap[1], self.heap[2], key=lambda x: x.priority)

    def display(self):
        return [
            {
                "id": node.id,
                "value": node.value,
                "priority": node.priority
            }
            for node in self.heap
        ]

    def build_heap(self, nodes):
        self.heap = []
        self.position = {}

        for node in nodes:
            self.insert(node)
            


    def children(self, i):
        result = []
        l = self.left(i)
        r = self.right(i)

        if l < len(self.heap):
            result.append(l)
        if r < len(self.heap):
            result.append(r)

        return result

    def grandchildren(self, i):
        result = []

        for child in self.children(i):
            result.extend(self.children(child))

        return result

    def smallest_descendant(self, i):
        candidates = self.children(i) + self.grandchildren(i)

        if not candidates:
            return None

        return min(candidates, key=lambda idx: self.heap[idx].priority)

    def largest_descendant(self, i):
        candidates = self.children(i) + self.grandchildren(i)

        if not candidates:
            return None

        return max(candidates, key=lambda idx: self.heap[idx].priority)

    def trickle_down_min(self, i):
        while True:
            m = self.smallest_descendant(i)

            if m is None:
                break

            if m in self.grandchildren(i):
                if self.heap[m].priority < self.heap[i].priority:
                    self.swap(m, i)

                    parent = self.parent(m)
                    if self.heap[m].priority > self.heap[parent].priority:
                        self.swap(m, parent)

                    i = m
                else:
                    break

            else:
                if self.heap[m].priority < self.heap[i].priority:
                    self.swap(m, i)
                break

    def trickle_down_max(self, i):
        while True:
            m = self.largest_descendant(i)

            if m is None:
                break

            if m in self.grandchildren(i):
                if self.heap[m].priority > self.heap[i].priority:
                    self.swap(m, i)

                    parent = self.parent(m)
                    if self.heap[m].priority < self.heap[parent].priority:
                        self.swap(m, parent)

                    i = m
                else:
                    break

            else:
                if self.heap[m].priority > self.heap[i].priority:
                    self.swap(m, i)
                break

    def extract_min(self):
        if self.is_empty():
            raise EmptyQueueError("Priority Queue is empty.")

        minimum = self.heap[0]

        if len(self.heap) == 1:
            self.heap.pop()
            return minimum

        self.heap[0] = self.heap.pop()
        self.trickle_down_min(0)

        return minimum

    def extract_max(self):
        if self.is_empty():
            raise EmptyQueueError("Priority Queue is empty.")

        if len(self.heap) == 1:
            return self.heap.pop()

        if len(self.heap) == 2:
            return self.heap.pop(1)

        max_index = 1 if self.heap[1].priority > self.heap[2].priority else 2

        maximum = self.heap[max_index]

        self.heap[max_index] = self.heap.pop()

        if max_index < len(self.heap):
            self.trickle_down_max(max_index)

        return maximum

def delete_by_id(self, node_id):
    if node_id not in self.position:
        raise KeyError("Node not found")

    index = self.position[node_id]
    deleted = self.heap[index]

    last = self.heap.pop()
    del self.position[node_id]

    if index == len(self.heap):
        return deleted

    self.heap[index] = last
    self.position[last.id] = index

    if index > 0:
        parent = self.parent(index)

        if self.is_min_level(index):
            if self.heap[index].priority > self.heap[parent].priority:
                self.swap(index, parent)
                self.bubble_up_max(parent)
            else:
                self.bubble_up_min(index)
        else:
            if self.heap[index].priority < self.heap[parent].priority:
                self.swap(index, parent)
                self.bubble_up_min(parent)
            else:
                self.bubble_up_max(index)
    else:
        self.trickle_down_min(0)

    return deleted


def update_priority(self, node_id, new_priority):
    if node_id not in self.position:
        raise KeyError("Node not found")

    i = self.position[node_id]
    old = self.heap[i].priority
    self.heap[i].priority = new_priority

    if new_priority < old:
        if self.is_min_level(i):
            self.bubble_up_min(i)
        else:
            p = self.parent(i)
            if p >= 0 and self.heap[i].priority < self.heap[p].priority:
                self.swap(i, p)
                self.bubble_up_min(p)
    else:
        if self.is_min_level(i):
            self.trickle_down_min(i)
        else:
            self.trickle_down_max(i)

    return True