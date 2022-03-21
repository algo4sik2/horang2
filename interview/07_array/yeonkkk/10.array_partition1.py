from audioop import reverse

input = [1, 4, 3, 2] # output 4

# 나의 시도
def solution(input):
    input.sort()
    return sum(input[::2])

# 오름차순 풀이
def solution(nums):
    sum = 0
    pair = []
    nums.sort()
    
    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들어 합 계산
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []
    return sum

# 짝수 번째 값 계산
def solution(nums):
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        # 짝수 번째 값의 합 계산
        if i % 2 == 0: sum += n
    return sum

# 파이썬다운 방식
def solution(nums):
    return sum(sorted(nums)[::2])

print(solution(input))