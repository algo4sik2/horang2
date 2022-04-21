# 1. 파이썬다운 방식
import collections

def invertTree(self, root):
    if root:
        root.left, root.right = \
            self.inverTree(root.right), self.inverTree(root.left)
        return root 

# 2. 반복 구조로 BFS
def invertTree(self, root):
    queue = collections.deque([root])
    
    while queue:
        node = queue.popleft()
        # 부모 노드부터 하향식 스왑
        if node:
            node.left, node.right = node.right, node.left 
            
            queue.append(node.left)
            queue.append(node.right)
    return root 

# 3. 반복 구조로 DFS
def invertTree(self, root):
    stack = collections.deque([root])
    
    while stack:
        node = stack.pop()
        # 부모 노드 부터 하향식 스왑
        if node:
            node.left, node.right = node.right, node.left 
        
            stack.append(node.left)
            stack.append(node.right)
    return root 

# 4. 반복 구조로 DFS 후위 순회
def invertTree(self, root):
    stack = collections.deque([root])
    
    while stack:
        node = stack.pop()
        
        if node:
            stack.append(node.left)
            stack.append(node.right)
            
            node.left, node.right = node.right, node.left
            
    return root 


