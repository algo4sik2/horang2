# 이중 연결 리스트로 풀이

input1 = [1, 2] # false
input2 = [1, 2, 2, 1] # true
input3 = [1, 2, 3, 2, 1] # true


# 1. 나의 시도 -----------------------------------------------------------
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
        
class Solution:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        new_node.prev = self.head
        
        self.head.next.prev = new_node
        self.head.next = new_node
    
    def insert_after(self, data, node):
        new_node = Node(data)
        new_node.next = node.next
        new_node.prev = node 
        
        node.next.prev = new_node
        node.next = new_node

    def insert_input(self, input):
        for i, val in enumerate(input):
            if i == 0: self.add_first(val)
            else: self.insert_after(val, self.tail.prev)

    def palindrome(self):
        cur = self.head.next
        val_list = []
        
        while cur is not self.tail:
            val_list.append(cur.data)
            cur = cur.next
        
        return True if val_list == val_list[::-1] else False
    
    # 2. 리스트 변환 ----------------------------------------------------------------
    def isPalindrome(self):
        q = []
        if not self.head.next: return True
        node = self.head.next
        # 리스트 변환
        while node.data is not None:
            q.append(node.data)
            # print(node.data, q)
            node = node.next
            
        # 팰린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False
        return True
    
    # 3. 데크를 이용한 최적화 ------------------------------------------------------
    def isPalindrome2(self):
        from collections import deque
        q = deque()
        
        if not self.head.next: return True
        node = self.head.next
        # 리스트 변환
        while node.data is not None:
            q.append(node.data)
            node = node.next
            
        # 팰린드롬 판별
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        return True
    
    # 4. 런너를 이용한 풀이 - 어떻게 바꿔야 하지? 실패... 질문하기 ---------------------
    def isPalindrome3(self):
        rev = None
        slow = fast = self.head.next
        
        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
            print('rev:', rev.data)
            print('slow:', slow.data)
            print('fast:', fast.data)            
            
        if fast:
            slow = slow.next
        
        # 팰린드롬 여부 확인
        while rev and rev.data == slow.data:
            # print('slow:', slow.data)
            # print('rev:', rev.data)
            slow, rev = slow.next, rev.next 
        return not rev
        
    
answer = Solution()
answer.insert_input(input3)
print(answer.palindrome()) # 내 풀이
print(answer.isPalindrome()) # 책 - 리스트 변환
print(answer.isPalindrome2()) # 책 - 데크 이용
print(answer.isPalindrome3()) # 책 - 런너 활용





        


