# input
n, k = 4, 2

# dfs 로 k개 조합 생성
def solution(n, k):
    results = [] 
    
    def dfs(elements, starts, k):
        if k == 0:
            results.append(elements[:])
            return 
        
        # 자신 이전의 모든 값을 고정하여 재귀 호출 
        for i in range(starts, n+1):
            elements.append(i)
            dfs(elements, i+1, k-1)
            elements.pop()
            
    dfs([], 1, k)
    return results 

# itertools 모듈 사용 
# def solution(n, k):
#     import itertools 
#     return list(itertools.combinations(range(1, n+1), k))

print(solution(n, k))