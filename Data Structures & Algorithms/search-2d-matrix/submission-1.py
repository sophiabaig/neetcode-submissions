class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, cols = len(matrix), len(matrix[0])

        r_low, r_high = 0, rows - 1

        while r_low <= r_high:
            
            r_mid = (r_low + r_high) // 2

            if target < matrix[r_mid][0]:
                r_high = r_mid - 1
            elif target > matrix[r_mid][cols - 1]:
                r_low = r_mid + 1
            else:
                c_low, c_high = 0, cols - 1

                while c_low <= c_high:

                    c_mid = (c_low + c_high) // 2

                    if target == matrix[r_mid][c_mid]:
                        return True
                    elif target > matrix[r_mid][c_mid]:
                        c_low = c_mid + 1
                    else:
                        c_high = c_mid - 1

                return False
        
        return False
