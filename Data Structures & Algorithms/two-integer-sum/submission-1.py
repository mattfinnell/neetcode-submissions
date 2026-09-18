class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}

        for j, num in enumerate(nums): 
            compliment = target - num

            if compliment in table:
                return [table[compliment], j]

            table[num] = j

        return Non