class Solution:
    def isValid(self, s: str) -> bool:
        stack, pairs = [], {
            '(':')',
            '[':']',
            '{':'}'
        }

        for c in s:
            if c in pairs.keys():
                stack.append(c)

            if c in pairs.values():
                if not stack or pairs[stack[-1]] != c:
                    return False
                
                stack.pop()
        
        return not stack