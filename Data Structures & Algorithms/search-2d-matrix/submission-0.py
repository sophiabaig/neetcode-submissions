class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):

            if matrix[r][0] <= target and matrix[r][cols - 1] >= target:

                low = 0
                high = cols - 1

                while low <= high:

                    mid = (low + high) // 2

                    if target == matrix[r][mid]:
                        return True
                    elif target > matrix[r][mid]:
                        low = mid + 1
                    else:
                        high = mid - 1
        
        return False