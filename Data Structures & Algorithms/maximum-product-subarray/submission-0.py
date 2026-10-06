class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result, current_min, current_max = nums[0], 1, 1

        for num in nums:
            secondary_max = current_max * num
            current_max = max(secondary_max, current_min * num, num)
            current_min = min(secondary_max, current_min * num, num)

            result = max(result, current_max)

        return result