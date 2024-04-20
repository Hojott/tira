class Node:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None
        self.balance = 0

class TreeSet:
    def __init__(self):
        self.root = None

    def add(self, x):
        if not self.root:
            self.root = Node(x)
            return

        node = self.root
        while True:
            if node.value == x:
                return
            if node.value < x:
                node.balance += 1
                if not node.right:
                    node.right = Node(x)
                    return
                if node.balance > 1:
                    if node.left:
                        left = node.left
                    else:
                        left = None
                    node.left = Node(node.value)
                    node.left.left = left
                    node.value = node.right.value
                    node.left.right = node.right.left
                    node.right = node.right.right
                    continue

                node = node.right

            if node.value > x:
                node.balance -= 1
                if not node.left:
                    node.left = Node(x)
                    return
                if node.balance < -1:
                    if node.right:
                        right = node.right
                    else:
                        right = None
                    node.right = Node(node.value)
                    node.right.right = right
                    node.value = node.left.value
                    node.right.left = node.left.right
                    node.left = node.left.left
                    continue

                node = node.left

    def __contains__(self, x):
        node = self.root
        while node:
            if node.value == x:
                return True
            elif node.value > x:
                node = node.left
            elif node.value < x:
                node = node.right
        
        return False

    def __repr__(self):
        items = []
        self.traverse(self.root, items)
        return str(items)

    def traverse(self, node, items):
        if not node:
            return
        self.traverse(node.left, items)
        items.append(node.value)
        self.traverse(node.right, items)

if __name__ == "__main__":
    s = TreeSet()
    s.add(1)
    s.add(2)
    s.add(4)
    print(1 in s) # True
    print(2 in s) # True
    print(3 in s) # False
    print(4 in s) # True
    print(s) # [1, 2, 4]
