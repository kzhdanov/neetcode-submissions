class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, c, t):
            if t == target:
                res.append(c.copy())
                return
            
            if i >= len(nums) or t > target:
                return

            val = nums[i]

            c.append(val)
            dfs(i, c, t + val)
            
            c.pop()
            dfs(i + 1, c, t)

        dfs(0, [], 0)

        return res        