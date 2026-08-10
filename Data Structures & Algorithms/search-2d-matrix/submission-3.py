class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i, v in enumerate(matrix):
            if v[-1] < target:
                continue

            l = 0
            r = len(v) - 1

            while l <= r:
                m = l + ((r - l) // 2)

                if v[m] == target:
                    return True
                elif v[m] < target:
                    l = m + 1
                else:
                    r = m - 1

        return False            