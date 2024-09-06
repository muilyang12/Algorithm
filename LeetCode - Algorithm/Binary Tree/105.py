# 105. Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inValIndexMapper = {value: index for index, value in enumerate(inorder)}

        return self.createSubTree(
            preorder, inValIndexMapper, 0, len(preorder) - 1, 0, len(preorder) - 1
        )

    def createSubTree(
        self,
        preorder: List[int],
        inValIndexMapper: List[int],
        preStartIndex: int,
        preEndIndex: int,
        inStartIndex: int,
        inEndIndex: int,
    ) -> TreeNode:
        if preStartIndex > preEndIndex or inStartIndex > inEndIndex:
            return

        nodeVal = preorder[preStartIndex]
        node = TreeNode(nodeVal)

        nodeIndexInIn = inValIndexMapper[nodeVal]
        leftSubTreeLength = nodeIndexInIn - inStartIndex

        node.left = self.createSubTree(
            preorder=preorder,
            inValIndexMapper=inValIndexMapper,
            preStartIndex=preStartIndex + 1,
            preEndIndex=preStartIndex + leftSubTreeLength,
            inStartIndex=inStartIndex,
            inEndIndex=inStartIndex + leftSubTreeLength,
        )
        node.right = self.createSubTree(
            preorder=preorder,
            inValIndexMapper=inValIndexMapper,
            preStartIndex=preStartIndex + leftSubTreeLength + 1,
            preEndIndex=preEndIndex,
            inStartIndex=nodeIndexInIn + 1,
            inEndIndex=inEndIndex,
        )

        return node
