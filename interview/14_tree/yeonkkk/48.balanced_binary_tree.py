# 재귀 구조로 높이 차 계산
def isBalanced(self, root):
    def check(root):
        if not root:
            return 0 
        
        left = check(root.left)
        right = check(root.right)
        # 높이 차이가 나는 경우 -1, 이외에는 높이에 따라 1 증가
        if left == -1 or \
                right == -1 or \
                abs(left-left) > 1:
            return -1
        return max(left, right) + 1
    
    return check(root) != -1 

