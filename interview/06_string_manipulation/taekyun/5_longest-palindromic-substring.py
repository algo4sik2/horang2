# 시간초과
class Solution:
    def longestPalindrome(self, s: str) -> str:
        orglen = len(s)
        strlen = len(s)
        while strlen > 1:
            start = 0
            while start + strlen <= orglen:
                substr = s[start:start+strlen]
                left, right = 0, strlen - 1
                while left < right:
                    if substr[left] != substr[right]:
                        break
                    left += 1
                    right -= 1
                if left >= right:
                    return substr
                start += 1
            strlen -= 1
        return s[0]
    
# 시간초과 2
class Solution:
    def longestPalindrome(self, s: str) -> str:
        orglen = len(s)
        strlen = len(s)
        while strlen > 1:
            start = 0
            while start + strlen <= orglen:
                substr = s[start:start+strlen]
                if substr == substr[::-1]:
                    return substr
                start += 1
            strlen -= 1
        return s[0]
    
# 책풀이
def expand(s: str, i: int, j:int, max_len:int) -> str:
    strlen = len(s)
    longest = min(i + 1 - 0, strlen - j) 
    longest = longest * 2 + j - i - 1
    if max_len > longest:
        return ''
    while i >= 0 and j < strlen and s[i] == s[j]:
        i -= 1
        j += 1
    return s[i+1:j]   

class Solution:
    def longestPalindrome(self, s: str) -> str:
        strlen = len(s)
        if strlen < 2:
            return s
        start = 0
        result = s[0]
        while start + 1 < strlen:
            max_len = len(result)
            result = (
                max(result, expand(s, start, start + 1, max_len),
                    expand(s, start, start+2, max_len), key=len)
            )
            start += 1
        return result
    
# 시간 최적화
def expand(s: str, i: int, j:int, max_len:int) -> str:
    strlen = len(s)
    longest = min(i + 1 - 0, strlen - j) 
    longest = longest * 2 + j - i - 1
    if max_len > longest:
        return ''
    while i >= 0 and j < strlen and s[i] == s[j]:
        i -= 1
        j += 1
    return s[i+1:j]   

class Solution:
    def longestPalindrome(self, s: str) -> str:
        strlen = len(s)
        if strlen < 2:
            return s
        start = 0
        result = s[0]
        while start + 1 < strlen:
            max_len = len(result)
            result = (
                max(result, expand(s, start, start + 1, max_len),
                    expand(s, start, start+2, max_len), key=len)
            )
            start += 1
        return result