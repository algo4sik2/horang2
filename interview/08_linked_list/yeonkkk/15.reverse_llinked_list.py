input = [1, 2, 3, 4, 5, None] # output = [None, 5, 4, 3, 2, 1]

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        
class Solution:
    # 1. 재귀 구조로 뒤집기 ---------------------------------------------------
    def revrseList(self, head):
        def reverse(node, prev):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        
        return reverse(head)
    
    # 2. 반복 구조로 뒤집기 ---------------------------------------------------
    def reverseList(self, head):
        node, prev = head, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
            
        return prev