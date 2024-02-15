class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def check(node):
    if not node.children:
        return True
    if len(node.children) > 1:
        return False
    return check(node.children[0])

if __name__ == "__main__":
    tree1 = Node(1, [
                Node(2),
                Node(3, [Node(4, [Node(5), Node(6)])]),
                Node(7, [Node(8), Node(9)])
            ])

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])

    print(check(tree1)) # False
    print(check(tree2)) # True
