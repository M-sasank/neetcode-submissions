class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        sett = set(nums) #O(n)
        if len(sett)!=len(nums): #O(1)s as len is a read from a ptr, no computation in python
            return True
        return False
        """
        # However, we can be a bit greedy in saving time
        # and memory and exit as soon as we see the duplicate
        seen = set()
        for i in nums:
            if not i in seen:
                seen.add(i)
            else: 
                return True
        return False