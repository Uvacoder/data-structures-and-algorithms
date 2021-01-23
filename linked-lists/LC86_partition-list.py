# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        half1 = ListNode()
        half2 = ListNode()
        curr1 = half1 
        curr2 = half2
        
        while head:   #while head is not None
            if head.val < x:
                curr1.next = head
                head = head.next
                curr1 = curr1.next
            else:    #if head.val >= x:
                curr2.next = head
                head = head.next
                curr2 = curr2.next
        
        curr2.next = None
        curr1.next = half2.next
        
        return half1.next
