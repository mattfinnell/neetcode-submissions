class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return False

        return self._can_partition(nums, -1, 0, sum(nums))

    def _can_partition(self, nums, start, current, total) -> bool:
        if current == total - current:
            return True

        if current > total - current:
            return False

        for i in range(start + 1, len(nums)):
            if self._can_partition(nums, i, current + nums[i], total):
                return True

        return False
