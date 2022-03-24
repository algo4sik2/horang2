input1 = [1, 2, 3, 4, 5] # output = [1, 3, 5, 2, 4]
input2 = [2, 1, 3, 5, 6, 4, 7] # output = [2, 3, 6, 7, 1, 5, 4]

class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class Solution:
    # 반복 구조로 홀짝 노드 처리
    def oddEvenList(self, head):
        # 예외 처리
        if head is None:
            return None
        
        odd = head
        even = head.next
        even_head = head.next
        
        # 반복하면서 홀짝 노드 처리
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next 
            odd, even = odd.next, even.next
        
        # 홀수 노드의 마지막을 짝수 헤드로 연결
        odd.next = even_head
        return head