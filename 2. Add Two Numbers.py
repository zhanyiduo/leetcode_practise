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
        if (not l1) | (not l2):
            return None
        else:
            adv = 0
            l3 = ListNode(0)
            l4 = l3
            suml = 0
            while l1 or l2 or suml:
                if l1:
                    suml += l1.val
                    l1 = l1.next
                if l2:
                    suml += l2.val
                    l2 = l2.next
                l3.next = ListNode(suml % 10)
                l3 = l3.next
                suml //= 10
        return l4.next
