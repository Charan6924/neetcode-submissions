from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        if n == 1:
            return True
            
        d = defaultdict(int)
        adj = defaultdict(list)
        q = deque()

        for a,b in edges:
            d[a] += 1
            d[b] += 1
            adj[a].append(b)
            adj[b].append(a)
        
        for i in range(n):
            if d[i] == 1:
                q.append(i)

        count = 0
        while q:
            node = q.popleft()
            d[node] -= 1
            count += 1
            for nxt in adj[node]:
                d[nxt] -= 1
                if d[nxt] == 1:
                    q.append(nxt)

        return count == n
