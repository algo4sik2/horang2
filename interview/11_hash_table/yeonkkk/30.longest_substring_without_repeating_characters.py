# input 
# s = "abcabcbb" # 3
# s = "bbbbb" # 1
s = "pwwkew" # 3

# 1. 나의 시도 -----------------------------------------------------------------------
def solution(s):
    answer = ""
    for i, char in enumerate(s):
        check_list = [char]

        for j in range(i+1, len(s)):
            if s[j] not in check_list: check_list.append(s[j])
            else:
                if len(answer) < len(check_list): answer = ''.join(check_list)
                check_list = []
                break

    return len(answer)

# 2. 책: 슬라이딩 윈도우와 투 포인터로 사이즈 조절 --------------------------------------
def solution(s):
    used = {}
    max_length = start = 0
    for index, char in enumerate(s):
        # 이미 등장했던 문자라면 'start' 위치 갱신
        if char in used and start <= used[char]:
            start = used[char] + 1
        else: # 최대 부분 문자열 길이 갱신
            max_length = max(max_length, index - start + 1)
            
        # 현재 문자의 위치 삽입
        used[char] = index 
        
    return max_length

print(solution(s))
                


