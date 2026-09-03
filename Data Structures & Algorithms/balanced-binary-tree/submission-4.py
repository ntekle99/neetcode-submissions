# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def dfs(root):
            if root is None:
                return 0
            leftval = dfs(root.left) 
            rightval = dfs(root.right)

            if abs(leftval-rightval) > 1:
                self.balanced = False
            return max(leftval,rightval) + 1

        dfs(root)
        return self.balanced


        