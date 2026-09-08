class Solution:
    def searchMatrix(self, mat: List[List[int]], x: int) -> bool:
        n = len(mat)
        m = len(mat[0])

        lo, hi = 0, n * m - 1
        while lo <= hi:
            mid = (lo + hi) // 2

            # find row and column of element at mid index
            row = mid // m
            col = mid % m

            # if x is found, return true
            if mat[row][col] == x:
                return True

            # if x is greater than mat[row][col], search 
            # in right half
            if mat[row][col] < x:
                lo = mid + 1

            # if x is less than mat[row][col], search 
            # in left half
            else:
                hi = mid - 1

        return False