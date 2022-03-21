input = [1, 2, 3, 4] # output = [24, 12, 8, 6]

# 나의 시도
def solution(input):
    answer, result = [] , 1
    for i in range(len(input)):
        for j, n in enumerate(input):
            if i != j: result *= n
        answer.append(result)
        result = 1
    return answer

# 왼쪽 곱셈 겨로가에 오른쪽 값을 차례대로 곱셈
def solution(nums):
    out = []
    p = 1
    # 왼쪽 곱셈
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
    p = 1
    # 왼쪽 곱셈 결과와 오른쪽 값을 차례대로 곱셈
    for i in range(len(nums) - 1, 0 - 1, -1):
        out[i] = out[i] * p
        p = p * nums[i]
    return out

print(solution(input))