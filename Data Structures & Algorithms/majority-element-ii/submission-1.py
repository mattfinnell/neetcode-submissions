import math

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) < 3:
            return nums

        a = b = -1
        a_count = b_count = 0

        for num in nums[0:]:
            if num == a:
                a_count += 1

            elif num == b:
                b_count += 1

            elif not a_count:
                a, a_count = num, 1

            elif not b_count:
                b, b_count = num, 1

            else:
                a_count -= 1
                b_count -= 1

        count_a = count_b = 0
        for num in nums:
            if num == a:
                count_a += 1
            elif num == b:
                count_b += 1

        result, n = [], len(nums)
        if count_a > n // 3:
            result.append(a)

        if count_b > n // 3:
            result.append(b)

        return result