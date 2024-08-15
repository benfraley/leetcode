class Solution:
    def reverse(self, x: int) -> int:
        MIN_INT_32 = -2**31
        MAX_INT_32 = 2**31 - 1
        y = str(x)
        if y[0] == "-":
            val = int(y[1:][::-1]) * -1
            return val if  MIN_INT_32 < val < MAX_INT_32 else 0
        else:
            val = int(y[::-1])
            return val if  MIN_INT_32 < val < MAX_INT_32 else 0