class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def count(node):
    biggest = len(node.children)
    for child in node.children:
        biggest = max(biggest, count(child))
    return biggest

if __name__ == "__main__":
    tree1 = Node(1, [
                Node(2),
                Node(3, [Node(4, [Node(5), Node(6)])]),
                Node(7, [Node(8), Node(9)])
            ])

    tree2 = Node(1, [Node(2, [Node(3), Node(4)])])

    print(count(tree1)) # 3
    print(count(tree2)) # 2
