class Solution:
    def addBinary(self, a: str, b: str) -> str:

        result = ""
        carry = 0

        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
            digit_a = int(a[i]) if i < len(a) else 0
            digit_b = int(b[i]) if i < len(b) else 0

            total = digit_a + digit_b + carry
            carry = total // 2
            result = str(total % 2) + result

        return result if not carry else "1" + result
