class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_l = 0
        valSet = {}
        l = 0

        for r in range(len(s)):
            valSet[s[r]] = valSet.get(s[r], 0) + 1

            if (r - l + 1) - max(valSet.values()) > k:
                valSet[s[l]] = valSet[s[l]] - 1
                l += 1

            max_l = max(max_l, r - l + 1)

        return max_l
            
