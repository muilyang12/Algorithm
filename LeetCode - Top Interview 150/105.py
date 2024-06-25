# 105. Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Divide and conquer
    # time complexity: O(n ^ 2) (At the worst)
    # Sicing operation takes O(n)
    def buildTree1(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_value = preorder[0]

        inorder_index = inorder.index(root_value)

        inorder_left = inorder[:inorder_index]
        inorder_right = inorder[inorder_index + 1 :]

        preorder_left = preorder[1 : 1 + len(inorder_left)]
        preorder_right = preorder[1 + len(inorder_left) :]

        root = TreeNode(root_value)

        root.left = self.buildTree1(preorder_left, inorder_left)
        root.right = self.buildTree1(preorder_right, inorder_right)

        return root

    # Divide and conquer
    # time complexity: O(n) (At the worst)
    def buildTree2(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        inorder_value_index_map = {value: index for index, value in enumerate(inorder)}

        def build(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end:
                return None

            current_value = preorder[pre_start]
            node = TreeNode(current_value)

            inorder_index = inorder_value_index_map[current_value]
            inorder_left_count = inorder_index - in_start

            node.left = build(
                pre_start + 1,
                pre_start + inorder_left_count,
                in_start,
                inorder_index - 1,
            )
            node.right = build(
                pre_start + inorder_left_count + 1, pre_end, inorder_index + 1, in_end
            )

            return node

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
