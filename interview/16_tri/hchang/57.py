from pprint import pprint
# words = ['d','cbbcd','dcbb','dcbc','cbbc','bbcd']
words = ['abcd','dcba','lls','s','sssll','']

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
        if (imchar:=word[len(word)-1-i]) not in imnode:
            imnode[imchar]=hi()
        node = node[char]
        imnode = imnode[imchar]
    node['end']=True
    node['index']=index
    imnode['end']=True
    imnode['index']=index

answerindex = set()

# 문자를 거꾸로 돌려서 다 넣고 남은 부분이 펠린드롬인 것을 찾는다.
for i, word in enumerate(words):
    node = trie
    imnode = imtrie
    remain = ''
    imremain = ''
    for j, char in enumerate(imword:=word[::-1]):
        remain = imword[j+1:]
        if char in node:
            node = node[char]
            if node['end'] and remain==remain[::-1] and node['index']!=i:
                answerindex.add((node['index'],i))
        else:
            break
    # 거꾸로 넣는 문자에 남은게 없으면 노드의 남은 부분을 살핀다. 
    # if not remain: 를 아래와 같이 변형한다. imnode 추가

    for j, char in enumerate(word):
        imremain = word[j+1:]
        if char in imnode:
            imnode = imnode[char]
            if imnode['end'] and imremain==imremain[::-1] and i != imnode['index']:
                answerindex.add((i,imnode['index']))
        else: 
            break
    # 문제에서 어이없게 빈 문자열을 줘서 예외처리를 해야한다. 하...
    if word=='':
        for j, word in enumerate(words):
            if word==word[::-1] and i!=j:
                answerindex.add((i,j))
                answerindex.add((j,i))




pprint(trie)
print('\n\n')
pprint(imtrie)
print(answerindex)