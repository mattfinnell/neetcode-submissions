class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}

        for j, n in enumerate(nums):
            compliment = target - n

            if compliment in table:
                return [table[compliment], j]

            table[n] = j

        return []