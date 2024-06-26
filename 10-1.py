# Given two sorted arrays A and B, where A has enough space at the end to hold B, merge the two in sorted order

class Node:
    def __init__(self, key):
        self.data = key
        self.next = None

def merge(h1, h2):
    if not h1:
        return h2
    if not h2:
        return h1

    if h1.data <= h2.data:
        h1.next = merge(h1.next, h2)
        return h1
    else:
        h2.next = merge(h1, h2.next)
        return h2

def printNode(node):
    while(node):
        print(node.data, end=" ")
        node = node.next
    return

n1 = Node(0)
n1.next = Node(2)
n1.next.next = Node(3)
n2 = Node(1)
n2.next = Node(4)
n2.next.next = Node(5)

n3 = merge(n1, n2)
print(printNode(n3))
