# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n): No of total nodes | O(h) : h - height of the tree
#USING STACKS
class Solution:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isValidBST(self,root):
        stack = []
        prev = None
        # root = self
        while root != None or stack:
            while root != None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev != None and prev.val >= root.val:
                return False
            print(root.val)
            prev = root
            root = root.right
        return True

# O(n) | O(h) : h - height of the tree
#Recursive Traversal with Valid Range

# def isValidBST(self, root):
#     def valid(root,min,max):
#         if root == None:
#             return True
#         if min != None and min.val >= root.val:
#             return False
#         if max != None and max.val <= root.val:
#             return False
#         return valid(root.left,min,max) and valid(root.right,root,max)


#     return valid(root,None,None)  

    

root1 = [5,1,4,None,None,3,6]
sol = Solution()
print(sol.isValidBST(root1))
