# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3_list = ListNode(0)
        if not l1 or not l2:
            return l1 or l2
        if l1.val <= l2.val:
            l3_list.val = l1.val
            l3_list.next = self.mergeTwoLists(l1.next,l2)
        else:
            l3_list.val = l2.val
            l3_list.next = self.mergeTwoLists(l1,l2.next)
        return l3_list
