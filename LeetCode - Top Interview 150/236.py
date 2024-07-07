# 236. Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # time complexity: O(n + h) = O(n)
    def lowestCommonAncestor1(
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

    def lowestCommonAncestor2(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        def findPath(node, target, path):
            if not node:
                return False

            path.append(node)

            if node == target:
                return True

            does_exist_left = findPath(node.left, target, path)
            does_exist_right = findPath(node.right, target, path)

            if does_exist_left or does_exist_right:
                return True

            path.pop()

            return False

        route_to_p = []
        route_to_q = []

        findPath(root, p, route_to_p)
        findPath(root, q, route_to_q)

        current = 0
        while (
            current < min(len(route_to_p), len(route_to_q))
            and route_to_p[current] == route_to_q[current]
        ):
            current += 1

        return route_to_p[current - 1]

    def lowestCommonAncestor3(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if not root:
            return None

        if root == p or root == q:
            return root

        node_from_left = self.lowestCommonAncestor2(root.left, p, q)
        node_from_right = self.lowestCommonAncestor2(root.right, p, q)

        if node_from_left and node_from_right:
            return root

        elif node_from_right:
            return node_from_right

        elif node_from_left:
            return node_from_left

        return None
