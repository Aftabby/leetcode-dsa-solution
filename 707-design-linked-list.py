'''
problem_name = Design Linked List
problem_source = https://leetcode.com/problems/design-linked-list/description/

Algo 
    -
'''


class NewNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:

    def __init__(self):
        self.head = NewNode(0, NewNode())       #Setting up a dummy head and tail node that makes easier to keep track of the linked list
        self.tail = self.head.next
        self.tail.prev = self.head
        self.length = 0

    def get(self, index: int) -> int:
        curr = self.head.next
        if index >= self.length:
            return -1
        for i in range(index):      
            curr = curr.next
        return curr.val     


    def addAtHead(self, val: int) -> None:
        new_node = NewNode(val, self.head.next, self.head)
        self.head.next.prev = new_node
        self.head.next = new_node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        new_node = NewNode(val, self.tail, self.tail.prev)
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head.next
        if index > self.length:
            return
        elif index == self.length:
            self.addAtTail(val)
            return
        else:
            for _ in range(index):
                curr = curr.next
            new_node = NewNode(val, curr, curr.prev)
            curr.prev.next = new_node
            curr.prev = new_node
        self.length += 1 


    def deleteAtIndex(self, index: int) -> None:
        if index < self.length:
            curr = self.head.next
            self.length -= 1
            for _ in range(index):
                curr = curr.next
            curr.prev.next = curr.next
            curr.next.prev = curr.prev


solve = MyLinkedList()
solve.addAtHead(5)
solve.addAtIndex(1, 2)
print(solve.get(1))
solve.addAtHead(6)
solve.addAtTail(2)
print(solve.get(3))
solve.addAtTail(1)
print(solve.get(5))



solve.addAtIndex(1, 2)
solve.deleteAtIndex(1)
print(solve.get(1))










# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)