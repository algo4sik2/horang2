# input 
J, S = "aA", "aAAbbbb" # output: 3

# 1. 나의 풀이 --------------------------------------------------------
def solution(J, S):
    j_stones = {}
    for key in set(S):
        if key in list(J): j_stones[key] = S.count(key)
    return sum(j_stones.values())
 
# 2. 책: 해시 테이블을 이용한 풀이 ------------------------------------
def solution(J, S):
    freqs = {}
    count = 0
    
    # 돌(S)의 빈도 수 계산
    for char in S:
        if char not in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1
    
    # 보석(J)의 빈도 수 합산
    for char in J:
        if char in freqs:
            count += freqs[char]
    
    return count

# 3. 책: defaultdict 를 이용한 비교 생략 --------------------------------
def solution(J, S):
    from collections import defaultdict
    freqs = defaultdict(int)
    count = 0
    
    # 비교 없이 돌(S) 빈도 수 계산
    for char in S:
        freqs[char] += 1
        
    # 비교 없이 보석(J) 빈도 수 합산
    for char in J:
        count += freqs[char]
    
    return count 

# 4. 책: counter 로 계산 생략 ----------------------------------------------
def solution(J, S):
    from collections import Counter
    freqs = Counter(S)
    count = 0 
    
    # 비교 없이 (J) 빈도 수 합산
    for char in J:
        count += freqs[char]
    
    return count 

# 5. 책: 파이썬 다운 방식 ---------------------------------------------------
def solution(J, S):
    return sum(s in J for s in S)
 
print(solution(J, S))