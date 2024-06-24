# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # BFS - Breadth First Search
    def maxDepth1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = []
        max_depth = 0

        queue.append((1, root))
        while queue:
            depth, current = queue.pop(0)
            max_depth = max(max_depth, depth)

            if current.left:
                queue.append((depth + 1, current.left))

            if current.right:
                queue.append((depth + 1, current.right))

        return max_depth

    # DFS - Depth First Search
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_depth):
            if not node:
                return current_depth - 1

            return max(
                dfs(node.left, current_depth + 1), dfs(node.right, current_depth + 1)
            )

        return dfs(root, 1)
