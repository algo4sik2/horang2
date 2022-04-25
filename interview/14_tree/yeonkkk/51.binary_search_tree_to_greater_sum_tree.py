class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right


# 중위 순회로 노드 값 누적
class Solution:
    val = 0
    
    def bstToGst(self, root):
        # 중위 순회 노드 값 누적
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)
            
        return root 
    