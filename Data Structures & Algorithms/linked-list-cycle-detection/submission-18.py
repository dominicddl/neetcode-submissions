# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head
        fast = head
        while slow.next and fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next == None:
                break
            fast = fast.next
            if slow.val == fast.val:
                return True
        return False