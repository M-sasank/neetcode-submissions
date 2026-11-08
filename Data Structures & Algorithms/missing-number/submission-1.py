class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lists = [i for i in range(len(nums)+1)] + nums
        ans=0
        for i in lists:
            ans ^=i
        return ans