from pprint import pprint
words = ['d','cbbcd','dcbb','dcbc','cbbc','bbcd']

def hi():
    dedic = {'end':False}
    return dedic

trie = hi()
imtrie = hi()
# 일단 다 집어 넣는다.
for index, word in enumerate(words):
    node = trie
    imnode = imtrie
    for i, char in enumerate(word):
        if char not in node:
            node[char]=hi()
        if imchar:=word[len(word)-1-i] not in imnode:
            imnode[imchar]=hi()
        node = node[char]
        imnode = imnode[imchar]
    node['end']=True
    node['index']=index
    imnode['end']=True
    imnode['index']=index

answerindex = []

# 문자를 거꾸로 돌려서 다 넣고 남은 부분이 펠린드롬인 것을 찾는다.
for i, word in enumerate(words):
    node = trie
    imnode = imtrie
    remain = ''
    imremain = ''
    for j, char in enumerate(imword:=word[::-1]):
        if char in node:
            node = node[char]
        else:
            remain = imword[j:]
            if node['end'] and remain==remain[::-1]:
                answerindex.append[(node['index'],i)]
            break
    #거꾸로 넣는 문자에 남은게 없으면 노드의 남은 부분을 살핀다. 
    # if not remain: 를 아래와 같이 변형한다. imnode 추가
    for j, char in enumerate(word):
        if char in imnode:
            imnode = imnode[char]
        else:
            imremain = word[j:]
            if imnode['end'] and imremain==imremain[::-1]:
                answerindex.append[(i,imnode['index'])]
            break



pprint(trie)
print(answerindex)