# input 
nums, k = [1, 1, 1, 2, 2, 3], 2 # [1, 2]

# 1. 나의 풀이 ------------------------------------------------------------
def solution(nums, k):
    from collections import Counter 
    return [key for key, val in Counter(nums).items() if val >= k]

# 2. Counter를 이용한 음수 순 추출 -----------------------------------------
def solution(nums, k):
    from collections import Counter
    import heapq 
    freqs = Counter(nums)
    freqs_heap = []
    # 힙에 음수로 삽입
    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))
        
    topk = list()
    # k번 만큼 추출, 최소 힙(Min Heap) 이므로 가장 작은 음수 순으로 추출 
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])
        
    return topk

# 3. 파이썬다운 방식 -----------------------------------------------------------
def solution(nums, k):
    import collections
    return list(zip(*collections.Counter(nums).most_common(k)))[0]
    
    
print(solution(nums, k))