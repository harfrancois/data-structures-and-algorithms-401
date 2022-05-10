


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def pre_order(self, root):
        stack = []
        result = []
        while root or stack:
            while root:
                result.append(self.root.value)
                stack.append(root)
                root = root.left
            root = stack.pop()
            root = self.root.right
        return result

