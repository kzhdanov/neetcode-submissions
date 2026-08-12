class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charSet = set()
        max_v = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])
            max_v = max(max_v, r - l + 1) 

        return max_v