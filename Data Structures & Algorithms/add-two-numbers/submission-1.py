# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1 = 0
        curr1 = l1
        tens1 = 1
        while curr1:
            sum1 += curr1.val * tens1
            tens1 *= 10 
            curr1 = curr1.next
        
        sum2 = 0
        curr2 = l2
        tens2 = 1
        while curr2:
            sum2 += curr2.val * tens2
            tens2 *=10
            curr2 = curr2.next
        
        res = ListNode(0, None)
        curr = res
        sum = sum1 + sum2
        if sum == 0:
            return res
        
        while sum > 0:
            digit = sum % 10
            print(digit)
            temp = curr.next
            curr.next = ListNode(digit, None)
            curr = curr.next
            curr.next = temp
            sum //= 10
        
        return res.next
        

        