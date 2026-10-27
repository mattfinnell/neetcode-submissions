class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []

        self._combination_sum(nums, target, 0, results, [])

        return results

    def _combination_sum(self, nums, target, i, results, visited: Set[int]):
        if target == 0:
            results.append([nums[j] for j in visited])
            return

        if i >= len(nums) or target < 0:
            return

        visited.append(i)
        self._combination_sum(nums, target - nums[i], i, results, visited)
        visited.pop()
        self._combination_sum(nums, target, i + 1, results, visited)