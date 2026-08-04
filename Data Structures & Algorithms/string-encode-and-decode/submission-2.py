class Solution:
    simbol = "~"

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + self.simbol + s
        
        return res     

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != self.simbol:
                j += 1

            length = int(s[i : j])
            word = s[j + 1 : j + 1 + length]
            res.append(word)

            i = j + 1 + length
  
        return res
# 5#Hello5#World