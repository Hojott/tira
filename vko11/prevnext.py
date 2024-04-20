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

    def next(self, x):
        node = self.root
        smallest = None
        while node != None:
            if node.value > x:
                if smallest is None or node.value < smallest:
                    smallest = node.value
                node = node.left
            else:
                node = node.right

        return smallest
        

    def prev(self, x):
        node = self.root
        biggest = None
        while node != None:
            if node.value < x:
                if biggest is None or node.value > biggest:
                    biggest = node.value
                node = node.right
            else:
                node = node.left
        
        return biggest

if __name__ == "__main__":
    s = TreeSet()
    s.add(2)
    s.add(5)
    print(s.prev(5)) # 2
    print(s.prev(2)) # None
    print(s.next(1)) # 2
    print(s.next(2)) # 5
    print(s.next(5)) # None

    s = TreeSet()
    s.add(10)
    print(s.prev(9))
    print(s.next(6))
    s.add(10)
    print(s.prev(10))
    print(s.next(3))
    s.add(6)
    print(s.prev(7))
    print(s.next(6))
    s.add(5)
    print(s.prev(7))
    print(s.next(4))
    s.add(6)
    print(s.prev(2))
    print(s.next(7))
    s.add(7)
    print(s.prev(2))
    print(s.next(9))
    s.add(6)
    print(s.prev(7))
    print(s.next(7))
    s.add(5)
    print(s.prev(1))
    print(s.next(6))
    s.add(10)
    print(s.prev(2))
    print(s.next(8))
    s.add(4)
    print(s.prev(3))
    print(s.next(6))
