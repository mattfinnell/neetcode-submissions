class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, result = [], 0

        for j, height in enumerate(heights):
            left = j
            while stack and stack[-1][1] > height:
                i, prior_height = stack.pop()
                result = max(result, prior_height * (j - i))
                left = i

            stack.append((left, height))

        for i, height in stack:
            result = max(result, height * (len(heights) - i))

        return result

