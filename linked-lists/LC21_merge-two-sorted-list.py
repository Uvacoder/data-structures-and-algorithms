# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode() 
        tail = dummy
        
        while l1 and l2:    # always loops until l1 and l2 reach null 
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:     # if l2.val is smaller OR if l1 & l2 values are the same
                tail.next = l2
                l2 = l2.next
                
            tail = tail.next
        
        # if either l1 or l2 reaches null first, append the rest of the list that is not null
        if l1 == None:
            tail.next = l2
        elif l2 == None:
            tail.next = l1
         
        
        return dummy.next 
