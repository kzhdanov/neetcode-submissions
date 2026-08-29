# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False
        if self.isTheSame(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isTheSame(self, node, subNode):
        if not node and not subNode:
            return True

        if node and subNode and node.val == subNode.val: 
            return self.isTheSame(node.left, subNode.left) and self.isTheSame(node.right, subNode.right)
        
        return False 

  

         



    
