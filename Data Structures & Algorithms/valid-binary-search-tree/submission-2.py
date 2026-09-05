# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isVal(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True

            if not (low < node.val < high):
                return False

            left = isVal(node.left, low, node.val)
            right = isVal(node.right, node.val, high)

            return left and right

        return isVal(root)
        