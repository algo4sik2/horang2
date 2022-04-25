class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right

root = TreeNode('F',
            TreeNode('B',
            TreeNode('A'),
            TreeNode('D',
                 TreeNode('C'), TreeNode('E'))
            ),
        TreeNode('G',
             None,
             TreeNode('I', TreeNode('H'))
             )
        )

# 전위 순회(pree-order, NLR)
def preorder(node):
    if node is None:
        return
    print(node.val, end=' ')
    preorder(node.left)
    preorder(node.right)

print('preorder:', end=' ')
preorder(root)
print()

# 중위 순회(in-order, LNR)
def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.val, end=' ')
    inorder(node.right)

print('inorder:', end=' ')
inorder(root)
print()

# 후위 순회(post-order, LRN)
def postorder(node):
    if node is None:
        return 
    postorder(node.left)
    postorder(node.right)
    print(node.val, end=' ')
    
print('postorder:', end=' ')
postorder(root)