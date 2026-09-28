class Solution:
    def climbStairs(self, n: int) -> int:
        i = n;
        prev = 0
        cur = 0
        while i > 0:
            if prev == 0:
                prev = 1
                cur = 1
            else:
                temp = cur;  
                cur = cur + prev
                prev = temp

            i -= 1

        return cur
