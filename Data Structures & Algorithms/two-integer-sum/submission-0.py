class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}

        for i, num in enumerate(nums):
            compliment = target - num

            if compliment in table:
                return [table[compliment], i]

            table[num] = i
        
        return [-1, -1]