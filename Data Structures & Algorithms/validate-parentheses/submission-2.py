class Solution:
    brackets = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in self.brackets:
                top = stack.pop() if stack else 0

                if top != self.brackets[char]:
                    return False
            else:
                stack.append(char)
    
        return not stack