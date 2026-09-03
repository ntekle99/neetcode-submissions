# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.mx = 0
        def dfs(root):
            if root is None:
                return 0
            left_val = dfs(root.left)
            right_val = dfs(root.right)
            self.mx = max(self.mx,left_val+right_val)
            return 1+max(left_val,right_val)
        dfs(root)
        return self.mx