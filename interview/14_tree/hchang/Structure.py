from collections import deque
class TreeNode:
    def __init__(self,data=None,left=None,right=None):
        self.left = left
        self.right = right
        if type(data)==list:
            self.val = data[0]
            nextnode = deque([self.add_left, self.add_right])
            for i in data[1:]:
                addnode = nextnode.popleft()
                if i is not None:node = addnode(i)
                nextnode.extend([node.add_left, node.add_right])
        else: self.val = data

    def to_list(self):
        result = [self.val]
        q = deque([self.left,self.right])
        while q:
            node = q.popleft()
            if node:
                result.append(node.val)
                q.extend([node.left,node.right])
            else: result.append(None)
        while result[-1] is None:
            result.pop()
        return result

    def add_left(self,data):
        self.left = TreeNode(data)
        return self.left

    def add_right(self,data):
        self.right = TreeNode(data)
        return self.right

    def print_all(self,num=30):
        count = 0
        nodelist = self.to_list()
        while 2**count < len(nodelist)+1:
            if count:
                for i in nodelist[2**count-1:2**(count+1)-1]:
                    print(' '*(num//(2**count+1)-len(str(i))),i, end='')
                print()
            else: print(' '*(num//2),nodelist[0])
            count+=1
