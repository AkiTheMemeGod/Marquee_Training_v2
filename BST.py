class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None


def printPostOrder(node):
    if node is None:
        return
    printPostOrder(node.left)
    printPostOrder(node.right)
    print(node.data, end=" ")

def printPreOrder(node):
    if node is None:
        return
    print(node.data, end=" ")
    printPostOrder(node.left)
    printPostOrder(node.right)

def printInOrder(node):
    if node is None:
        return
    printPostOrder(node.left)
    print(node.data, end=" ")
    printPostOrder(node.right)


root = Node(100)
root.left = Node(20)
root.right = Node(200)
root.left.left = Node(10)
root.left.right = Node(30)
root.right.left = Node(150)
root.right.right = Node(300)


print("Postorder Traversal: ", end="")
printPostOrder(root)
print("\nPreorder Traversal: ", end="")
printPreOrder(root)
print("\nInorder Traversal: ", end="")
printInOrder(root)