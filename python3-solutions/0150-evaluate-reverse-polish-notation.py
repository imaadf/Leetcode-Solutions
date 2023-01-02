from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        value_stack = []

        for item in tokens:
            if item in ["*", "/", "+", "-"]:
                num1 = int(value_stack.pop())
                num2 = int(value_stack.pop())
                if item == "+":
                    value_stack.append(num2 + num1)
                if item == "-":
                    value_stack.append(num2 - num1)
                if item == "*":
                    value_stack.append(num2 * num1)
                if item == "/":
                    value_stack.append(int(num2 / num1))
            else:
                value_stack.append(item)

        return int(value_stack[0])
