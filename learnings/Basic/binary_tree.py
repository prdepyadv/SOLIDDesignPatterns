class Node():
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

class BinaryTree():
    def __init__(self, data):
        self.root = Node(data)

    # def show(self):
    #     self._show_recursive(self.root)
    
    # def _show_recursive(self, node):
    #     if node.left:
    #         self._show_recursive(node.left)
    #     print(node.data)
    #     if node.right:
    #         self._show_recursive(node.right)
    
    def show(self):
        if self.root.left:
            self.root.left.show()
        print(self.root.data)
        if self.root.right:
            self.root.right.show()

tree = BinaryTree(100)
tree.root.left = BinaryTree(99)
tree.root.right = BinaryTree(101)
tree.show()