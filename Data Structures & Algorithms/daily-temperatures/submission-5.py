class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = [] # [temp, index]

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                s_temp, s_index = stack.pop()
                output[s_index] = i - s_index
            stack.append([temp, i])

        return output