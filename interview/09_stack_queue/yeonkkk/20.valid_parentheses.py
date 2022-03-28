input = "()[]{}" # true

# 1. 나의 풀이 ------------------------------------------------------------------
def solution(input):
    check, stack = {")":"(", "}":"{", "]":"["}, []
    for i in input:
        if i in check.values(): stack.append(i)
        elif not stack or check[i] != stack.pop(): return False
    return False if stack else True


# 2. 스택 일치 여부 판별 (책) ---------------------------------------------------
def solution(input):
    stack = []
    table = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    # 스택 이용 예외 처리 및 일치 여부 판별
    for char in input:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0


print(solution(input))