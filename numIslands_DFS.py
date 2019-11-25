#DFS
##對每個有'1'的位置進行DFS，把和它四聯通的位置全部變成'0'
##這樣就能把一個點推廣到一個島
##所以，進行了DFS的次數，就是有多少島的數目

##DFS函數意義:已知當前是1，把它周圍相鄰的所有1轉換成0
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    self.dfs(grid, r, c)
                    res += 1
        return res
        
    def dfs(self, grid, i, j):
        dirs = [[-1, 0], [0, 1], [0, -1], [1, 0]]
        grid[i][j] = "0"
        for dir in dirs:
            nr, nc = i + dir[0], j + dir[1]
            if nr >= 0 and nc >= 0 and nr < len(grid) and nc < len(grid[0]):
                if grid[nr][nc] == "1":
                    self.dfs(grid, nr, nc)