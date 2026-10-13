from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:
        result, left, right = 0, 0, 0

        while right < len(nums) - 1:
            farthest = max(i + nums[i] for i in range(left, right + 1))
            left, right = right + 1, farthest

            result += 1

        return result