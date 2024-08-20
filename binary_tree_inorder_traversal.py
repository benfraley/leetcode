# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # function to recursively check the left value, then root, then right
        # and append in that order
        def traverse(node, values):
            if node.left != None:
                traverse(node.left, values)
            values.append(node.val)
            if node.right != None:
                traverse(node.right, values)

        values = []
        if root != None:
            traverse(root, values)
        return values

        