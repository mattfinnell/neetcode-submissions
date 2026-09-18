class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j, max_area = 0, len(heights) - 1, 0

        while i < j:
            max_area = max(max_area, (j - i) * min(heights[i], heights[j]))

            if heights[i] <= heights[j]:
                i += 1

            else:
                j -= 1

        return max_area