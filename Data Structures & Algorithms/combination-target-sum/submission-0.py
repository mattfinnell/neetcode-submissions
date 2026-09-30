class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []

        self.dfs(nums, target, 0, [], 0, result)

        return result

    def dfs(self, nums, target, i, current, total, result):
        if total == target:
            result.append(current.copy())
            return

        for j in range(i, len(nums)):
            if total + nums[j] > target:
                return

            current.append(nums[j])
            self.dfs(nums, target, j, current, total + nums[j], result)
            current.pop()
