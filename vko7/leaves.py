class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def count(node):
    leaves = 0
    if node.children:
        for child in node.children:
            leaves += count(child)
    else:
        leaves += 1

    return leaves

if __name__ == "__main__":
    tree = Node(1, [
               Node(2),
               Node(3, [Node(4, [Node(5), Node(6)])]),
               Node(7, [Node(8), Node(9)])
           ])

    print(count(tree)) # 5
    print(count(Node(1))) # 1
