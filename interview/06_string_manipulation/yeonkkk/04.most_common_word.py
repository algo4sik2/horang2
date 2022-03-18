# input
par = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

# 내 코드
def solution(par, banned):
    from collections import Counter
    import re
    par = re.sub(r'[^a-z0-9]', ' ', par.lower())
    result = Counter(par.split()).most_common()
    for r in result:
        if r[0] not in banned: return r[0]
    

# 책 코드
def solution(par, banned):
    from collections import Counter
    import re
    words = [word for word in re.sub(r'[^\w]', ' ', par).lower().split() if word not in banned]
    counts = Counter(words)
    return counts.most_common(1)[0][0]

print(solution(par, banned))
