'''
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL


Constraints:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
The length of the linked list is between [0, 10^4].
'''
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        evenhead = ListNode(0)
        odd = head
        even = evenhead
        current = head.next
        counter = 1
        while current:
            counter += 1
            if counter%2 ==0:
                even.next = current
                even = even.next
            else:
                odd.next = current
                odd = odd.next
            current = current.next
        odd.next = evenhead.next
        even.next = current
        return head