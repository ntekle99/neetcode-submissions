# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.path_1 = []
        self.path_2 = []

        def create_path(root,path):
            if root == None:
                return None
            if root.val == p.val:
                self.path_1 = path
            if root.val == q.val:
                self.path_2 = path
            create_path(root.left,path + ["left"])
            create_path(root.right,path + ["right"])
        
        def find_lca(root,idx):
            if idx == len(self.path_1) or idx == len(self.path_2):
                self.lca = root
                return 
            
            elif self.path_1[idx] == self.path_2[idx]:
                if self.path_1[idx] == "left":
                    find_lca(root.left,idx+1)
                else:
                    find_lca(root.right,idx+1)

            elif self.path_1[idx] != self.path_2[idx]:
                self.lca = root
                return

        create_path(root,[])
        print(self.path_1,self.path_2)
        find_lca(root,0)

        return self.lca

