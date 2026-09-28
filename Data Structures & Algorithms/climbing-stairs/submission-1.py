class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 0
        cur = 0
        while n > 0:
            if prev == 0:
                prev = 1
                cur = 1
            else:
                temp = cur;  
                cur = cur + prev
                prev = temp

            n -= 1

        return cur
