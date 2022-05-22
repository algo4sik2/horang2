import collections

# input 
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

# while문 이용
def solution(nums, k):
    i = 0
    result = []
    while len(nums[i:i+k]) == k:
        result.append(max(nums[i:i+k]))
        i += 1
    return result

# for문 이용
def solution2(nums, k):
    result = []
    for i in range(len(nums)):
        if len(nums[i:i+k]) < k: break
        result.append(max(nums[i:i+k]))
    return result 


# for문 이용 2
def solution3(nums, k):
    result = []
    for i in range(len(nums)-k+1):
        result.append(max(nums[i:i+k]))
    return result 

# deque 이용
def solution4(nums, k):
    result = []
    window = collections.deque()
    current_max = float('-inf')
    for i, v in enumerate(nums):
        window.append(v)
        if i < k-1:
            continue 
        
        if current_max == float('-inf'):
            current_max = max(window)
        elif v > current_max:
            current_max = v
            
        result.append(current_max)
        
        if current_max == window.popleft():
            current_max = float('-inf')
    
    return result


print(solution(nums, k))
print(solution2(nums, k))
print(solution3(nums, k))
print(solution4(nums, k))


