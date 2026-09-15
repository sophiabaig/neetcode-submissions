# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root is None:
            return False
        
        check = self.isSameTree(root, subRoot)
        
        if check:
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)



    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and q is None: # reached leaf node
            return True
        elif p is None or q is None: # one side none, other has val
            return False
        elif p.val == q.val: # vals equal, need to keep checking
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False # vals not equal, immediately return false
        