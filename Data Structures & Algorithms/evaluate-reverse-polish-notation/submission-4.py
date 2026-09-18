class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))

            else:
                a = stack.pop()
                b = stack.pop()

                if token == "+":
                    stack.append(a + b)

                elif token == "-":
                    stack.append(b - a)

                elif token == "/":
                    stack.append(int(float(b) / a))

                elif token == "*":
                    stack.append(a * b)

        return stack[-1]