'''
From each node i do a bfs. Need to figure out which nodes to add to a queue
and start the bfs from.
'''
from collections import defaultdict, deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        visited = [False] * n

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def bfs(node):
            q = deque([node])
            while q:
                node = q.popleft()
                for neighbor in adj[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        q.append(neighbor)
        
        components = 0
        for i in range(n):
            if not visited[i]:
                bfs(i)
                visited[i] = True
                components += 1

        return components

