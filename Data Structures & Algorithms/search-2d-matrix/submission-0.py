class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x = []
        for i in matrix:
            x += i
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

