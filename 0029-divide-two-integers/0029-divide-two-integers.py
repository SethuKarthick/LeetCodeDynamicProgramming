class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        val = int(str(dividend/divisor).split(".")[0])

        if val == 2**31:
            return 2147483647
        return val