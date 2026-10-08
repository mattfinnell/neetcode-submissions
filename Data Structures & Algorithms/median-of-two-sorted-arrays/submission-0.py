class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        small, large, n = nums1, nums2, len(nums1) + len(nums2)
        half = n // 2

        if len(large) < len(small):
            small, large = large, small

        left, right = 0, len(small) - 1
        while True:
            i = (left + right) // 2
            j = half - i - 2

            small_left, small_right =  (
                small[i] if i >= 0 else -float("inf"),
                small[i + 1] if (i + 1) < len(small) else float("inf"),
            )

            large_left, large_right =  (
                large[j] if j >= 0 else -float("inf"),
                large[j + 1] if (j + 1) < len(large) else float("inf"),
            )

            if small_left <= large_right and large_left <= small_right:
                if n % 2:
                    return min(small_right, large_right)

                return (max(small_left, large_left) + min(small_right, large_right)) / 2

            elif small_left > large_right:
                right = i - 1

            else:
                left = i + 1


