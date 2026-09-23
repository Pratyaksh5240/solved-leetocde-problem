class Solution(object):
    def decodeString(self, s):
        countStack = []
        stringStack = []

        currentString = ""
        currentNumber = 0

        for ch in s:

            if ch.isdigit():
                currentNumber = currentNumber * 10 + int(ch)

            elif ch == '[':
                countStack.append(currentNumber)
                stringStack.append(currentString)

                currentNumber = 0
                currentString = ""

            elif ch == ']':
                repeat = countStack.pop()
                previous = stringStack.pop()

                currentString = previous + currentString * repeat

            else:
                currentString += ch

        return currentString