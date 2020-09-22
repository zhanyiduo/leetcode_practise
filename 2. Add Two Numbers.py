'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        incre = 0
        head = ListNode(val=0, next=None)
        l3 = head
        while l1 or l2:
            if l1 and l2:
                val = l1.val + l2.val + incre
                l1 = l1.next
                l2 = l2.next
            elif l1:
                val = l1.val + incre
                l1 = l1.next
            else:
                val = l2.val + incre
                l2 = l2.next
            if val >= 10:
                val -= 10
                incre = 1
            else:
                incre = 0
            l3.next = ListNode(val=val, next=None)
            l3 = l3.next

        if incre:
            l3.next = ListNode(val=incre, next=None)
        return head.next
