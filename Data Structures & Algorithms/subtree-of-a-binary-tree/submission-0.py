# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        def sameTree(root,subRoot):
            if root is None and subRoot is None:
                return True
            if root is None or subRoot is None or root.val != subRoot.val:
                return False
            LeftTrees = sameTree(root.left,subRoot.left)
            RightTrees = sameTree(root.right,subRoot.right)

            return LeftTrees and RightTrees
        fun_bool = sameTree(root,subRoot)
        if fun_bool == True:
            return True
        second_LeftTrees = self.isSubtree(root.left, subRoot)
        second_RightTrees = self.isSubtree(root.right,subRoot)
        return second_LeftTrees or second_RightTrees




