# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Fast and Slow Pointer technique 
        slow = head
        fast = head.next
        # This causes slow to be at the middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Separate the list into 2
        second = slow.next # Start of the second half
        slow.next = None # End of the first half

        prev = None
        # Reverse the second half of the list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        first = head
        second = prev

        # Merge the two lists
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

        
        
        


        