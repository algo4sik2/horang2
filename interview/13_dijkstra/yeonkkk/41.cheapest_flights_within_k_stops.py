# input
n = 3
edges = [[0, 1, 100],
         [1, 2, 100],
         [0, 2, 500]]
src, dst, K = 0, 2, 0 

# 다익스트라 알고리즘 응용 
def solution(n, flights, src, dst, K):
    from collections import defaultdict 
    import heapq 
    
    graph = defaultdict(list)
    # 그래프 인접 리스트 구성
    for u, v, w in flights:
        graph[u].append((v, w))
        
    # 큐 변수: [(가격, 정점, 남은 가능 경유지 수)]
    Q = [(0, src, K)]
    
    # 우선순위 큐 최솟값 기준으로 도착점가지 최소 비용 판별
    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k >= 0:
            for v, w in graph[node]:
                alt = price + w 
                heapq.heappush(Q, (alt, v, k-1))
    return -1