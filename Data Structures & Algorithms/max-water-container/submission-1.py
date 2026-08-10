class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_s = 0

        l = 0
        r = len(heights) - 1

        while l < r:
            distance = r - l
            m_val = min(heights[l], heights[r]) * distance
            max_s = max(m_val, max_s)

            if heights[l] < heights[r]:
                l += 1
            else: 
                r -= 1

        return max_s         