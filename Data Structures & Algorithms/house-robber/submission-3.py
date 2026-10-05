class Solution:
    def rob(self, nums: List[int]) -> int:
        first, second = 0, 0
        for num in nums:
            current = max(first + num, second)
            first, second = second, current

        return second