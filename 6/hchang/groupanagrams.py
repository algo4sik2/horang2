input_= ['eat','tea','tan','ate','nat','bat']
from collections import defaultdict
anagram_dict = defaultdict(list)

for i in input_:
    word = ''.join(sorted(list(i)))
    anagram_dict[word].append(i)

print(anagram_dict)

