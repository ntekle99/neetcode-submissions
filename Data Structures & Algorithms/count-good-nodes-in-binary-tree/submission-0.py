# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.good = 0
        def dfs(root,num):
            if root is None:
                return
            if root.val >= num:
                self.good+=1
                dfs(root.right,root.val)
                dfs(root.left,root.val)
            else:
                dfs(root.right,num)
                dfs(root.left,num)
        dfs(root,root.val)
        return self.good