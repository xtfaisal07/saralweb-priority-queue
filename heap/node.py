from dataclasses import dataclass

@dataclass
class Node:
    id: int
    value: str
    priority: int

    def __repr__(self):
        return f"Node(id={self.id}, value='{self.value}', priority={self.priority})"