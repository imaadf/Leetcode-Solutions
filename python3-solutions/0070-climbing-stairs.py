class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev1, prev2 = 1, 0

        for _ in range(n):
            prev1, prev2 = prev1 + prev2, prev1

        return prev1
