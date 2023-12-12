# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def nextLargerNodes(self, head: [ListNode]) -> [int]:
        nodes = []
        current = head
        while current:
            nodes.append(current.val)
            current = current.next

        answer = [0]*len(nodes)
        stack = []

        for i in range(len(nodes)):
            while stack and nodes[stack[-1]] < nodes[i]:
                answer[stack[-1]] = nodes[i]
                stack.pop()

            stack.append(i)

        return answer

        
        