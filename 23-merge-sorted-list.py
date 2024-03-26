'''
problem_name = Merge k Sorted Lists
problem_source = https://leetcode.com/problems/merge-k-sorted-lists/description/

Algo 
    -
'''

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return
        #helper function - two compare and merge two singly linked list
        def merge_lists(list2, lists1 = lists[0]):
            head = curr = ListNode()
            while lists1 and list2:
                if lists1.val <= list2.val:
                    curr.next = lists1
                    curr = curr.next
                    lists1 = lists1.next
                else:
                    curr.next = list2
                    curr = curr.next
                    list2 = list2.next
            if lists1:
                curr.next = lists1
            elif list2:
                curr.next = list2
            return head.next
        
        #The actual part of the code-


        #We are comparing and merging the result in lists[0] , and comparing the next element with the merged result (lists[0])
        for _ in range(1, len(lists)):
            lists[0] = merge_lists(lists[_], lists[0])
       
        #return the first element of the list
        return lists[0]
        


