class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        digits.reverse()
        for i, digit in enumerate(digits):
            if digit < 9:
                digits[i] += 1
                digits.reverse()
                return digits
            else:
                digits[i] = 0

        digits.append(1)
        digits.reverse()
        return digits