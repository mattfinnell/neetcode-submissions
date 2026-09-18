class Solution:
    def isValid(self, s: str) -> bool:
        compliments, stack = {
            '(': ')',
            '[': ']',
            '{': '}'
        }, []

        for character in s:
            if character in compliments.keys():
                stack.append(character)
            elif character in compliments.values():
                if stack and compliments[stack[-1]] == character:
                    stack.pop()
                else:
                    return False

        return not stack