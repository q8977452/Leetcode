class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        queue = collections.deque([])
        h = len(grid)
        w = len(grid[0])
        cnt = 0
        for i in range(w):
            for j in range(h):
                if grid[j][i] == '1':
                    grid[j][i] = '-'
                    queue.append([i, j])
                    cnt += 1
                    while queue:
                        x, y = queue.popleft()
                        if x > 0 and grid[y][x-1] == '1':
                            grid[y][x-1] = '-'
                            queue.append([x-1, y])
                        if x < w-1 and grid[y][x+1] == '1':
                            grid[y][x+1] = '-'
                            queue.append([x+1, y])
                        if y > 0 and grid[y-1][x] == '1':
                            grid[y-1][x] = '-'
                            queue.append([x, y-1])
                        if y < h-1 and grid[y+1][x] == '1':
                            grid[y+1][x] = '-'
                            queue.append([x, y+1])
        return cnt