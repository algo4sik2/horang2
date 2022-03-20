'''
1. str > list
2. [::-1] is fastest
'''
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:   
        s = s.lower()
        s = re.sub(r'[^a-z0-9]','',s)
        return s == s[::-1]
        ''' str + 문자열 슬라이싱 뒤집기([::-1])
        processed = str()
        for w in s:
            if w.isalnum():
                processed += w.lower()
        return processed == processed[::-1]
        '''
        ''' list + 문자열 슬라이싱 뒤집기([::-1]
        52 ms	20.1 MB
        processed = list()
        for w in s:
            if w.isalnum():
                processed.append(w.lower())
        return processed == processed[::-1]
        '''
        ''' deque + 양쪽에서 원소 지워나가기
        77 ms	19.1 MB
        deq = deque()
        for w in s:
            if w.isalnum():
               deq.append(w.lower())
        while len(deq) > 1:
            if deq.pop() != deq.popleft():
                return False
        return True
        '''