class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(start, acc, summ):
            if summ == target:
                res.append(acc.copy())
                return

            for j in range(start, len(candidates)):
                if summ + candidates[j] > target:
                    break;

                if j > start and candidates[j] == candidates[j - 1]:
                    continue

                acc.append(candidates[j])
                dfs(j + 1, acc, candidates[j] + summ)
                acc.pop()    
            
        dfs(0, [], 0)

        return res     