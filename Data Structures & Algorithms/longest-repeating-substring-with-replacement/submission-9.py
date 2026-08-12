class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_l = 0
        counter = {}
        l = 0

        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r], 0) + 1
            diff = (r - l + 1) - max(counter.values())

            if diff > k:
                counter[s[l]] = counter[s[l]] - 1
                l += 1

            max_l = max(max_l, r - l + 1)

        return max_l
            
