""" 
1. 로그의 가장앞부분은식별자다.
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3. 식별자는순서에 영향을끼치지 않지만.문자가동일할경우식별자순으로한다.
4. 숫자로그는입력 순서대로한다 . 
"""
logs = [ "dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

dig = []
let = []
for i in logs:
    if i[0]=="d":dig.append(i)
    else: let.append(i)
dig.sort(key=lambda x: x[4:]+x[3])
let.sort(key=lambda x: x[4:]+x[3])

print(let+dig)