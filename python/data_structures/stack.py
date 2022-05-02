from data_structures.invalid_operation_error import InvalidOperationError
from data_structures.linked_list import Node


class Stack:
    """
    Put docstring here
    """

    def __init__(self):
        self.top = None

    # push the element at the last Index
    def push(self, value):
        self.top = Node(value, self.top)

    # remove last item.
    def pop(self):
        if not self.top:
            raise InvalidOperationError("Method not allowed on empty collection")
        old_top = self.top
        self.top = self.top.next
        old_top.next = None

        return old_top.value

    # allows you to see the last element
    def peek(self):
        if not self.top:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value

    def is_empty(self):
        return self.top is None
