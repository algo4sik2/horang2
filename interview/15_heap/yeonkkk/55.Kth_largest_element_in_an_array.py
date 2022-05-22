import heapq

# input
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4 

# 나의 풀이
def solution(nums, k):
    return sorted(nums, reverse=True)[k-1]

# 1. heapq 모듈 이용
def solution2(nums, k):
    heap = list()
    for n in nums:
        heapq.heappush(heap, -n)
    
    for _ in range(1, k):
        heapq.heappop(heap)
        
    return -heapq.heappop(heap)

# 2. heapq 모둘의 heapify 이용
def solution3(nums, k):
    heapq.heapify(nums)
    
    for _ in range(len(nums) - k):
        heapq.heappop(nums)
    
    return heapq.heappop(nums)

# 3. heapq 모듈의 nlargest 이용
def solution4(nums, k):
    return heapq.nlargest(k, nums)[-1]

# 4. 정렬을 이용한 풀이
def solution5(nums, k):
    return sorted(nums, reverse=True)[k-1]

print(solution(nums, k))
print(solution2(nums, k))
# print(solution3(nums, k))
print(solution4(nums, k))
# print(solution5(nums, k))


