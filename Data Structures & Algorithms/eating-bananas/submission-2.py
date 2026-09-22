import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        result = high

        while low <= high:
            k, total_time = (low + high) // 2, 0

            for pile in piles:
                total_time += math.ceil(float(pile) / k)

            if total_time <= h:
                result = k
                high = k - 1

            else:
                low = k + 1

        return low