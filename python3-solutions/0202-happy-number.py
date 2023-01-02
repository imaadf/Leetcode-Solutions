class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n

        while True:
            slow = self.sum_square_digits(slow)
            fast = self.sum_square_digits(fast)
            fast = self.sum_square_digits(fast)
            if fast == 1 or slow == 1:
                return True
            elif fast == slow:
                return False

    def sum_square_digits(self, n: int) -> int:
        res = 0

        while n:
            digit = n % 10
            res += digit ** 2
            n = n // 10

        return res
