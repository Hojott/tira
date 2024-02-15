class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def count_helper(node):
    samenodes = 0
    if node.children:
        childrenlens = []

        for child in node.children:
            new_samenodes, childamount = count_helper(child)
            
            childrenlens.append(childamount)
            samenodes += new_samenodes

        if len(set(childrenlens)) == 1:
            issame = True
        else:
            issame = False

    else:
        issame = True
        childrenlens = []

    if issame:
        samenodes += 1

    childamount = sum(childrenlens) + 1
    return samenodes, childamount

def count(node):
    return count_helper(node)[0]

if __name__ == "__main__":
    tree = Node(1, [
               Node(2),
               Node(3, [
                    Node(4, [
                        Node(5),
                        Node(6)
                    ])
                ]),
                Node(7, [
                    Node(8),
                    Node(9)
                ])
           ])

    print(count(tree)) # 8

    tree = Node(6, [
                Node(3, [
                    Node(2, [
                        Node(1)
                    ])
                ]),
                Node(5, [
                    Node(4)
                ])
            ])
    print(count(tree)) # 5

