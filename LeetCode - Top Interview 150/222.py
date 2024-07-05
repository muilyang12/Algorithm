# 222. Count Complete Tree Nodes
# https://leetcode.com/problems/count-complete-tree-nodes/


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def get_leftmost_height(node):
            result = 0
            current = node

            while current:
                result += 1
                current = current.left

            return result

        def get_rightmost_height(node):
            result = 0
            current = node

            while current:
                result += 1
                current = current.right

            return result

        def get_count(node):
            result = 0

            queue = []
            queue.append(node)

            while queue:
                current = queue.pop(0)
                result += 1

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            return result

        leftmost_height = get_leftmost_height(root)
        rightmost_height = get_rightmost_height(root)

        if leftmost_height == rightmost_height:
            return (2**leftmost_height) - 1
        else:
            return get_count(root)
