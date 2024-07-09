# 103. Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/


from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []

        queue = []
        queue.append(root)

        is_even = False

        while queue:
            size = len(queue)

            current_result = [0] * size

            for i in range(size):
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if not is_even:
                    current_result[i] = node.val
                else:
                    current_result[size - 1 - i] = node.val

            result.append(current_result)

            is_even = not is_even

        return result
