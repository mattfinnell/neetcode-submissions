class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                low = mid + 1

            else:
                high = mid

        pivot = low

        def binary_search(l, r) -> int:
            while l <= r:
                m = (l + r) // 2

                if nums[m] == target:
                    return m

                elif nums[m] < target:
                    l = m + 1

                else:
                    r = m - 1

            return -1

        result = binary_search(0, pivot - 1)

        return result if result != -1 else binary_search(pivot, len(nums) - 1)