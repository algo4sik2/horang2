import collections
import heapq
from secrets import token_urlsafe

def topKFrequent(nums,k):
    freqs = collections.Counter(nums)
    freqs_heap = []
    # 힘에 음수로 삽입

    for f in freqs:
        heapq.heappush(freqs_heap, (-freqs[f], f))

    
    topk = list()
    # k번 만큼 추출, 최소 힙(Min Heap)이므로 가장 작은 음수 순으로 추출
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])

    return topk

nums = [1,1,1,2,2,3]
k =2

print(topKFrequent(nums, k))

