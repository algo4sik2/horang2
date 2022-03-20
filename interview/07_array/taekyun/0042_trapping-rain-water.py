from typing import List
'''
구상
    vars: left top, right top, left top idx, rigth top idx
    1.decrease할때까진 쭉 left top 업데이트 (initialize)
    2.decreas 되고 top보다 큰게 나오면 기존거 업데이트
    3.top은 인덱스로 찾 자 
'''

# 내풀이
'''
- 테케에 억지로 맞춤
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        if not height:
            return 0
        left_top, right_top = 0, len(height) - 1
        left, right = 0, len(height) - 1
        while left < len(height) and height[left] >= height[left_top]:
            left_top = left
            left += 1
        while right > 0 and height[right] >= height[right_top]:
            right_top = right  
            right -= 1
        if left == right:
            if height[left_top] > height[left] and height[right_top] > height[left]:
                smaller = min(height[left_top], height[right_top])
                total += smaller - height[left]
        while left < right:
            if height[left_top] < height[right_top]:
                while left < right and height[left] <= height[left_top]:
                    left += 1
                for i in range(left_top + 1, left):
                    if height[left_top] - height[i] > 0:
                        total += height[left_top] - height[i]
                if left == right and height[left_top] > height[left]:
                    total += height[left_top] - height[left]
                left_top = left
            else:
                while left < right and height[right] <= height[right_top]:
                    right -= 1
                for i in range(right + 1, right_top):
                    if height[right_top] - height[i] > 0:
                        total += height[right_top] - height[i]
                if left == right and height[right_top] > height[right]:
                    total += height[right_top] - height[right]
                right_top = right
        return total

"""
처음에 left max 찾는 과정이 필요 없음
while이 한번 실행될때 left나 right이 하나씩 움직임
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        volumn = 0
        if not height:
            return volumn
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        while left < right:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
            if left_max < right_max:
                left += 1
                if height[left] < left_max:
                    volumn += left_max - height[left]
            else:
                right -= 1
                if height[right] < right_max:
                    volumn += right_max - height[right]
        return volumn
    
    
'''
미리 left_max나 height[left] 중 max를 정해놓기 때문에 조건이 필요없음 
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        volumn = 0
        if not height:
            return volumn
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        while left < right:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
            if left_max < right_max:
                volumn += left_max - height[left]
                left += 1
            else:
                volumn += right_max - height[right]
                right -= 1
        return volumn
