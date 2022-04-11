# sol1. dfs
import collections

def findItinerary(tickets):
    graph = collections.defaultdict(list)
    # 그래프 순서대로 구성
    for a, b in sorted(tickets): # 사전 순으로 정렬
        graph[a].append(b)

    route = []
    def dfs(a):
        # 첫 번째 값을 읽어 어휘 순 방문
        while graph[a]:
            dfs(graph[a].pop(0))
        route.append(a)

    dfs('JFK')
    # 다시 뒤집기
    return route[::-1]

# sol2. 스택 연산으로 큐 연산 최적화

def findItinerary2(tickets):
    graph = collections.defaultdict(list)

    # 그래프를 뒤집어서 구성
    for a, b in sorted(tickets, reverse = True):
        graph[a].append(b)

    route = []
    def dfs(a):
        # 마지막 값을 읽어 어휘 순 방문
        while graph[a]:
            dfs(graph[a].pop())
        route.append(a)

    dfs('JFK')

    return route[::-1]

# sol3. 일정 그래프 반복

def findItinerary3(tickets):
    graph = collections.defaultdict(list)
    # 그래프 순서대로 구성
    for a, b in sorted(tickets):
        graph[a].append(b)

    route, stack = [], ['JFK']
    while stack:
        # 반복으로 스택으로 구성하되 막히는 부분에서 풀어내는 처리
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
        route.append(stack.pop())

    return route[::-1] # 어차피 stack에 순서대로 다 들어가 있는데 그냥 스택을 반환하면 되지 않나??
 
tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
tickets2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

# findItinerary(tickets)
# findItinerary(tickets2)

# findItinerary2(tickets)
# findItinerary2(tickets2)

findItinerary3(tickets)
# findItinerary3(tickets2)