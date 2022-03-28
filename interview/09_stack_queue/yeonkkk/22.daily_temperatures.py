# input 
t = [73, 74, 75, 71, 69, 72, 76, 73] # output [1, 1, 4, 2, 1, 1, 0, 0]

# 1.스택값 비교
def solution(t):
    answer = [0] * len(t)
    stack = []
    for i, cur in enumerate(t):
        # 현재 온도가 스택 값보다 높다면 정답 처리
        while stack and cur > t[stack[-1]]:
            last = stack.pop()
            answer[last] = i -last 
        stack.append(i)
        
    return answer 
