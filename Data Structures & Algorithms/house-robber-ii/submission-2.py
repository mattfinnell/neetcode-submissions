class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(
            nums[0],
            self._rob(nums[1:]), 
            self._rob(nums[:-1])
        )

    def _rob(self, nums):
        first, second = 0, 0
        for num in nums:
            current = max(first + num, second)
            first, second = second, current

        return second