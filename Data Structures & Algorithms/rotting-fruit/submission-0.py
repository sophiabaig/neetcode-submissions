class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rotten = collections.deque()
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        fresh = 0
        minutes = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                elif grid[r][c] == 1:
                    fresh+=1

        while rotten and fresh > 0:
            q_len = len(rotten)
            minutes+=1

            for i in range(q_len):
                cur_r, cur_c = rotten.popleft()

                for dr, dc in directions:
                    new_r, new_c = cur_r + dr, cur_c + dc

                    if (new_r in range(rows) and 
                        new_c in range(cols) and 
                        grid[new_r][new_c] == 1):

                        grid[new_r][new_c]=2
                        fresh-=1
                        rotten.append((new_r, new_c))

        if fresh > 0: return -1

        return minutes