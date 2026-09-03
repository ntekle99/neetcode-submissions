# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.result = True
        
        def helper(root):    
            if root is None:
                return 0 
            
            leftTree=helper(root.left)
            rightTree=helper(root.right)
            if abs(leftTree - rightTree) > 1:
                self.result = False
            return max(leftTree, rightTree) + 1
        helper(root)
        return self.result
