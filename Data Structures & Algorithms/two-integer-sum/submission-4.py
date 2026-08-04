class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        tail = 0
        head = 0

        while head < len(nums):
            head += 1

            if head == len(nums): 
                tail += 1
                head = tail + 1

            if nums[tail] + nums[head] == target:
                return [tail, head]


