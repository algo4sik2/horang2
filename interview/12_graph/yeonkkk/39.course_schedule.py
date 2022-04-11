# input
numcourses = 2
prerequisites = [[1, 0]] # true

# dfs로 순환 구조 판별
def solution(numcourses, prerequisites):
    import collections 
    
    graph = collections.defaultdict(list)
    # 그래프 구성
    for x, y in prerequisites:
        graph[x].append(y)
        
    traced = set()
    
    def dfs(i):
        # 순환 구조이면 false
        if i in traced:
            return False 
        
        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False 
        # 탐색 종료 후 순환 노드 삭제
        traced.remove(i)
        return True 
    
    # 순환 구조 판별
    for x in list(graph):
        if not dfs(x):
            return False 
        
    return True 

# 가지치기를 이용한 최적화
def solution(numcourses, prerequisites):
    import collections 
    graph = collections.defaultdict(list)
    # 그래프 구성
    for x, y in prerequisites:
        graph[x].append(y)
        
    traced = set()
    visited = set()
    
    def dfs(i):
        # 순환 구조이면 False
        if i in traced:
            return False 
        # 이미 방문했던 노드이면 True 
        if i in visited:
            return True 
        
        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False 
            
            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)
            # 탐색 종료 후 방문 노드 추가
            visited.add(i)
            
            return True 
        
        # 순환 구조 판별 
        for x in list(graph):
            if not dfs(x):
                return False 
        return True

print(solution(numcourses, prerequisites))