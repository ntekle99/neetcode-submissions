"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clones = {node: Node(node.val)}

        dq = deque([node])

        while dq:
            element = dq.pop()
            for item in element.neighbors:
                if item not in clones:
                    clones[item] = Node(item.val)
                    dq.append(item)
                clones[element].neighbors.append(clones[item])

        return clones[node]