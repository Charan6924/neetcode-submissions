'''
I start a bfs from each leaf node. I explore every node using bfs. If node not visited i add it to q. Number of bfs calls = number of componets
'''
from collections import defaultdict, deque
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        d = defaultdict(int)
        visited = set()
        out = 0

        def bfs(q):
            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    visited.add(node)
                    for nei in adj[node]:
                        if nei not in visited:
                            q.append(nei)

        for root,child in edges:
            adj[root].append(child)
            adj[child].append(root)
            d[root] += 1
            d[child] += 1

        for i in range(n):
            if i not in visited:
                q = deque()
                q.append(i)
                bfs(q)
                out += 1
        return out

        