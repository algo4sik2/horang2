class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right
        
        
class Solution:
    # 1. 재귀 구조 DFS로 브루트 포스 검색
    def rangeSumBST(self, root, L, R):
        if not root:
            return 0
        
        return (root.val if L <= root.val <= R else 0) + \
                self.rangeSumBST(root.left, L, R) + \
                self.rangeSumBST(root.right, L, R)
    
    # 2. DFS 가지치기로 필요한 노드 탐색
    def rangeSumBST2(self, root, L, R):
        def dfs(node):
            if not node:
                return 0
            
            if node.val < L:
                return dfs(node.right)
            elif node.val > R:
                return dfs(node.left)
            return node.val + dfs(node.left) + dfs(node.right)
        
        return dfs(root)
    
    # 3. 반복 구조 DFS로 필요한 노드 탐색
    def rangeSumBST3(self, root, L, R):
        stack, sum = [root], 0
        # 스택 이용 필요한 노드 DFS 반복
        while stack:
            node = stack.pop()
            if node:
                if node.val > L:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
                if L < node.val <= R:
                    sum += node.val
        return sum 
    
    # 4. 반복 구조 BFS로 필요한 노드 탐색
    def rangeSumBST4(self, root, L, R):
        stack, sum = [root], 0
        # 큐 연산을 이용해 반복 구조 BFS로 필요한 노드 탐색  ---> ? stack인데?
        while stack:
            node = stack.pop(0)
            if node:
                if node.val > L:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
                if L <= node.val <= R:
                    sum += node.val 
        return sum