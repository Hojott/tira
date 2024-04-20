class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeSet:
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            return

        node = self.root
        while True:
            if node.value == value:
                return
            if node.value > value:
                if not node.left:
                    node.left = Node(value)
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = Node(value)
                    return
                node = node.right

    def __contains__(self, value):
        if not self.root:
            return False

        node = self.root
        while node:
            if node.value == value:
                return True
            if node.value > value:
                node = node.left
            else:
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

    def height(self, h=-1, node="root"):
        if node == "root":
            # very purkkakoodi
            node = self.root

        if not node:
            return h

        return max(self.height(h=h+1, node=node.left), \
                   self.height(h=h+1, node=node.right))

if __name__ == "__main__":
    s = TreeSet()
    print(s.height()) # -1
    s.add(2)
    print(s.height()) # 0
    s.add(1)
    print(s.height()) # 1
    s.add(3)
    print(s.height()) # 1
    s.add(4)
    print(s.height()) # 2
