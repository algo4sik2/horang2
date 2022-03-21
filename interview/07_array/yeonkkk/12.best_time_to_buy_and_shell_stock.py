input = [7, 1, 5, 3, 6, 4] # output 5
input2 = [3, 7, 5, 6, 4, 1]  # output 4

# 나의 시도
def solution(input):
    max_diff = 0
    for i, n in enumerate(input):
        if n != input[-1]:
            if n >= max(input[i+1:]): continue
            else: max_diff = max(max_diff, max(input[i+1:]) - n)
    return max_diff


# 브루트 포스
def solution(prices):
    max_price = 0
    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)
    return max_price


# 저점과 현재 값과의 차이 계산
def solution(prices):
    import sys
    profit = 0
    min_price = sys.maxsize # 시스템 최댓값
    
    # 최솟값, 최댓값 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price-min_price)
    return profit

print(solution(input))