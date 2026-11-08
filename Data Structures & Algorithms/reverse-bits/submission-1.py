class Solution:
    def reverseBits(self, n: int) -> int:
        print(format(n,'032b'))
        x = 0
        for i in range(32):
            x += ((n>>i) & 1) << 31-i
        return x