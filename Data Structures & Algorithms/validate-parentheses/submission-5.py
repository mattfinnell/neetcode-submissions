class Solution:
    def isValid(self, s: str) -> bool:
        stack, compliments = [], {
            '(': ')',
            '[': ']',
            '{': '}',
        }

        for c in s:
            if c in compliments.keys():
                stack.append(c)
            else:
                if stack and c == compliments[stack[-1]]:
                    stack.pop()
                else: 
                    return False

        return not stack