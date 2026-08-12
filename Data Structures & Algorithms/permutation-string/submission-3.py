from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_object = dict(Counter(s1))
        s2_object = {}

        window_len = len(s1)
        l = 0

        for r in range(len(s2)):
            s2_object[s2[r]] = s2_object.get(s2[r], 0) + 1
            diff = r - l + 1

            if diff > window_len:
                s2_object[s2[l]] -= 1
                if s2_object[s2[l]] == 0:
                    del s2_object[s2[l]]
                l += 1

            if s1_object == s2_object:
                return True    

        return False


        