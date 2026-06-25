'''
create a dictionary of number to list of characters it can map to
backtrack(i,cur) if i == len(digits) add to out list
for each char in list, add to cur and backtrack(i+1,cur)
pop from cur and recurse
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        out = []

        def backtrack(i,cur):
            if i == len(digits):
                out.append("".join(cur))
                return

            for j in d[digits[i]]:
                cur.append(j)
                backtrack(i+1,cur)
                cur.pop()
        backtrack(0,[])
        return out
