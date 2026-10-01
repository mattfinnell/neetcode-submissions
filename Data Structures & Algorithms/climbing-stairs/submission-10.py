class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5, n = math.sqrt(5), n + 1
        phi, psi = (1 + sqrt5) / 2, (1 - sqrt5) / 2

        return round((phi**n - psi**n) / sqrt5)