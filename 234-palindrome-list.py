'''
problem_name = Palindrome Linked List
problem_source = https://leetcode.com/problems/palindrome-linked-list/description/?envType=daily-question&envId=2024-03-22

Algo 
    -Try another approach:
    -Initialize two pointers, slow and fast, at the head of the linked list.
    -Move fast two steps at a time and slow one step at a time. When fast reaches the end of the list, slow will be at the middle.
    -Reverse the second half of the list, starting from where slow is.
    -Compare the first half of the list with the reversed second half. If they are the same, then the list is a palindrome
'''

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



from typing import Optional

#Iterative approach
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = [head.val]
        total = 1
        while head.next:
            head = head.next
            total += 1
            values.append(head.val)
        return values == values[::-1]
    

#Another Approach 1
