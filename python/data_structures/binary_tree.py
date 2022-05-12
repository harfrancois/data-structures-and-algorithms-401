class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self, root=None, values=None):
        self.root = root
        if values:
            for value in values:
                self.add(value)

    def pre_order(self):
        """
        Traverse the tree in a pre-order fashion
        return list of the values in correct order
        """

        def walk(root, values):  # root = a Node or none. Recursive function

            # every recursive function needs to know when to stop, aka base case
            if not root:
                return

            # Task 1: do something
            values.append(root.value)

            # Task 2: go left
            walk(root.left, values)

            # Task 3: go right
            walk(root.right, values)

        ordered_values = []

        walk(self.root, ordered_values)

        return ordered_values

    def in_order(self):
        """
        Traverse the tree in an in-order fashion
        return list of the values in correct order
        """

        def walk(root, values):  # root = a Node or none. Recursive function

            # every recursive function needs to know when to stop, aka base case
            if not root:
                return

            # Task 1: go left
            walk(root.left, values)

            # Task 2: do something
            values.append(root.value)

            # Task 3: go right
            walk(root.right, values)

        ordered_values = []

        walk(self.root, ordered_values)

        return ordered_values

    def post_order(self):
        """
        Traverse the tree in a post-order fashion
        return list of the values in correct order
        """

        def walk(root, values):  # root = a Node or none. Recursive function

            # every recursive function needs to know when to stop, aka base case
            if not root:
                return

            # Task 1: go left
            walk(root.left, values)

            # Task 2: go right
            walk(root.right, values)

            # Task 3: do something
            values.append(root.value)

        ordered_values = []

        walk(self.root, ordered_values)

        return ordered_values


    def find_maximum_value(self):

        def climb(root, values):

            if not root:
                return

            if root.value > self.max:
                self.max = root.value

            climb(root.left, values)

            climb(root.right, values)

        climb(self.root, self.ordered_values)

        return self.max

 def add(self, value):

        node = Node(value)

        if not self.root:
            self.root = node
            return

        breadth = Queue()

        breadth.enqueue(self.root)

        while not breadth.is_empty():
            front = breadth.dequeue()
            if not front.left:
                front.left = node
                return
            else:
                breadth.enqueue(front.left)

            if not front.right:
                front.right = node
                return
            else:
                breadth.enqueue(front.right)
