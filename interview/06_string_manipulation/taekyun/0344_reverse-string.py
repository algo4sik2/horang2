from typing import List

# 더블 포인터 
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
# list reverse 함수
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        
        
# 문자열 슬라이싱
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]