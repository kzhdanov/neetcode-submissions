class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = [] # [temp, index]

        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][0]:
                temp, index = stack.pop()
                output[index] = i - index
            stack.append([v, i])    

        return output        