class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        return self._rob(nums, 0, memo)

    def _rob(self, nums, i, memo):
        if i >= len(nums):
            return 0

        if i in memo:
            return memo[i]

        memo[i] = max(
            self._rob(nums, i + 1, memo),
            nums[i] + self._rob(nums, i + 2, memo)
        )

        return memo[i]