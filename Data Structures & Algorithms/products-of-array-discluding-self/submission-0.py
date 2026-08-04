class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix = prefix * nums[i]

        # [1, 1, 2, 8]

        postfix = 1
        for i in range(len(output) - 1, -1, -1):
            output[i] = output[i] * postfix # 8 12 24 48
            postfix = postfix * nums[i] # 6 24 48 48
        
        # [48, 24, 12, 8]

        return output