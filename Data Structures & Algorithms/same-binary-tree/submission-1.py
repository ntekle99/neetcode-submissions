# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        lst = []
        lst_2 = []
        def tree(curr):
            if not curr:
                return [None]
            left_val = tree(curr.left)
            right_val = tree(curr.right)

            return [curr.val] + left_val + right_val
        return tree(p) == tree(q)
        
