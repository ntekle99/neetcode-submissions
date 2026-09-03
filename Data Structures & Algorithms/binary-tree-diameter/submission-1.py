# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(curr):
            if curr == None:
                return 0
            
            left_val = dfs(curr.left)
            right_val = dfs(curr.right)

            self.res = max(self.res,left_val+right_val)
            return 1 + max(left_val,right_val)
        
        dfs(root)
        return self.res
