from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)

        # sset = dict()

        # for char in s:
        #     if char in sset:
        #         sset[char] = sset[char] + 1
        #     else:
        #         sset[char] = 1
        # for char in t:
        #     if char in sset and sset[char]>1:
        #         sset[char] = sset[char] - 1
        #     elif char in sset and sset[char] == 1:
        #         sset.pop(char)
        #     else:
        #         return False
        # if not sset:
        #     return True
        # else:
        #     return False
        