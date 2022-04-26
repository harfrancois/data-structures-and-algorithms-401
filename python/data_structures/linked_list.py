class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        self.next = None
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)

    def append(self, value):
        new_node = Node(value)  # create new node.

        if self.head is None:  # check if head has data.
            self.head = new_node  # None becomes new head.
            return

        last_node = self.head  # if list is not empty?
        while last_node.next:  # if not none continue loop.
            last_node = last_node.next
        last_node.next = new_node  # insert new node when none.

    def insert_before(self, value, new_value):
        new_node = Node(new_value) # creating new node
        current = self.head # current is the head
        if current.value is value: # check to see if current is target value
            new_node.next = self.head # new node next is connected to head
            self.head = new_node # new node becomes the new head

        while current.next is not None: # while current has value
            new_node.next = current.next # new node's next become the current node's next
            current.next = new_node # current next is the new node
            return



    def includes(self, target_value):
        current = self.head
        while current:
            if current.value == target_value:
                return True
            current = current.next
        return False

    def __str__(self):
        string = ""
        if self.head == None:
            return 'NULL'
        current = self.head
        while current:
            string += f"{{ {current.value} }} -> "
            current = current.next
        string += 'NULL'
        return string


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TargetError:
    pass
