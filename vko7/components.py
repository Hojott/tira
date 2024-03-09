def count(n):
    components = set()
    curves = dict()
    for i in range(2, n+1):
        curves[i] = []

    for i in range(2, n+1):
        for j in range(i+1, n+1):
            if not j % i:
                curves[i].append(j) 
                curves[j].append(i)

    places_been: set
    def recursive(a):
        places_been.add(a)
        if a in components:
            return False
        for dest in curves[a]:
            if dest in places_been:
                continue

            if not recursive(dest):
                return False

        return True


    for i in curves:
        places_been = set()
        if recursive(i):
            components.add(i)

    return len(components)

if __name__ == "__main__":
    print(count(3)) # 0
    print(count(4)) # 1
    print(count(6)) # 3
    print(count(1000)) # ??

