# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(root,node):
            if root is None and node is None:
                return True
            elif root is None or node is None:
                return False
            elif root.val != node.val:
                return False
            left_res = dfs(root.left,node.left)
            right_res = dfs(root.right,node.right)
            
            return left_res and right_res   
        
        return dfs(p,q)
            