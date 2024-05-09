# Remove duplicates from an unsorted linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def add(self, n):
        node = self

        while node.next != None:
            node = node.next

        node.next = n

        return n


node = Node(1)
node.add(Node(2))
node.add(Node(2))
node.add(Node(3))
node.add(Node(2))
n = node
prev = node
seen = {n.data}
while n.next != None:
    prev = n
    n = n.next
    if n.data in seen:
        print("seen", n.data)
        prev.next = n.next
    else:
        seen.add(n.data)

n = node
print(n.data)
while n.next != None:
    n = n.next
    print(n.data)
