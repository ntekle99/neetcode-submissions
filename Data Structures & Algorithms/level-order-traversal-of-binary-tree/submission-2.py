# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stk = deque()
        stk.append(root)
        if root is None:
            return []

        self.res = [[root.val]]
        temp_lst = []
        while stk:
            level_size = len(stk)
            for i in range(level_size):
                element = stk.popleft()
                if element.left:
                    stk.append(element.left) 
                    temp_lst.append(element.left.val)
                if element.right:
                    stk.append(element.right)                   
                    temp_lst.append(element.right.val)

            if len(temp_lst)!=0:
                self.res.append(temp_lst)
            temp_lst = []
        return self.res

                