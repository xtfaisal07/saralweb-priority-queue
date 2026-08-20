class PriorityQueueError(Exception):
    """Base exception for Priority Queue."""
    pass


class EmptyQueueError(PriorityQueueError):
    """Raised when queue is empty."""
    pass


class NodeNotFoundError(PriorityQueueError):
    """Raised when requested node doesn't exist."""
    pass