class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        self.head = None
        self.end = "NULL"

    def insert(self, value):
        self.head = Node(value, self.head)

    def __str__(self):

        return f"{self.end}"



    def includes(self, target_value):
        current = self.head
        while current:
            if current.value == target_value:
                return True
            current = current.next
        return False

class Node:
    def __init__(self, value, next=None, end="NULL"):
        self.value = value
        self.next = next
        self.end = end

    # def __str__(self):
    #
    #     return f"{self.next} -> {self.end}"



class TargetError:
    pass
