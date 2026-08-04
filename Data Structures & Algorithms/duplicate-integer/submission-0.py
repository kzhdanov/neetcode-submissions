class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        already_have = {}

        for i in range(len(nums)):
            key = already_have.get(nums[i])
            if key: 
                return True
            else:
               already_have[nums[i]] = True

        return False       
        