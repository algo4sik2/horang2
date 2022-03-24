# input
input = [1, 2, 3, 4, 5] 
m, n = 2, 4

# output 1 -> 4 -> 3 -> 2 -> 5 -> Null

class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class Solution:
    # 반복 구조로 노드 뒤집기
    def reverseBetween(self, head, m, n):
        # 예외 처리
        if not head or m == n:
            return head 
        
        root = start = ListNode(None)
        root.next = head 
        # start, end 지정
        for _ in range(m-1):
            start = start.next
        end = start.next 
        
        # 반복하면서 노드 차례대로 뒤집기
        for _ in range(n-m):
            tmp, start.next, end.next = start.next, end.next, end.next.next 
            start.next.next = tmp
        return root.next 