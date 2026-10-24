from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = list()
        anags = dict()

        for s in strs:
            x = sorted(s)  # ik Counter is preferred but idk how to get signature from a dict?
            x = ''.join(x) #unique signature for the anagram
            if x in anags:
                anags[x].append(s)
            else:
                anags[x] = [s]
        return list(anags.values())
        