'''
problem_name = Merge Two Sorted Lists
problem_source = https://leetcode.com/problems/merge-two-sorted-lists/
Algo 
    -
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#Brute force approach
class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2
        elif not list2:
            return list1
        
        if list1.val <= list2.val:
            head = list1
        else:
            head = list2

        while list1 and list2:
            #Checking if list1 value is less or equal to the current list2 value
            if list1.val <= list2.val:
                #Checking if the lis1.next is null or not
                if not list1.next:
                    list1.next = list2
                    list1 = None
                    continue
                #Checking if the list1.next value is less or equel to the current list2 value
                if list1.next.val <= list2.val:
                    list1 = list1.next
                    continue
                next = list1.next
                list1.next = list2
                list1 = next
            #When the list2 is less than list1
            else:
                 #Checking if the lis2.next is null or not
                if not list2.next:
                    list2.next = list1
                    list2 = None
                    continue
                #Checking if list2.next is less than list1
                if list2.next.val < list1.val:
                    list2 = list2.next
                    continue
                next = list2.next
                list2.next = list1
                list2 = next
        return head





#Another Approach
class Solution:
    def mergeTwoLists(self, list1, list2):
        curr = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                curr.next, list1 = list1, list1.next
            else:
                curr.next, list2 = list2, list2.next
            curr = curr.next
        curr.next = list1 if list1 else list2
        return dummy.next



#Test                   
list1 = ListNode(4, ListNode(4, ListNode(4)))
list2 = ListNode(4, ListNode(4, ListNode(4)))
solve = Solution()
result = solve.mergeTwoLists(list1, list2)
for i in range(6):
    print(result.val, end=", ")
    result = result.next