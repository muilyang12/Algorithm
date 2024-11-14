# 1372. Longest ZigZag Path in a Binary Tree
# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

from typing import Optional, Literal, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = -1

        def dfs(node: TreeNode, route: List[str]):
            nonlocal result

            if not node.left and not node.right:
                result = max(result, self.countZigZagLength(route))

            if node.left:
                route.append("l")
                dfs(node.left, route)
                route.pop()

            if node.right:
                route.append("r")
                dfs(node.right, route)
                route.pop()

        dfs(root, [])

        return result

    def countZigZagLength(self, zigZag: List[Literal["l", "r"]]) -> int:
        if len(zigZag) == 0:
            return 0

        lengthRecord = []

        currentLength = None
        previous = None

        for direction in zigZag:
            if not previous:
                previous = direction
                currentLength = 1

                continue

            if previous == direction:
                lengthRecord.append(currentLength)
                currentLength = 1

                continue

            previous = direction
            currentLength += 1

        lengthRecord.append(currentLength)

        return max(lengthRecord)
