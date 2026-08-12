class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        obj = {}
        max_v = 0

        for r in range(len(s)):
            char = s[r]

            if char in obj and obj[char] >= l:
                l = obj[char] + 1

            obj[char] = r
            max_v = max(max_v, r - l + 1)
           
        return max_v