# Brute-force
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
# using "in", range
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            diff = target - nums[i]
            if diff in nums[i + 1:]:
                return [i, nums[i + 1:].index(diff) + i + 1]
                
# using "in", range
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, v in enumerate(nums[:-1]):
            diff = target - v
            if diff in nums[i + 1:]:
                return [i, nums[i + 1:].index(diff) + i + 1]
                

# using "in", two enumerates 
# 처음에는 i != nums_dict[targe- n] 부분에서 리스트 nums 뒤에 인덱스에도 nums_dict[target - n] 값이 있을 수 있는데 넘어가면 어떡하지 라고 생각
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        for i, n in enumerate(nums):
            nums_dict[n] = i
        for i, n in enumerate(nums):
            if target - n in nums_dict.keys() and i != nums_dict[target - n]:
                return [i, nums_dict[target - n]]
            
# using "in", a enumerate                
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        for i, n in enumerate(nums):
            if target - n in nums_dict.keys() and i != nums_dict[target - n]:
                return [i, nums_dict[target - n]]
            nums_dict[n] = i
             
# using two pointer
# Failed: key is only one that makes treat harder
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_indexed = {}
        for i, n in enumerate(nums):
            nums_indexed[n] = i
        nums_sorted = sorted(nums_indexed)
        left, right = 0, len(nums_sorted) - 1    
        while left < right:
            if target == nums_sorted[left] + nums_sorted[right]:
                return [nums_indexed[nums_sorted[left]], nums_indexed[nums_sorted[right]]]
            elif target > nums_sorted[left] + nums_sorted[right]:
                left += 1
            else:
                right -= 1