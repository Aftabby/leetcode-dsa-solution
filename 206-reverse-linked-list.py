"""
problem_name = Reverse Linked List
problem_source = https://leetcode.com/problems/reverse-linked-list/

Algo 
    -Change the current nodes pointer to point to its previous node
    -Since a node does not have reference to its previous node, we must store its previous element beforehand
    -As we are changing the reference (as per first step) we also need another pointer to store the next node before changing the reference
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Recursive Approach
class Solution:
    def reverseList(self, head, prev=None):
        if not head:
            return head
        next = head.next
        head.next = prev
        if not next:
            return head
        else:
            return self.reverseList(next, head)


# Another recursive Approach
class Solution:
    def reverseList(self, head, prev=None) -> ListNode:
        if not head:
            return prev
        else:
            reversed_head = self.reverseList(head.next, head)
            head.next = prev
            return reversed_head


# Iteration Approach
class Solution:
    def reverseList(self, head):
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev


listnode = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
solve = Solution()
rev_list = solve.reverseList(listnode)
print(rev_list.val, rev_list.next.val, rev_list.next.next.val)
