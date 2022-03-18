""" 
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자를 구분하지
않으며, 구두점 또한무시한다 """
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = {"hit"}

import re
from collections import Counter

paragraph = re.sub(r'[^\w]', ' ', paragraph)
words = [word for word in paragraph.lower().split() if not word in banned]

count = Counter(words)

print(count.most_common(1))

