# input
prices = [7, 1, 5, 3, 6, 4] # 7

# 1.그리디 알고리즘
def solution(prices):
    result = 0 
    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            result += prices[i + 1] - prices[i]
    return result 

# 2.파이썬 다운 방식
def solution2(prices):
    return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))

print(solution(prices))
print(solution2(prices))