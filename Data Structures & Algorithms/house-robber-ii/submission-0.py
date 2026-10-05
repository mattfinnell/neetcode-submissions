class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo = {}
        return max(
            self._rob(nums, 0, True, memo), 
            self._rob(nums, 1, False, memo)
        )

    def _rob(self, nums, i, flag, memo):
        if (i, flag) in memo:
            return memo[(i, flag)]

        if i >= len(nums) or (flag and i == len(nums) - 1):
            return 0

        result = max(
            self._rob(nums, i + 1, flag, memo),
            self._rob(nums, i + 2, flag or i == 0, memo) + nums[i]
        )
        memo[(i, flag)] = result
        return memo[(i, flag)]