# input
times = [[3, 1, 5], [3, 2, 2], [2, 1, 2], [3, 4, 1],
         [4, 5, 1], [5, 6, 1], [6, 7, 1], [7, 8, 1], [8, 1, 1]]
N, K = 8, 3 

# 다익스트라 알고리즘 구현
def solution(times, N, K):
    from collections import defaultdict
    import heapq
    graph = defaultdict(list)
    # 그래프 인접 리스트 구성
    for u, v, w in times:
        graph[u].append((v, w))
        
    # 큐 변수: [(소요 시간, 정점)]
    Q = [(0, K)]
    dist = defaultdict(int)
    
    # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))
                
    # 모든 노드의 최단 경로 존재 여부 판별
    if len(dist) == N:
        return max(dist.values())
    return -1

print(solution(times, N, K))