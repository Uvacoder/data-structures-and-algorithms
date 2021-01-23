# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Approach 1: Hash table
        llist = set()
        
        while head:  # loops until head is null. #if list is a cycle this will loop forever
            if head not in llist:
                llist.add(head)
            else:     # if the value is already in the list
                return True
            
            head = head.next
        
        return False
