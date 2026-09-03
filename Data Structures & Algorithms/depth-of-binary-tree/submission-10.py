# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level = 0

        def dfs(root,level):
            if root is None:
                return 0
            leftval = dfs(root.left,level+1)
            rightval = dfs(root.right,level+1)
            return max(leftval,rightval) + 1
        return dfs(root,0)
        
