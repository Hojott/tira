class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def check_helper(node, depth):
    if not node.children:
        leafdepth.add(depth)

    for child in node.children:
        check_helper(child, depth+1)

def check(node):
    global leafdepth
    leafdepth = set()
    check_helper(node, 0)
    return not bool(len(leafdepth)-1)

if __name__ == "__main__":
    tree1 = Node(1, [
                Node(2),
                Node(3, [Node(4, [Node(5), Node(6)])]),
                Node(7, [Node(8), Node(9)])
            ])

    tree2 = Node(1, [Node(2, [Node(3)]), Node(4, [Node(5), Node(6)])])

    print(check(tree1)) # False
    print(check(tree2)) # True
