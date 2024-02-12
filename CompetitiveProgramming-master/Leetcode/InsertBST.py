# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def insertIntoBST(self, root: [TreeNode], val: int) -> [TreeNode]:
        newNode = TreeNode(val)
        dummy = TreeNode(val = float('inf'), left = root)
        prev = dummy
        curr = root

        while curr:
            if val < curr.val:
                if curr.left:
                    prev = curr
                    curr = curr.left
                else:
                    curr.left = newNode
                    break

            else:
                if curr.right:
                    prev = curr
                    curr = curr.right
                else:
                    curr.right = newNode
                    break

        if not root:
            root = newNode

        return root
        