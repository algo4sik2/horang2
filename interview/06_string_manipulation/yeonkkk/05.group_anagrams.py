input = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

# 내 코드
def solution(input):
    from collections import defaultdict
    result = defaultdict(list)
    for i in input:
        result[''.join(sorted(list(i)))].append(i)
    return list(result.values())

print(solution(input))