# 876. Middle of the Linked List (Easy)

# Given a non-empty, singly linked list with head node head, return a middle node of linked list.

# If there are two middle nodes, return the second middle node.

# Example 1:
#     Input: [1,2,3,4,5]
#     Output: Node 3 from this list (Serialization: [3,4,5])

#     The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
#     Note that we returned a ListNode object ans, such that:
#     ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

# Example 2:
#     Input: [1,2,3,4,5,6]
#     Output: Node 4 from this list (Serialization: [4,5,6])
#     Since the list has two middle nodes with values 3 and 4, we return the second one.
 

# Note:
#     The number of nodes in the given list will be between 1 and 100.


import math 

class Solution:
    def get_length(self, head):
        counter = 1
        current = head
        
        while current.next:
            current = current.next
            counter += 1
        return counter
    
    def middleNode(self, head: ListNode) -> ListNode:
        length = self.get_length(head)
        idx = math.floor(length/2 + 1)
        counter = 1
        current = head
        while idx != counter:
            current = current.next
            counter += 1
        return current



# First Solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#class Solution:
#     def get_length(self, head):
#         counter = 1
#         current = head
        
#         while current: 
#             if current.next == None:
#                 return counter
#             else:
#                 current = current.next
#                 counter += 1
    
#     def middleNode(self, head: ListNode) -> ListNode:
#         length = self.get_length(head)
#         if length % 2 == 0:
#             idx = length/2 + 1
#         else:
#             idx = length/2 + 0.5
#         counter = 1
#         current = head
#         while idx != counter:
#             current = current.next
#             counter += 1
#         return current
