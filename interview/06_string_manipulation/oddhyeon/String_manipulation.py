

# #--- 1번 문제 ---
# import re
#
# char = "A man, a plan, a canal: Panama"
# clist = ["h","e","l","l","o"]
#
# def ispalinremix(s): # 내 코드
#     strs = []
#
#     for char in s:
#         if char.isalnum():
#             strs.append(char.lower())
#
#     strs.reverse()
#     areverse = [i for i in strs]
#
#     if strs == areverse:
#         return True
#     return False
#
# def exispal1(s): # 책 코드
#     s = s.lower()
#     s = re.sub('[^a-z0-9]','',s)
#     return s==s[::-1]
#
# print(ispalinremix(char))


# #--- 2번 문제 ---
#
# def reverseString1(s): # 책 코드
#     left, right = 0,len(s)-1
#     while left < right:
#         s[left],s[right] = s[right],s[left]
#         left += 1
#         right -= 1
#     return s
#
# def reverseString2(s): # 내 코드
#     s.reverse()
#     return s
#
# print(reverseString1(clist))
#
# import collections
# import re


#--- 3번 문제 ---
# log = [ "digl 8 1 5 1" , "letl art can" , "dig2 3 6" , "let2 own kit dig" , "let3 art zero" ]
#
#
# def rLog(logs):
#     letters, digits = [] , []
#     for log in logs:
#         if log.split()[1].isdigit(): # 숫자인경우 False, 문자만 True
#             digits.append(log)
#         else:
#             letters.append(log)
#
#     letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
#     return letters + digits
#
# print(rLog(log))


#--- 4번 문제 ---
# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
# banned = ['hit']
# def countword(paragraph,banned):
#     words = [word for word in re.sub(r'[^\w]', ' ', paragraph) #
#         .lower().split()  # 소문자 변환 및 단어 별 저장
#              if word not in banned] # banned 단어 제외
#
#     counts = collections.Counter(words) # 단어별 빈도 계산
#     print(counts)
#     return counts.most_common(1)[0][0] # most_common(1) 만 하게 될 경우 [('ball', 2)]로 출력
#
#
# def countword1(paragraph,banned):
#     words = [word for word in re.sub(r'[^\w]', ' ', paragraph) #
#         .lower().split()  # 소문자 변환 및 단어 별 저장
#              if word not in banned] # banned 단어 제외
#
#     counts = collections.defaultdict(int)
#     for word in words:
#         counts[word] += 1
#     return max(counts, key=counts.get)
#
# print(countword(paragraph,banned))
# print(countword1(paragraph,banned))


# --- 5번 문제 ---
# a = [ "eat" , "tea" , "tan" , "ate" , "nat" , "bat" ]

# def ganagrams(strss):
#     anagrams = collections.defaultdict(list)
#
#     for word in strss:
#         anagrams = [''.join(sorted(word))].append(word)
#     return list(anagrams.values())
#
# print(ganagrams(a))


# def groupAnagrams(strs):
#     anagrams = collections.defaultdict(list)
#
#     for word in strs:
#         # 정렬하여 딕셔너리에 추가
#         anagrams[''.join(sorted(word))].append(word)
#     return list(anagrams.values())
#
# print(groupAnagrams(a))


# --- 6번 문제 ---
#
# a1 = "babed"
# a2 = "cbbd"
# def longestPalindrome(s):
#     def expand(left,right):
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             left -= 1
#             right += 1
#         return s[left+1:right]
#
#
#     if len(s) < 2 or s == s[::-1]:
#         return s
#
#     result = ''
#
#     for i in range(len(s) - 1):
#         result = max(result,
#                      expand(i, i + 1),
#                      expand(i, i + 2),
#                      key=len)
#     return result
#
# print(longestPalindrome(a1))
# print(longestPalindrome(a2))
