class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:

            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
                continue

            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)

            elif token == "-":
                stack.append(a - b)

            elif token == "*":
                stack.append(a * b)

            else:
                value = abs(a) // abs(b)

                if (a < 0) != (b < 0):
                    value = -value

                stack.append(value)

        return stack[-1]