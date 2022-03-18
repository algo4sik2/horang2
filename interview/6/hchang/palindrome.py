# 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

input_list = ['A man, a plan, a canal: Panama', 'race a car']

import re


def solution(text: str) -> bool:
    text = text.lower()
    text = re.sub(r'[^0-9a-z]', '',text)
    return text==text[::-1]

for i in range(len(input_list)):
    print(f'{i+1}번 정답: ',end='')
    print(solution(input_list[i]))