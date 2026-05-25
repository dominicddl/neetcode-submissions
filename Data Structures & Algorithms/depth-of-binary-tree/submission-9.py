# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        frontier = deque()
        frontier.append((root, 1))
        res = 0

        while frontier:
            node, depth = frontier.popleft()
            
            if node.left:
                frontier.append((node.left, depth + 1))
            if node.right:
                frontier.append((node.right, depth + 1))

            res = max(depth, res)
        return res
        