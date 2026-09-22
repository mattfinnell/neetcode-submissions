class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[low] <= nums[high]:
                return nums[low]

            elif nums[low] <= nums[mid]:
                low = mid + 1

            else:
                high = mid

        return nums[low]