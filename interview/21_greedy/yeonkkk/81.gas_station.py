# input 
gas, cost = [1, 2, 3, 4, 5], [3, 4, 5, 1, 2] # 3

# 1. 모두 방문 
def solution(gas, cost):
    for start in range(len(gas)):
        fuel = 0 
        for i in range(start, len(gas) + start):
            index =i % len(gas)
            
            can_travel = True 
            if gas[index] + fuel < cost[index]:
                can_travel = False 
                break
            else:
                fuel += gas[index] - cost[index]
        if can_travel:
            return start 
    return -1

# 2. 한 번 방문 
def solution2(gas, cost):
    # 모든 주유소 방문 가능 여부 판별
    if sum(gas) < sum(cost):
        return -1
    
    start, fuel = 0, 0 
    for i in range(len(gas)):
        # 출발점이 안되는 지점 판별
        if gas[i] + fuel < cost[i]:
            start = i + 1
            fuel = 0
        else:
            fuel += gas[i] - cost[i]
    return start

print(solution(gas, cost))
print(solution2(gas, cost))
