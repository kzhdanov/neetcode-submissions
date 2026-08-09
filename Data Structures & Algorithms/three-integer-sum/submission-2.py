class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s_nums = sorted(nums)
        r = []

        for a, v in enumerate(s_nums):
            if a > 0 and s_nums[a - 1] == v: 
                continue

            head = a + 1
            tail = len(s_nums) - 1

            while head < tail:
                res = v + s_nums[head] + s_nums[tail] 

                if res > 0: 
                    tail -= 1
                elif res < 0:
                    head += 1
                else:
                    r.append([v, s_nums[head], s_nums[tail]])
                    head += 1

                    while head < tail and s_nums[head] == s_nums[head - 1]: 
                        head += 1
       
        return r
