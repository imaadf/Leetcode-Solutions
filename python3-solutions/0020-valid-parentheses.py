class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 == 1:
            return False

        bracket_to_compliment = {
            '(': ')',
            '{': '}',
            '[': ']',
        }

        stack = []

        for bracket in s:
            if bracket in bracket_to_compliment:
                stack.append(bracket)
            elif len(stack) == 0 or bracket_to_compliment[stack.pop()] != bracket:
                return False

        return len(stack) == 0
