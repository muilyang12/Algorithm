# 129. Sum Root to Leaf Numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers1(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = 0

        queue = []
        queue.append((root, str(root.val)))

        while queue:
            node, current_num = queue.pop(0)

            if node.left:
                queue.append((node.left, current_num + str(node.left.val)))
            if node.right:
                queue.append((node.right, current_num + str(node.right.val)))
            if not node.left and not node.right:
                result += int(current_num)

        return result

    def sumNumbers2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = 0

        def traverse(node: Optional[TreeNode], prev_num: str):
            nonlocal result

            if not node:
                return

            current_num = prev_num + str(node.val)

            traverse(node.left, current_num)
            traverse(node.right, current_num)

            if not node.left and not node.right:
                result += int(current_num)

        traverse(root, "")

        return result
