input1 = [2, 4, 3]
input2 = [5, 6, 4]

class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class Solution:
    # 1. 자료형 변환 -------------------------------------------------------
    # 연결 리스트 뒤집기
    def reverseList(self, head):
        node, prev = head, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        
        return prev
    
    # 연결 리스트 파이썬 리스트로 변환
    def toList(self, node):
        list = []
        while node:
            list.append(node.val)
            node = node.next 
        return list
    
    # 파이썬 리스트를 연결 리스트로 변환
    def toRverseLinkedList(self, result):
        prev = None
        for r in result:
            node = ListNode(r)
            node.next = prev
            prev = node

        return node
    
    # 두 연결 리스트의 덧셈
    def addTwoNumbers(self, l1, l2):
        a =  self.toList(self.reverseList(l1))
        b =  self.toList(self.reverseList(l2))
        
        resultStr = int(''.join(str(e) for e in a)) + \
                    int(''.join(str(e) for e in b))
        
        return self.toRverseLinkedList(str(resultStr))
    

    # 2. 전가산기 구현 ----------------------------------------------------------
    def addTwoNumbers(self, l1, l2):
        root = head = ListNode(0)
        
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            # 두 입력값의 합 계산
            if l1:
                sum += l1.val
                l1 = l1.next 
            if l2:
                sum += l2.val
                l2 = l2.next 
                
            # 몫(자리올림수)과 나머지(값) 계산
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next 
            
        return root.next
    
        