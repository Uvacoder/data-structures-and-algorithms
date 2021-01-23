# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous = None
        curr = head
        while curr != None:
            temp = curr.next
            curr.next = previous
            previous = curr
            curr = temp
            
            head = previous   # don't forget to return the new head at the end! 
        
        return(head)
