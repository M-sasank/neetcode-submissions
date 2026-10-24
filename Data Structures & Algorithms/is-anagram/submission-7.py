class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ash = [0]*26
        ash1 = [0]*26
        print(ash)
        for c in s:
            ash[ord(c)-ord('a')] += 1
        for c in t:
            ash1[ord(c)-ord('a')] += 1
        ash = ''.join([str(n) for n in ash])
        ash1 = ''.join([str(n) for n in ash1])
        if ash != ash1:
            return False
        else:
            return True