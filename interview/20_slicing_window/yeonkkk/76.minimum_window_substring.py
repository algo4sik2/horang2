import collections

# input
S, T = "ADOBECODEBANC", "ABC"   # "BANC"

def solution(s, t):
    need = collections.Counter(t)
    missing = len(t)
    left = start = end = 0
    
    # 오른쪽 포인터 이동
    for right, char in enumerate(s, 1):
        missing -= need[char] > 0
        need[char] -= 1 
        
        # 필요 문자가 0이면 왼쪽 포인터 이동 판단
        if missing == 0:
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            
            if not end or right - left <= end - start:
                start, end = left, right
                need[s[left]] += 1
                missing += 1
                left += 1
    return s[start:end]

def solution2(s, t):
    t_count = collections.Counter(t)
    current_count = collections.Counter()
    
    start = float('-inf')
    end = float('inf')
    
    left = 0
    # 오른쪽 포인터 이동
    for right, char in enumerate(s, 1):
        current_count[char] += 1 
        
        # AND 연산 결과로 왼쪽 포인터 이동 판단
        while current_count & t_count == t_count:
            if right - left < end - start:
                start, end = left, right 
            current_count[s[left]] -= 1 
            left += 1 
    
    return s[start: end] if end - start <= len(s) else ''
    
    
# print(solution(S, T))
print(solution2(S, T))
