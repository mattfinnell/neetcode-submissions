class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1

        a, b = 1, 1
        for _ in range(1, n):
            b, a = a + b, b

        return b