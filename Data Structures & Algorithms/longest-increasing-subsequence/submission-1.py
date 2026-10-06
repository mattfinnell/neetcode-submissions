class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self._dfs(nums, 0, -1, {})

    def _dfs(self, nums: List[int], i, j, memo) -> int:
        if i == len(nums):
            return 0

        if (i, j) in memo:
            return memo[(i, j)]

        result = self._dfs(nums, i + 1, j, memo)

        if j == -1 or nums[j] < nums[i]:
            result = max(
                result, 
                self._dfs(nums, i + 1, i, memo) + 1
            )

        memo[(i, j)] = result
        return result

