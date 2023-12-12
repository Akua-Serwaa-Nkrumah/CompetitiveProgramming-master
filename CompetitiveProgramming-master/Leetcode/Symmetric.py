# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: [TreeNode]) -> bool:
        def symmetry(p,q):
            if p == q == None:
                return True

            if (p and not q) or (q and not p):
                return False

            if p.val != q.val:
                return False

            return symmetry(p.left,q.right) and symmetry(p.right,q.left)
            
        return symmetry(root.left,root.right)
