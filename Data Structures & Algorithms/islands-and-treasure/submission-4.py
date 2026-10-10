'''
run a bfs from each treasure chest. Each cell thats not 0 or inf gets the level of the traversal
'''
from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m,n = len(grid),len(grid[0])
        q = deque()
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        land = 2147483647
        
        #seed the queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j,0))

        while q:
            for _ in range(len(q)):
                i,j,dist = q.popleft()
                for dx,dy in dirs:
                    x = i + dx
                    y = j + dy
                    if x >= 0 and y >= 0 and x < m and y < n and grid[x][y] == land:
                        grid[x][y] = min(1+dist,grid[x][y])
                        q.append((x,y,1+dist))


        