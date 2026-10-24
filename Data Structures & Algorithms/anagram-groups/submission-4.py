from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = list()
        anags = dict()

        for s in strs:
            sig = list([0]*26)
            for c in s:
                sig[ord(c) - ord('a')] +=1
            # x = ''.join(x) #unique signature for the anagram
            x = tuple(sig)
            if x in anags:
                anags[x].append(s)
            else:
                anags[x] = [s]
        return list(anags.values())
        