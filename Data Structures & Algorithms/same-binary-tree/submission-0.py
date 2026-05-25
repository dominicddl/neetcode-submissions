# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # p's queue
        queue1 = deque()
        # q's queue
        queue2 = deque()

        queue1.append(p)
        queue2.append(q)

        while queue1 and queue2:
            pnode, qnode = queue1.popleft(), queue2.popleft()

            if not pnode and not qnode:
                continue

            if not pnode or not qnode:
                return False

            if pnode.val != qnode.val:
                return False
            
            queue1.append(pnode.left)
            queue1.append(pnode.right)
            queue2.append(qnode.left)
            queue2.append(qnode.right)
        
        return True
        