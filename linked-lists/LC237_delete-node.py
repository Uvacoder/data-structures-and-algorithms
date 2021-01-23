# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 4 -> 5 -> 1 -> 9
        nextValue = node.next.val 
        node.val = nextValue   # 4 -> 1 -> 1 -> 9
        node.next = node.next.next
        
