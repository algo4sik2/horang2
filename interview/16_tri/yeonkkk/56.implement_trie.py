# insert, search, startsWith 메소드 구현
# 딕셔너리를 이용해 간결한 트라이 구현
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    # 단어 삽입
    def insert(self, word):
        node = self.root 
        for char in word:
            node = node.children[char]
        node.word = True 
    
    # 단어 존재 여부 판별
    def search(self, word):
        node = self.root 
        for char in word:
            if char not in node.children:
                return False 
            node = node.children[char]

        return node.word 
    
    # 문자열로 시작 단어 존재 여부 판별
    def startsWith(self, prefix):
        node = self.root 
        for char in prefix:
            if char not in node.children:
                return False 
            node = node.children[char]
            
        return True 

trie = Trie()
trie.insert("apple")
trie.search("apple") # True
trie.search("app") # False 
trie.startsWith("app") # True 
trie.insert("app") 
trie.search("app") # True