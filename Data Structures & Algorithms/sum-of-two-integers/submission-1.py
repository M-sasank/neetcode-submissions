class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        while b !=0:
            x = (a ^ b) & MASK
            y = ((a & b) << 1) & MASK
            a,b = x,y
        return ~(a ^ MASK) if a > 0x7FFFFFFF else a
