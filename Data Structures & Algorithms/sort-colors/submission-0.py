class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter, j = Counter(nums), 0
        for i in range(3):
            for _ in range(counter[i]):
                nums[j] = i
                j += 1