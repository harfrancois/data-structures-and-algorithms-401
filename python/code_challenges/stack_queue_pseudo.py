from data_structures.linked_list import Node


class PseudoQueue:
    pass

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        self.rear = Node(value, self.rear)
        if not self.front:
            self.front = self.rear

    def dequeue(self):
        old_front = self.front
        self.front = old_front.next
        old_front.next = None

        return old_front.value
