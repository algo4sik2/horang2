# input
logs = ['dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero']

# 내 코드
def solution(input):
    let, dig = [], []
    for log in logs:
        if log[:3] == 'dig': dig.append(log)
        else: let.append(log)
    let.sort(key=lambda x: (x.split()[1], x.split()[0]))
    return let + dig


def solution(logs): 
    letters , digits = [], [] 
    for log in logs: 
        if log.split()[1].isdigit(): 
            digits.append(log) 
        else: 
            letters.append(log) 
    # 2개의 키를 람다 표현식으로 정렬 
    letters.sort(key=lambda x:(x.split()[1:], x.split()[0])) 
    return letters + digits

print(solution(logs))