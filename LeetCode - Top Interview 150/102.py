# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/


from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder1(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []

        queue = []
        queue.append((root, 1))

        prev_depth = None

        while queue:
            node, depth = queue.pop(0)

            if depth != prev_depth:
                result.append([])

                prev_depth = depth

            result[-1].append(node.val)

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return result

    def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []

        queue = []
        queue.append(root)

        while queue:
            size = len(queue)

            result.append([])

            for i in range(size):
                node = queue.pop(0)

                result[-1].append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
