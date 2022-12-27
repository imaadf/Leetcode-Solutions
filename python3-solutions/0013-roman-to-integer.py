class Solution:
    def romanToInt(self, s: str) -> int:

        numeral_to_value = {'I': 1, 'V': 5, 'X': 10,
                            'L': 50, 'C': 100, 'D': 500,
                            'M': 1000,
                            }

        total = 0
        prev_value = 0

        for numeral in s:
            current_value = numeral_to_value[numeral]

            if current_value > prev_value:
                total -= prev_value * 2

            total += current_value
            prev_value = current_value

        return total
