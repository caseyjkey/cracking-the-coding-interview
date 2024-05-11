# Write an algorithm to determine if there is a path between two nodes in a directed graph
from queue import SimpleQueue

class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = []

node = Node(1)
node2 = Node(2)
node2.neighbors = [Node(3)]
node.neighbors = [node2]
print(node.data)
print([n.data for n in node.neighbors])


def bfs(node, target):
    q = SimpleQueue()
    q.put(node)

    while not q.empty():
        n = q.get()
        if n.data == target:
            return True
        for neighbor in n.neighbors:
            q.put(neighbor)

    return False


print(bfs(node, 3))
print(bfs(node, 9))
