# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balance = True

        def dfs(curr):
            if not curr:
                return 0
        
            left_val = dfs(curr.left)
            right_val = dfs(curr.right)

            if abs(left_val-right_val) > 1:
                self.balance = False
            return 1 + max(left_val,right_val)
        
        dfs(root)
        return self.balance
        