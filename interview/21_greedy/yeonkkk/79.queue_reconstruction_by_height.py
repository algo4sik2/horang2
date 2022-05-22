import heapq

# input
people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]

# 우선순위 큐 이용
def solution(people):
    heap = []
    # 키 역순, 인덱스 삽입
    for person in people:
        heapq.heappush(heap, (-person[0], person[1]))
        
    result = []
    # 키 역순 인덱스 추출
    while heap:
        person = heapq.heappop(heap)
        result.insert(person[1], [-person[0], person[1]])
    return result 

print(solution(people))
        