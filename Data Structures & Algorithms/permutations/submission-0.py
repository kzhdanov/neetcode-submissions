class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # acc = []

        def dfs(acc):
            if len(acc) == len(nums):
                res.append(acc.copy())
                return

            for num in nums: 
                if num in acc:
                    continue

                acc.append(num)
                dfs(acc)
                acc.pop()    
            
        dfs([])

        return res

        