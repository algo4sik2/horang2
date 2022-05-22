from collections import Counter 

# input
# tasks, n = ['A', 'A', 'A', 'B', 'B', 'B'], 2
tasks, n = ['A', 'A', 'A', 'B', 'C', 'D'], 2


# 우선순위 큐 이용
def solution(tasks, n):
    counter = Counter(tasks)
    result = 0 # 반환값 (최소 간격)
    
    while True:
        sub_count = 0 
        
        # 개수 순 추출
        for task, _ in counter.most_common(n+1):
            sub_count += 1
            result += 1
            
            counter.subtract(task)
            # 0 이하인 아이템을 목록에서 완전히 제거
            counter += Counter()
            
        if not counter:
            break
        
        result += n - sub_count + 1
    
    return result 
            
print(solution(tasks, n))