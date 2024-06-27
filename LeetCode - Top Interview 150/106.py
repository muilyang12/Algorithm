# 106. Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        inorder_value_index_mapper = {
            value: index for index, value in enumerate(inorder)
        }

        def build(in_start, in_end, post_start, post_end):
            if in_start > in_end or post_start > post_end:
                return None

            root_val = postorder[post_end]
            node = TreeNode(root_val)

            root_val_index = inorder_value_index_mapper[root_val]
            left_tree_size = root_val_index - in_start

            node.left = build(
                in_start,
                root_val_index - 1,
                post_start,
                post_start + left_tree_size - 1,
            )
            node.right = build(
                root_val_index + 1,
                in_end,
                post_start + left_tree_size,
                post_end - 1,
            )

            return node

        return build(0, len(inorder) - 1, 0, len(postorder) - 1)
