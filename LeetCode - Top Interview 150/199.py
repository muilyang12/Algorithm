# 199. Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/


from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None

        result = []

        queue = []
        queue.append((root, 1))

        while queue:
            node, depth = queue.pop(0)

            if len(result) < depth:
                result.append(node.val)
                print(result)

            if node.right:
                queue.append((node.right, depth + 1))
            if node.left:
                queue.append((node.left, depth + 1))

        return result
