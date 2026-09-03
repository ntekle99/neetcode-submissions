# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.ancestor = root
        def dfs(root):
            if root is None:
                return
            if p.val > root.val and q.val > root.val:
                self.ancestor = root.right
                dfs(root.right)
            elif p.val < root.val and q.val < root.val:
                self.ancestor = root.left
                dfs(root.left)
            elif p.val > root.val and q.val < root.val:
                return
            elif root.val == p.val or root.val ==q.val:
                self.ancestor = root
                return
            return
        dfs(root)
        return self.ancestor