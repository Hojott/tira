import collections

class FlipList:
    def __init__(self):
        self.fliplist = collections.deque()
        self.flipped = False

    def push_first(self, x):
        if not self.flipped:
            return self.fliplist.appendleft(x)

        return self.fliplist.append(x)

    def push_last(self, x):
        if not self.flipped:
            return self.fliplist.append(x)
        
        return self.fliplist.appendleft(x)

    def pop_first(self):
        if not self.flipped:
            return self.fliplist.popleft()
        
        return self.fliplist.pop()

    def pop_last(self):
        if not self.flipped:
            return self.fliplist.pop()

        return self.fliplist.popleft()

    def flip(self):
        self.flipped = not self.flipped

if __name__ == "__main__":
    f = FlipList()
    f.push_last(1)
    f.push_last(2)
    f.push_last(3)
    print(f.pop_first()) # 1
    f.flip()
    print(f.pop_first()) # 3
