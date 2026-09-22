class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result, n = [], len(nums)
        nums.sort()

        for i, a in enumerate(nums[:n - 2]):
            # if a > 0:
            #     break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, n - 1

            while l < r:
                value = a + nums[l] + nums[r]

                if value > 0:
                    r -= 1

                elif value < 0:
                    l += 1

                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return result