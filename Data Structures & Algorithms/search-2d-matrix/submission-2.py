class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rLow = 0
        rHigh = len(matrix) - 1
        while rLow <= rHigh:
            rMid = rLow + (rHigh - rLow) // 2
            cLow = 0
            cHigh = len(matrix[rMid]) - 1
            if matrix[rMid][cLow] > target:
                rHigh = rMid - 1
                continue
            elif matrix[rMid][cHigh] < target:
                rLow = rMid + 1
                continue
            while cLow <= cHigh:
                cMid = cLow + (cHigh - cLow) // 2
                if matrix[rMid][cMid] == target:
                    return True
                elif matrix[rMid][cMid] > target:
                    cHigh = cMid - 1
                elif matrix[rMid][cMid] < target:
                    cLow = cMid + 1
            return False
        return False