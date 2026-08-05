class Solution:
    brackets = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)): 
            val = s[i]
            top = stack[-1] if stack else 0
            print(i, top, val, self.brackets.get(val))
            if top != self.brackets.get(val):
                stack.append(val)  
            elif stack:
                stack.pop()
  
        return not stack
         
        