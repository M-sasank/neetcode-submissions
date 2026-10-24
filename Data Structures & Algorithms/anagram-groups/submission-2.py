from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = list()
        anags = dict()

        for s in strs:
            x = sorted(s) #unique signature for the anagram
            x = ''.join(x)
            if x in anags:
                anags[x].append(s)
            else:
                anags[x] = [s]
        for x in anags.values():
            result.append(x)
        return result
        