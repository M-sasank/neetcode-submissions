class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        if len(nums)<=1:
            return False
        for i in range(len(nums)):
            if nums[i] in hash.keys():
                return True
            else:
                hash[nums[i]]= i
        return False