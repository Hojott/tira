class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def count_helper(node, depth):
    depthsum = depth
    for child in node.children:
        depthsum += count_helper(child, depth+1)
    return depthsum

def count(node):
    return count_helper(node, 0)

if __name__ == "__main__":
    tree = Node(1, [
               Node(2),
               Node(3, [Node(4, [Node(5), Node(6)])]),
               Node(7, [Node(8), Node(9)])
           ])

    print(count(tree)) # 15
