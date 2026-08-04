class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        resMap = {}

        for char in s:
            resMap[char] = resMap.get(char, 0) + 1

        for char in t:
            if char not in resMap:
                return False 
            
            resMap[char] -= 1
            if resMap[char] == 0:
                del resMap[char]

        return not resMap
            