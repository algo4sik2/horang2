import collections
# input 
s, k = "AAABBC", 2
    
# 투 포인터, 슬라이딩 윈도우, counter 이용 
def solution(s, k):
    left = right = 0
    counts = collections.Counter()
    for right in range(1, len(s) + 1):
        counts[s[right - 1]] += 1 
        # 가장 흔하게 등장하는 문자 탐색
        max_char_n = counts.most_common(1)[0][1]
        
        # k 초과시 왼쪽 포인터 이동
        if right - left - max_char_n > k:
            counts[s[left]] -= 1
            left += 1
    return right - left 

print(solution(s, k))
