# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def hasPathSum(self, root: [TreeNode], targetSum: int) -> bool:
        check = False
        count = float('inf')
        if root:
            count = 0

        def dfs(root,count):
            nonlocal check
            if root:
                count += root.val
                if (not root.left and not root.right):
                    if not check:
                            check = (count == targetSum)
                    return

                if root.left:
                    dfs(root.left,count)
                if root.right:
                    dfs(root.right,count)

            return 

        dfs(root,count)
        return check