import bisect

# input1
# nums1, nums2 = [1, 2, 2, 1], [2, 2]
nums1, nums2 = [4, 9, 5], [9, 4, 9, 8, 4]

# 1. 나의 풀이ㅋ
def solution(nums1, nums2):
    return set(nums1).intersection(set(nums2))

# 2. 브루트 포스
def solution2(nums1, nums2):
    result = set()
    for n1 in nums1:
       for n2 in nums2:
           if n1 == n2:
               result.add(n1)
    return result   

# 3. 이진 검색
def solution3(nums1, nums2):
    result = set()
    nums2.sort()
    for n1 in nums1:
        # 이진 검색으로 일치 여부 판별
        i2 = bisect.bisect_left(nums2, n1)
        if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
            result.add(n1)
    return result

# 4. 투 포인터로 일치 여부 판별
def solution4(nums1, nums2):
    result = set()
    # 양쪽 모두 정렬
    nums1.sort()
    nums2.sort()
    i = j = 0
    # 투 포인터 우측으로 이동하며 일치 여부 판별 
    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            result.add(nums1[i])
            i += 1
            j += 1 
    
    return result 

# print(solution(nums1, nums2))
# print(solution2(nums1, nums2))
# print(solution3(nums1, nums2))
print(solution4(nums1, nums2))


