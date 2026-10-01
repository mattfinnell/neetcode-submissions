class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits 

        i, result, carry = len(digits), [0, *digits], 1
        while result[i] == 9:
            result[i] = 0
            i -= 1

        result[i] += 1

        return result if result[0] == 1 else result[1:]
