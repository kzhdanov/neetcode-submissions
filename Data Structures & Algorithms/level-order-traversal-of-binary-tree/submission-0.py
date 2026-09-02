# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
            
        def bfs(items):
            acc = []
            nextLevel = []
            if items:
                for item in items:
                    if item:
                        acc.append(item.val)
                        if item.left:
                            nextLevel.append(item.left)
                        if item.right:
                            nextLevel.append(item.right)

                res.append(acc)
                bfs(nextLevel)

        bfs([root])

        return res        
