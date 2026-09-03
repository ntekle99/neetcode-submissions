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

        clones = {}
        dq = deque()
        dq.append(node)
        clones[node] = Node(node.val)

        while dq:
            curr = dq.popleft()
            for nei in curr.neighbors:
                if nei not in clones:
                    clones[nei] = Node(nei.val)
                    dq.append(nei)
                clones[curr].neighbors.append(clones[nei])
        
        return clones[node]

