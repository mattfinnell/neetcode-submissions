class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total, expected = sum(nums), int(((n * (n + 1)) / 2))

        return expected - total