# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: [TreeNode], k: int) -> int:
        tree = []
        
        def traverse(root):
            if not root:
                return

            traverse(root.left)
            tree.append(root.val)
            traverse(root.right)

            return tree

        return traverse(root)[k-1]