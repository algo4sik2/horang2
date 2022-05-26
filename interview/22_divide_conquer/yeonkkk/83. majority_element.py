from collections import Counter, defaultdict

# input
# nums = [3, 2, 3]
nums = [2, 2, 1, 1, 1, 2, 2]

# 나의 풀이
def solution(nums):
    count = Counter(nums).most_common()
    if count[0][1] >= len(nums)//2: return count[0][0]

# 브루트 포스로 과반수 비교
def solution2(nums):
    for num in nums:
        if nums.count(num) > len(nums)//2: return num

# 다이나믹 프로그래밍
def solution3(nums):
    counts = defaultdict(int)
    for num in nums:
        if counts[num]== 0:
            counts[num] = nums.count(num)

        if counts[num] > len(nums) // 2:
            return num
   
# 분할 정복
def solution4(nums):
    if not nums:
        return None 
    if len(nums) == 1:
        return nums[0]
    
    half = len(nums) // 2
    a = solution4(nums[:half])
    b = solution4(nums[half:])
    
    return [b, a][nums.count(a)>half]

# 파이썬다운 방식
def solution5(nums):
    return sorted(nums)[len(nums)//2]

print(solution(nums))
print(solution2(nums))
print(solution3(nums))
print(solution4(nums))
print(solution5(nums))



