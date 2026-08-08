class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        head = 0
        tail = len(numbers) - 1

        while head <= tail:
            val1 = numbers[head]
            val2 = numbers[tail]
            sum_both = val1 + val2
  
            if sum_both == target: 
                return [head + 1, tail + 1]
            elif sum_both > target: 
                tail -= 1
            else:
                head += 1

