# Definition for a binary tree node.
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution: 
    def rob(self, root: TreeNode) -> int:
        memo = defaultdict(list)
        def dp(node):
            if not node:
                return [0,0]

            if node not in memo:
                leftTree = dp(node.left)
                rightTree = dp(node.right)

                withRoot = node.val + leftTree[1]+ rightTree[1]
                withoutRoot = max(leftTree) + max(rightTree)

                memo[node] = [withRoot,withoutRoot]

            return memo[node]

        return max(dp(root))
