from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        adj = defaultdict(list)
        d = defaultdict(int)
        visited = set()
        q = deque()

        for root,child in edges:
            adj[root].append(child)
            adj[child].append(root)
        
        q.append(0)
        visited.add(0)
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for nei in adj[node]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
                    
        return len(visited) == n
                    


        