import collections
        
def canFinish(numCourses, prerequisites): # prerequisites : 페어들의 목록
    graph = collections.defaultdict(list)
    # 그래프 구성
    for x, y in prerequisites:
        graph[x].append(y)
    
    traced = set() # 이미 방문한 노드를 저장. 방문한 곳을 재방문 할 경우는 순환구조

    def dfs(i):
        # 순환 구조일 경우 False 반환
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

answer = canFinish(2, [[1,0],[0,1]])
print(answer)