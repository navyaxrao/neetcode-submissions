class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # iterative BFS approach
        part_of_island = set()
        num_islands = 0
        num_rows = len(grid)
        num_cols = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]


        def bfs(row, col):
            queue = collections.deque()
            queue.append([row, col])
            part_of_island.add((row, col))

            while queue:
                node_r, node_c = queue.popleft()
                for dr, dc in directions:
                    neighbor_r, neighbor_c = node_r + dr, node_c + dc
                    if (neighbor_r < num_rows and neighbor_r >= 0 and neighbor_c < num_cols and neighbor_c >= 0 and 
                        grid[neighbor_r][neighbor_c] == "1" and 
                        (neighbor_r, neighbor_c) not in part_of_island):
                        part_of_island.add((neighbor_r, neighbor_c))
                        queue.append([neighbor_r, neighbor_c])

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == "1" and (row, col) not in part_of_island:
                    bfs(row, col)
                    num_islands += 1
        return num_islands

        # recursive dfs approach:
        # part_of_island = set()
        # num_islands = 0
        # num_rows = len(grid)
        # num_cols = len(grid[0])
        # directions = [[1,0], [0, 1], [-1, 0], [0, -1]]
        # def dfs(row, col):
        #             if (row < 0 or col < 0 or 
        #             row >= num_rows or col >= num_cols or grid[row][col] == "0" or 
        #             (row, col) in part_of_island):
        #                 return
        #             part_of_island.add((row, col))
        #             for dr, dc in directions:
        #                 dfs(row + dr, col + dc)

        # for row in range(num_rows):
        #     for col in range(num_cols):
        #         if grid[row][col] == "1" and (row, col) not in part_of_island:
        #             dfs(row, col)
        #             num_islands += 1
        # return num_islands



                    


        