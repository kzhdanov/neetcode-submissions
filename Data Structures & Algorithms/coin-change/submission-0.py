class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [float('inf')] * (amount + 1)
        arr[0] = 0

        for i in range(1, amount + 1):
            for coin in coins: 
                if i - coin >= 0:
                    curr = i - coin
 
                    arr[i] = min(arr[i], arr[curr] + 1)

        if arr[amount] != float('inf'):
            return arr[amount]

        return -1    

        