# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        def issameTree(p,q):
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            elif p.val!=q.val:
                return False
            return issameTree(p.left,q.left) and issameTree(p.right,q.right)


        stk = [root]
        while stk:
            for elements in stk:
                element = stk.pop()
                if element.left:
                    stk.append(element.left)
                if element.right:
                    stk.append(element.right)
                print(element.val,subRoot.val)
                if issameTree(element,subRoot):
                    return True
        return False

