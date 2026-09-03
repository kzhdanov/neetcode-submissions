class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        acc = []

        def dfs(i):
            print(i)
            if i > len(nums) - 1:
                print(acc.copy())
                if acc not in res:
                    res.append(acc.copy())

                return

            acc.append(nums[i])
            dfs(i + 1)

            acc.pop()
            dfs(i + 1)

        dfs(0)

        return res            
