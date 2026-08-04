class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        resMap = {}

        if len(s) != len(t):
            return False 

        for i in range(len(s)):
            val = resMap.get(s[i])

            if val is not None:
                resMap[s[i]] = resMap[s[i]] + 1
            else:
                resMap[s[i]] = 1

        for j in range(len(t)):
            val = resMap.get(t[j])

            if val is not None:
                if resMap[t[j]] == 0:
                    del resMap[t[j]]
                else:
                    resMap[t[j]] -= 1

                    if resMap[t[j]] == 0:
                        del resMap[t[j]]

        if not resMap:    
            return True
        else:
            return False    
            