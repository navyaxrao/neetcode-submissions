class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        part_of_island = set()
        num_islands = 0
        num_rows = len(grid)
        num_cols = len(grid[0])
        directions = [[1,0], [0, 1], [-1, 0], [0, -1]]
        def dfs(row, col):
                    if (row < 0 or col < 0 or 
                    row >= num_rows or col >= num_cols or grid[row][col] == "0" or 
                    (row, col) in part_of_island):
                        return
                    part_of_island.add((row, col))
                    for dr, dc in directions:
                        dfs(row + dr, col + dc)

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == "1" and (row, col) not in part_of_island:
                    dfs(row, col)
                    num_islands += 1
        return num_islands


                    


        