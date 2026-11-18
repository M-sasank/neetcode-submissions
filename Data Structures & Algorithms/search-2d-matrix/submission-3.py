class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binaryX(x):
            l,r=0,len(x)-1
            while l<=r:
                mid = (l + r)//2
                if x[mid] == target:
                    return True
                elif target > x[mid]:
                    l = mid + 1
                elif target < x[mid]:
                    r = mid - 1
            return False
        
        
        # naive solution, this takes extra space?
        x = []
        for i in matrix:
            x += i
        return binaryX(x)

        # find out which row the target lies in and binary search that. 
        # the finding out takes O(n) comparisons? but O(n+log(m))<<O(log(m)) right?
        


