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

    def parent(self, node, child):
        if not node:
            return
        if node.left:
            if node.left.value == child.value:
                return node
        if node.right:
            if node.right.value == child.value:
                return node

        left = self.parent(node.left, child)
        right = self.parent(node.right, child)

        return left if left else right
        

    def remove(self, x):
        if x not in self:
            return
        node = self.root
        while node:
            if node.value > x:
                node = node.left
            elif node.value < x:
                node = node.right
            elif node.value == x:
                self.__rm(node)
                return

    def __rm(self, node):
        parent = self.parent(self.root, node)

        if not node.left and not node.right:
            if not parent:
                self.root = None
                return
            if parent.left:
                if parent.left.value == node.value:
                    parent.left = None
                    return
            if parent.right.value == node.value:
                parent.right = None

        elif not node.left:
            if not parent:
                self.root = node.right
                return
            if parent.left:
                if parent.left.value == node.value:
                    parent.left = node.right
                    return
            if parent.right.value == node.value:
                parent.right = node.right

        elif not node.right:
            if not parent:
                self.root = node.left
                return
            if parent.left:
                if parent.left.value == node.value:
                    parent.left = node.left
                    return
            if parent.right.value == node.value:
                parent.right = node.left

        else:
            swap = self.next(node.value)
            self.remove(swap)
            node.value = swap

if __name__ == "__main__":
    s = TreeSet()
    s.add(2)
    s.add(1)
    s.add(3)
    s.add(4)
    print(s) # [1, 2, 3, 4]
    s.remove(3)
    print(s) # [1, 2, 4]
    s.remove(2)
    print(s) # [1, 4]
    s.remove(1)
    print(s) # [4]
    s.remove(1)
    print(s) # [4]

    print()

    s = TreeSet()
    s.add(7)
    print(s)
    s.remove(9)
    print(s)
    s.add(6)
    print(s)
    s.remove(7)
    print(s)
    s.remove(5)
    print(s)
    s.add(1)
    print(s)
    s.add(10)
    print(s)
    s.add(8)
    print(s)
    s.add(3)
    print(s)
    s.add(10)
    print(s)
