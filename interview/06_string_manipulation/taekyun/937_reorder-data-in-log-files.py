'''
split 미리 해놓는 것 보다, if문으로 split()[1]만 빼는게 빠름
28ms, 36ms > 63ms, 79ms
'''

from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        for l in logs:
            if l.split()[1].isdigit():
                digits.append(l)
            else:
                letters.append(l)
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits
        