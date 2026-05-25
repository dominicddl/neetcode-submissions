# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return -1
        
        leftHeight = self.get_height(node.left)
        rightHeight = self.get_height(node.right)

        return 1 + max(leftHeight, rightHeight)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        leftHeight = self.get_height(root.left)
        rightHeight = self.get_height(root.right)

        res = abs(leftHeight - rightHeight)

        if res > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
            