# 100. Same Tree
# https://leetcode.com/problems/same-tree/


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # BFS - Breadth First Search
    def isSameTree1(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = []

        if p and not q:
            return False
        elif not p and q:
            return False
        elif p and q:
            queue.append((p, q))

        while queue:
            node_p, node_q = queue.pop(0)
            if node_p.val != node_q.val:
                return False

            if node_p.left and not node_q.left:
                return False
            elif not node_p.left and node_q.left:
                return False
            elif node_p.left and node_q.left:
                queue.append((node_p.left, node_q.left))

            if node_p.right and not node_q.right:
                return False
            elif not node_p.right and node_q.right:
                return False
            elif node_p.right and node_q.right:
                queue.append((node_p.right, node_q.right))

        return True

    # BFS - Breadth First Search
    def isSameTree2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = []
        queue.append((p, q))

        while queue:
            node_p, node_q = queue.pop(0)
            if not node_p and not node_q:
                continue
            elif (node_p and not node_q) or (not node_p and node_q):
                return False
            elif node_p.val != node_q.val:
                return False

            queue.append((node_p.left, node_q.left))
            queue.append((node_p.right, node_q.right))

        return True

    # DFS - Depth First Search
    def isSameTree3(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if (not p and q) or (p and not q):
            return False

        if p.val != q.val:
            return False

        return self.isSameTree3(p.left, q.left) and self.isSameTree3(p.right, q.right)
