# 106. Construct Binary Tree from Inorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/


from typing import Optional, List, Dict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderValIndexMapper = {value: index for index, value in enumerate(inorder)}

        return self.createSubTree(
            inorder,
            postorder,
            inorderValIndexMapper,
            0,
            len(inorder) - 1,
            0,
            len(inorder) - 1,
        )

    def createSubTree(
        self,
        postorder: List[int],
        inorderValIndexMapper: Dict[int, int],
        inStartIndex: int,
        inEndIndex: int,
        postStartIndex: int,
        postEndIndex: int,
    ) -> TreeNode:
        if inStartIndex > inEndIndex or postStartIndex > postEndIndex:
            return None

        rootVal = postorder[postEndIndex]

        node = TreeNode(rootVal)

        rootValIndexInIn = inorderValIndexMapper[rootVal]
        leftSubTreeSize = rootValIndexInIn - inStartIndex

        node.left = self.createSubTree(
            postorder,
            inorderValIndexMapper,
            inStartIndex,
            rootValIndexInIn - 1,
            postStartIndex,
            postStartIndex + leftSubTreeSize - 1,
        )
        node.right = self.createSubTree(
            postorder,
            inorderValIndexMapper,
            rootValIndexInIn + 1,
            inEndIndex,
            postStartIndex + leftSubTreeSize,
            postEndIndex - 1,
        )

        return node


"""
In the recursive function, the algorithm repeatedly searches for the index of a specific number 
in the inorder array. By creating a map in advance, I can introduce a method that increases the
overall time efficiency of the algorithm.

Initially, I tried to find the end index in the postorder array by searching for the number just
before the root number in the inorder array. Instead, if I subtract the start index of the 
inorder array from the index of the root value, I can avoid using the index function again.
"""
