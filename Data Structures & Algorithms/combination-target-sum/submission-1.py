class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        self.acc = []
        self.accSum = 0

        def dfs(i):
            if self.accSum == target:
                res.append(self.acc.copy())
                return
            
            if i >= len(nums) or self.accSum > target:
                return

            val = nums[i]

            # 1. Ветка: Берем текущее число nums[i]
            self.accSum += val
            self.acc.append(val)
            dfs(i)  # Остаемся на i, так как элементы можно использовать повторно
            
            # Откат изменений (Backtrack) для ветки 1
            self.acc.pop()
            self.accSum -= val
            dfs(i + 1)

        dfs(0)

        return res        