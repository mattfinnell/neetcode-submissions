class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        
        if n == 1:
            return nums[0]

        first, second = nums[n - 1], 0
        for i in range(n - 2, -1, -1):
            current = max(first, second + nums[i])
            first, second = current, first

        return first
