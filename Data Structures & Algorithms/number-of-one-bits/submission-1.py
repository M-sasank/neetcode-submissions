class Solution:
    def hammingWeight(self, n: int) -> int:
        b = format(n, '032b')
        count = 0
        for i in b:
            if i == '1':
                count +=1 
        return count