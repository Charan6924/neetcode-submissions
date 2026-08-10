'''
I start a bfs from each leaf node. I explore every node using bfs. If node not visited i add it to q. Number of bfs calls = number of componets
'''
from collections import defaultdict, deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        out = 0
        visited = [False] * n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(node):
            q = deque([node])
            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    visited[node] = True
                    for nxt in adj[node]:
                        if not visited[nxt]:
                            q.append(nxt)

        for i in range(n):
            if not visited[i]:
                out += 1
                bfs(i)

        return out
