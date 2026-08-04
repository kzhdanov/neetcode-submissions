import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cash = {}

        for i in range(len(nums)):
            if cash.get(nums[i]) is not None:
                cash[nums[i]] += 1
            else:
                cash[nums[i]] = 1

        top_2 = [key for key, value in heapq.nlargest(k, cash.items(), key=lambda item: item[1])]

        return top_2

        