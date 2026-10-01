class Solution:
    def isHappy(self, n: int) -> bool:
        sum_of_squares = staticmethod(lambda x: sum(int(d) ** 2 for d in str(x)))

        slow, fast = n, sum_of_squares(n)

        while slow != fast:
            fast = sum_of_squares(fast)
            fast = sum_of_squares(fast)
            slow = sum_of_squares(slow)

        return fast == 1