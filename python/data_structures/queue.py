from data_structures.invalid_operation_error import InvalidOperationError
from data_structures.linked_list import Node


class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        self.rear = None
        self.front = None

    def enqueue(self, value):
        self.rear = Node(value, self.rear)
        if not self.front:
            self.front = self.rear

    def dequeue(self):
        if not self.front:
            raise InvalidOperationError("Method not allowed on empty collection")
        old_front = self.front
        self.front = old_front.next
        old_front.next = None

        return old_front.value

    def peek(self):
        if not self.rear:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.front.value

    def is_empty(self):
        return self.front is None
