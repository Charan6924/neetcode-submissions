'''
-1 means it cant be traversed so we stop the recursion
0 is a treasure chest and inf is land.

We can do a bfs from each treasure chest. Update cell values if it is = inf
We store the min distance to a treasure chest to handle multiple updates
'''
from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        land = 2147483647
        q = deque()
        m,n = len(grid),len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j,0)) # a chest is 0 steps away from a chest

        d = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            for _ in range(len(q)):
                i,j,dist = q.popleft()
                for dq, dt in d:
                    if i + dq < m and i + dq >= 0 and j + dt >=0 and j + dt < n and grid[i+dq][j+dt] == land:
                        grid[i+dq][j+dt] = min(dist + 1,grid[i+dq][j+dt])
                        q.append((i+dq,j+dt,dist+1))
        



