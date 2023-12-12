# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head:[ListNode]) -> bool:
        current = head 
        list_dict = {}
        while current:
            if current in list_dict:
                return True
            list_dict[current] = 1

            current = current.next   

        return False
        

        