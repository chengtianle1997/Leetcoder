
# O(3Nˆ2)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row_num, col_num = len(grid), len(grid[0])
        visited = [[False] * len(row) for row in grid]
        overall_time = -1
        rotted_list = []
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # find all rotted oranges first
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 2:
                    rotted_list.append((row, col))
        
        # BFS
        while rotted_list:
            counter = len(rotted_list)
            overall_time += 1
            for i in range(counter):
                row, col = rotted_list.pop(0)
                if not visited[row][col]:
                    visited[row][col] = True
                    # all directions
                    for direction in directions:
                        _row, _col = row + direction[0], col + direction[1]
                        # check boundaries
                        if 0 <= _row < row_num and 0 <= _col < col_num and grid[_row][_col] == 1:
                            # the orange that can be rotted, traverse its neighbors
                            grid[_row][_col] = 2
                            rotted_list.append((_row, _col))
        
        # there is no more oranges that can be rotted
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if not visited[row][col] and grid[row][col] == 1:
                    return -1
        
        return overall_time if overall_time > 0 else 0
                        
                    
# O(2Nˆ2), add a fresh counter
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row_num, col_num = len(grid), len(grid[0])
        visited = [[False] * len(row) for row in grid]
        
        minute_passed = 0
        rotted_list = []
        fresh_count = 0
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        
        # find all rotted and fresh oranges first
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 2:
                    rotted_list.append((row, col))
                if grid[row][col] == 1:
                    fresh_count += 1
        
        # BFS
        while rotted_list and fresh_count > 0:
            rotted_count = len(rotted_list)
            minute_passed += 1
            for _ in range(rotted_count):
                row, col = rotted_list.pop(0)
                if not visited[row][col]:
                    visited[row][col] = True
                    # all directions
                    for direction in directions:
                        _row, _col = row + direction[0], col + direction[1]
                        # check boundaries
                        if 0 <= _row < row_num and 0 <= _col < col_num and grid[_row][_col] == 1:
                            # the orange that can be rotted, traverse its neighbors
                            grid[_row][_col] = 2
                            fresh_count -= 1
                            rotted_list.append((_row, _col))
        
        return minute_passed if fresh_count == 0 else -1
                        
                    
