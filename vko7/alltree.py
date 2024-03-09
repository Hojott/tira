import math

def count(n, k):
    """ Could probably have been done arithmetically """
    trees = 0 # amount of possible trees
    base = 1 # startpoint
    leafs = k # endpoint
    barks = n - leafs - base # everything in between

    # edgecases out of the way
    if leaf == 0:
        return 0
    if barks < 0:
        return 0
    if barks == 0:
        return leafs
    
    tree_children = [] # total amount of trees without position taken into account
    for leaf in range(leafs+1): # how many leaves are allocated
        leaf_children = []
        for bark in range(barks+1): # how many barks are allocated
            bark_children = count(bark+leaf, leaf)
            leaf_children.append(bark_children)

        tree_children.append(leaf_children)

    def bark_combs(leaf, bark):
        """ Each (inner) recursion takes n barks away """
        ways_list = []
        for b in range(1, bark+1):
            for l in range(1, leaf+1):
                for i in bark_combs(l, b):
                    wayslist.append(...)
            

        return wayslist

    for leaf in range(leafs+1):
        total = 0

        for bark_list in bark_combs(leaf):
            bark = len(bark_list)

            bark_leaf_combs = math.ncr(leaf+bark, leaf)
            bark_bark_combs = math.npr(bark, bark)

            all_bark_children = 1
            sizes_used = set()
            for (b, l) in bark_list:
                all_bark_children *= leaf_children[l][b]
                if (b, l) in sizes_used:
                    all_bark_children -= leaf_children[l][b]
                
                sizes_used.add((b, l))

            bark_bark_weighted = bark_bark_combs * all_bark_children

            total += bark_bark_weighted * bark_leaf_combs

        trees += total

    return trees


if __name__ == "__main__":
    print(count(4, 1)) # 1
    print(count(4, 2)) # 3
    print(count(4, 3)) # 1
    print(count(4, 4)) # 0
    print(count(10, 4)) # 1176
