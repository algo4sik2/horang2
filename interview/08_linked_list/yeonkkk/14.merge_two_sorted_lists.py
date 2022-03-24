# input
input1 = [1, 2, 4]
input2 = [1, 3, 4]

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        
class Solution:
    # 재귀 구조로 연결 (책)
    def mergetwolists(self, l1, l2): 
        # 작은 값이 왼쪽에 오게함
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergetwolists(l1.next, l2)
        return l1

ret = Solution.mergetwolists(input1, input2)
print(ret)
