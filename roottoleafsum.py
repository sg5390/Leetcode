#My Solution : INORDER TRAVERSAL

class Pair:
    def __init__(self,node, val):
        self.node = node
        self.val = val

    def getkey(self):
        return self.node

    def getValue(self):
        return self.val


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root == None:
            return 0
        s = []
        res = 0
        currsum = 0
        while(root!= None) or s:
            while root!= None:
                currsum = currsum * 10 + root.val
                s.append(Pair(root,currsum))
                root=root.left
            p = s.pop()
            root = p.getkey()
            currsum = p.getValue()
            if(root.left == None and root.right == None):   #checking whether we have reached the leaf node
                res += currsum
            root = root.right
        return res



# INORDER RECURSION
class Solution:
    def sumNumbers(self, root):
        return self.helper(root, 0)

    def helper(self, root, s):
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return s * 10 + root.val
        return self.helper(root.left, s * 10 + root.val) + self.helper(root.right, s * 10 + root.val)
