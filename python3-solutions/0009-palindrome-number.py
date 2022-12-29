class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        scaler = 1

        while x // scaler >= 10:
            scaler *= 10

        if scaler == 1:
            return True

        while x:
            first_digit = x // scaler
            last_digit = x % 10

            if first_digit != last_digit:
                return False

            x -= (first_digit * scaler)
            x //= 10
            scaler //= 100

            if scaler <= 1:
                return True

        return True
