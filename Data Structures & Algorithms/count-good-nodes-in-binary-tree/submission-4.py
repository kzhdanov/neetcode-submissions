# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def isGood(node, prevMaxVal) -> int:
            if not node:
                return 0

            good = 1 if node.val >= prevMaxVal else 0

            maxVal = max(node.val, prevMaxVal)

            rightVal = isGood(node.right, maxVal)
            leftVal = isGood(node.left, maxVal)
    

            return good + leftVal + rightVal

        

        return isGood(root, root.val)    
