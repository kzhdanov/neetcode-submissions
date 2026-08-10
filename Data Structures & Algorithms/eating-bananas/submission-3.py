class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r: 
            m = (r + l) // 2
            hours_sum = 0

            for p in piles:
                hours_sum += math.ceil(p / m)

            if hours_sum <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1

        return res


