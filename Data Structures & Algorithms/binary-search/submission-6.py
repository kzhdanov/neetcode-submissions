class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            center = l + ((r - l) // 2)

            if nums[center] == target:
                return center
            elif nums[center] < target:
                l = center + 1
            else:
                r = center - 1

        return -1