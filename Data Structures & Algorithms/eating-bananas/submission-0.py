class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        result, l, r = math.inf, 1, max(piles)

        while l <= r:
            hours, k = 0, (l + r) // 2

            for pile in piles:
                hours += math.ceil(pile / k)

            if hours > h:
                l = k + 1
            else:
                result = min(result, k)
                r = k - 1

        return result