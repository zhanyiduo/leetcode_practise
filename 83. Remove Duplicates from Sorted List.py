'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
'''

'''
This code is faster than 99.58% submissions
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        curr_node = head
        next_node = head.next
        while curr_node.next != None:
            while curr_node.val == next_node.val:
                if next_node.next == None:
                    curr_node.next = next_node.next
                    return head
                next_node = next_node.next
            curr_node.next = next_node
            curr_node = next_node
            next_node = curr_node.next
        return head
