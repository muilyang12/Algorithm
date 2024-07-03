# 236. Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        route_to_p = None
        route_to_q = None

        queue = []
        queue.append((root, []))

        while queue:
            node, nodes_before_current = queue.pop(0)

            if node.val == p.val:
                route_to_p = nodes_before_current[:]
                route_to_p.append(node)

            elif node.val == q.val:
                route_to_q = nodes_before_current[:]
                route_to_q.append(node)

            if route_to_p and route_to_q:
                break

            if node.left:
                temp = nodes_before_current[:]
                temp.append(node)
                queue.append((node.left, temp))
            if node.right:
                temp = nodes_before_current[:]
                temp.append(node)
                queue.append((node.right, temp))

        current = 0
        while (
            current < min(len(route_to_p), len(route_to_q))
            and route_to_p[current] == route_to_q[current]
        ):
            current += 1

        return route_to_p[current - 1]
