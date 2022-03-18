input1 = "A man, a plan, a canal: Panama" # True
input2 = "race a car" # False

# 내 코드
def solution(s):
    import re
    s = s.lower()
    s = re.sub(r'[^a-z0-9]', '', s)
    return s == s[::-1]


# 책 코드 (데크)
def solution(s):
    from collections import deque
    strs = deque()
    for c in s:
        if c.isalnum():
            strs.append(c.lower())
    
    while len(strs) > 1:
        if strs.popleft() != strs.pop(): return False
    return True
            
    
print(solution(input1))
print(solution(input2))