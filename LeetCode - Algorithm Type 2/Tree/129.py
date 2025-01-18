from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(node: Optional[TreeNode], route: List[int]):
            nonlocal result

            route.append(node.val)

            if node.left:
                dfs(node.left, route)
            if node.right:
                dfs(node.right, route)
            if not node.left and not node.right:
                numStr = ""
                for digit in route:
                    numStr += str(digit)

                result += int(numStr)

            route.pop()

        dfs(root, [])

        return result
