# sol2. 가지치기를 이용한 최적화

import collections

def canFinish2(numCourses, prerequisites):
    graph = collections.defaultdict(list)
    # 그래프 구성
    for x, y in prerequisites:
        graph[x].append(y)
    
    traced = set() # 이미 지나간 노드의 시작점을 저장 (0,1,2,3,4)
    visited = set() # 이미 확인한 경로를 저장. visitied에 저장되어 있는 경로에서 시작하는 코스는 이미 확인이 끝난 것이기 때문에 또 확인할 필요가 없으므로 True 반환

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

answer = canFinish2(5, [[0,1],[1,2],[2,3],[3,4]])
print(answer)

