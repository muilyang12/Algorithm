# 105. Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_value = preorder[0]

        inorder_index = inorder.index(root_value)

        inorder_left = inorder[:inorder_index]
        inorder_right = inorder[inorder_index + 1 :]

        preorder_left = preorder[1 : 1 + len(inorder_left)]
        preorder_right = preorder[1 + len(inorder_left) :]

        root = TreeNode(root_value)

        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root
