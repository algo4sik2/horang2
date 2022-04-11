# input
nums = [1, 2, 3]

# dfs를 활용한 순열 생성
def solution(nums):
    results = [] 
    prev_elements = []
    
    def dfs(elements):
        # 리프 노드일 때 결과 추가 
        if len(elements) == 0:
            results.append(prev_elements[:])
            
        # 순열 생성 재귀 호출
        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)
            
            prev_elements.append(e) 
            dfs(next_elements)
            prev_elements.pop()
            
    
    dfs(nums)
    return results 

# itertools 모듈 사용
# def solution(nums):
#     import itertools
#     return list(itertools.permutations(nums))

print(solution(nums))