class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT = dict(collections.Counter(t))
        window = {}

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]: 
                have += 1

            while have == need:
                pointer = r - l + 1
                if pointer < resLen:
                    res = [l, r]
                    resLen = pointer

                window[s[l]] -= 1

                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                    
                l += 1

        return s[res[0]:res[1]+1] if resLen != float("infinity") else ""   


