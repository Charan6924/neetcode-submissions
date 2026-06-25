class Solution:
    def partition(self, s: str) -> List[List[str]]:
        out = []
        def backtrack(start,cur):
            if start == len(s):
                out.append(cur[:])
                return

            for end in range(start+1,len(s)+1):
                sub = s[start:end]
                if sub == sub[::-1]:
                    cur.append(sub)
                    backtrack(end,cur)
                    cur.pop()
    
        backtrack(0,[])
        return out