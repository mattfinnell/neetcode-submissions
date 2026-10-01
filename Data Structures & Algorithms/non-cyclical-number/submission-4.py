def sum_of_squares(n):
    result = 0
    while n > 0:
        n, d = divmod(n, 10)
        result += d ** 2

    return result

class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, sum_of_squares(n)

        while slow != fast:
            fast = sum_of_squares(sum_of_squares(fast))
            slow = sum_of_squares(slow)

        return fast == 1
