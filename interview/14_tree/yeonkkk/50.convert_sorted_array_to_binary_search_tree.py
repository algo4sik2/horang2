# input 
nums = [-10, -3, 0, 5, 9]

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None 
        
        mid = len(nums) // 2
        
        # 분할 정복으로 이진 검색 결과 트리  구성
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        # print(node.val, end=' ')
        node.right = self.sortedArrayToBST(nums[mid+1:])
        

test = Solution()
test.sortedArrayToBST(nums)