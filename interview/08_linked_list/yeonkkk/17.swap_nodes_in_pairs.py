input = [1, 2, 3, 4] # output 2 1 4 3


class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class Solution:
    # 1. 값만 교환 ----------------------------------------------------------
    def swapPairs(self, head):
        cur = head 
        
        while cur and cur.next:
            # 값만 교환
            cur.val, cur.next.val = cur.next.val, cur.val
            print(cur.val, cur.next.val)
            cur = cur.next.next
        return head
    
    # 2. 반복 구조로 스왑 ---------------------------------------------------
    def swapPairs(self, head):
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            # b가 a(head)를 가리키도록 할당
            b = head.next
            head.next = b.next 
            b.next = head
            
            # prev가 b를 가리키도록 할당
            prev.next = b 
            
            # 다음번 비교를 위해 이동
            head = head.next 
            prev = prev.next.next
        return root.next
    
    # 3. 재귀 구조로 스왑 ----------------------------------------------------
    def swapPairs(self, head):
        if head and head.next:
            p = head.next 
            # 스왑된 값 리턴 받음
            head.next = self.swapPairs(p.next)
            p.next = head 
            return p
        return head 