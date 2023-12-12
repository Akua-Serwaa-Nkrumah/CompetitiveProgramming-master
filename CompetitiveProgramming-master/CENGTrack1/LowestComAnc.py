# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lowestAnc(root,p,q):
            if not root:
                print(prev.val)
                return prev

            prev = root
            if (p.val <= root.val <= q.val) or (q.val <= root.val <= p.val):
                return root

            if (p.val > root.val):
                return lowestAnc(root.right,p,q)
            
            else:
                return lowestAnc(root.left,p,q)

        return lowestAnc(root,p,q)
        