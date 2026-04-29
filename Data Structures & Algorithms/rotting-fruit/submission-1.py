class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque()
        num_fresh = 0
        mins = 0
        num_rows = len(grid)
        num_cols = len(grid[0])
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == 2:
                    queue.append([row, col])
                elif grid[row][col] == 1:
                    num_fresh +=1
        
        while(queue and num_fresh > 0):
            length = len(queue)
            for i in range(length):
                r, c = queue.popleft()
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if new_r >= 0 and new_r < num_rows and new_c >= 0 and new_c < num_cols and grid[new_r][new_c] == 1:
                        num_fresh -=1
                        grid[new_r][new_c] = 2
                        queue.append([new_r, new_c])
            mins += 1
        
        if num_fresh == 0:
            return mins
        else:
            return -1
        