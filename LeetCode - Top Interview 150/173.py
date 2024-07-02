# 173. Binary Search Tree Iterator
# https://leetcode.com/problems/binary-search-tree-iterator/


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.inorder_values = []

        def get_inorder_values(node: Optional[TreeNode]):
            if not node:
                return

            get_inorder_values(node.left)
            self.inorder_values.append(node.val)
            get_inorder_values(node.right)

        get_inorder_values(root)

        self.current_index = -1

    def next(self) -> int:
        self.current_index += 1

        return self.inorder_values[self.current_index]

    def hasNext(self) -> bool:
        return self.current_index + 1 < len(self.inorder_values)
