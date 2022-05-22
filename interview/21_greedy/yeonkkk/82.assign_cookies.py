import bisect
# Input
g, s = [1, 2, 3], [1, 1] # 1
# g, s = [1, 2], [1, 2, 3] # 2

# 1. 그리디 알고리즘
def solution(g, s):
    g.sort()
    s.sort()
    
    child_i = cookie_j = 0
    # 만족하지 못할 때까지 그리디 진행
    while child_i < len(g) and cookie_j < len(s):
        if s[cookie_j] >= g[child_i]:
            child_i += 1 
        cookie_j += 1
        
    return child_i

# 2. 이진 검색
def solution2(g, s):
    g.sort()
    s.sort()
    
    result = 0
    for i in s:
        # 이진 검색으로 더 큰 인덱스 탐색
        index = bisect.bisect_right(g, i)
        if index > result:
            result += 1
    return result 

print(solution(g, s))
print(solution2(g, s))