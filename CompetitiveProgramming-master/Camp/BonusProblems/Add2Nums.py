# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.head = None

    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        list1 = []
        list2 = []
        p1, p2 = l1, l2
        while p1 or p2:
            if p1:
                list1.append(str(p1.val)) 
                p1 = p1.next
            if p2:
                list2.append(str(p2.val))
                p2 = p2.next

        
        list3 = str(int(''.join(reversed(list1))) + int(''.join(reversed(list2))))


        for i in range(len(list3)):
            obj = ListNode(list3[i])
            if self.head:
                obj.next = self.head
                self.head = obj
            else:
                self.head = obj

        return self.head
            
        