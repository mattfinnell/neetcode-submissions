class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        result = nums[low]

        while low <= high:
            if nums[low] < nums[high]:
                return min(result, nums[low])

            mid = (low + high) // 2

            result = min(result, nums[mid])
            if nums[mid] >= nums[low]:
                low = mid + 1

            else: 
                high = mid - 1

        return result