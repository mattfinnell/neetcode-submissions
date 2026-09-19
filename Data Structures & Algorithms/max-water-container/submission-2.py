class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) < 2:
            return 0

        max_area, l, r = 0, 0, len(heights) - 1

        while l < r:
            max_area = max(
                (r - l) * min(heights[l], heights[r]),
                max_area
            )

            l, r = (l + 1, r) if heights[l] <= heights[r] else (l, r - 1)

        return max_area
