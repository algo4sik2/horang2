from typing import List
from collections import defaultdict, Counter
          
# defaultdict
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        counter = defaultdict(int)
        paragraph = re.sub(r'[^\w]',' ',paragraph).lower()
        for p in paragraph.split():
            counter[p] += 1
        for b in banned:
            if b in counter.keys():
                del counter[b]
        return max(counter, key=counter.get)
    
# counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        lst = []
        paragraph = re.sub(r'[^\w]',' ',paragraph).lower()
        counter = Counter(paragraph.split())
        for b in banned:
            if b in counter.keys():
                del counter[b]
        return counter.most_common(1)[0][0]
                
# counter + list comprehension
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'[^\w]',' ',paragraph).lower()
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
        counter = Counter(words)
        return counter.most_common(1)[0][0]