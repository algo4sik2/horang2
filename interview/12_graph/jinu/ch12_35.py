def combine(n ,k):
    results = []

    def dfs(elements, start, k):
        if k == 0:
            results.append(elements[:])
            return

        # 자신 이전의 모든 값을 고정하여 재귀 호출
        for i in range(start, n+1): # start ~ 5 까지
            elements.append(i)
            dfs(elements, i+1, k-1) # start = i + 1 => 다음 조합 값. 중복을 방지하기 위해 i + 1. i는 이전 단계에서 사용한 숫자. k => 총 3자리 중 남은 자리 수 
            elements.pop()

    dfs([], 1, k)
    return results

n = 5
k = 3
answer = combine(n, k)
print(answer)