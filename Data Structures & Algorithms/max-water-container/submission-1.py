class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        max_volume, l, r = 0, 0, len(heights) - 1

        while l < r and l < len(heights) - 1 and r >= 0:
            max_volume = max(max_volume, (r - l) * min(heights[l], heights[r]))

            if heights[l] <= heights[r]:
                l += 1
            
            else:
                r -= 1

        return max_volume