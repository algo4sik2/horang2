# input
nums = [2, 7, 11, 15]
target = 9  #  output [0, 1]

# 나의 시도
def solution(nums, target):
    from itertools import combinations
    com = list(combinations(nums, 2))
    for c in com:
        if sum(c) == target: return [nums.index(c[0]), nums.index(c[1])] 
        # 같은 수가 다른 인덱스를 가지는 경우 고려하면 이건 틀린 코드다

# 브루트 포스  
def solution(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# in을 이용한 탐색(target-n 탐색)  
def solution(nums, target):
    for i, n in enumerate(nums):
        complement = target - n
        
        if complement in nums[i+1:]:
            return [nums.index(n), nums[i+1:].index(complement)+(i+1)] 
        # 왜 nums.index(complement)를 사용하지 않는지 궁금함 -> 같은 수가 다른 인덱스를 가지는 경우 고려


# 딕셔너리 활용  
def solution(nums, target):
    nums_map = {}
    # 키와 값을 바꿔 딕셔너리로 저장 
    for i, num in enumerate(nums):
        nums_map[num] = i
        
    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target-num]: return [i, nums_map[target - num]]


# 조회 구조 개선 
def solution(nums, target):
    nums_map = {}
    for i, n in enumerate(nums):
        if target - n in nums_map:
            return [nums_map[target - n], i]
        nums_map[n] = i


# 투 포인터 이용 -> 정렬 이용으로 인덱스 문제 생김 -> 풀이 불가  
def solution(nums, target):
    nums.sort()
    left, right = 0, len(nums) - 1
    while not left == right:
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]

print(solution(nums, target))