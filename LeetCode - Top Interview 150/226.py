# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DFS - Depth First Search
    def invertTree1(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        temp = root.left

        root.left = self.invertTree1(root.right)
        root.right = self.invertTree1(temp)

        return root

    # BFS - Breadth First Search
    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = []
        queue.append((root, root.left, root.right))

        while queue:
            node, left, right = queue.pop(0)

            node.left = right
            node.right = left

            if left:
                queue.append((left, left.left, left.right))
            if right:
                queue.append((right, right.left, right.right))

        return root
