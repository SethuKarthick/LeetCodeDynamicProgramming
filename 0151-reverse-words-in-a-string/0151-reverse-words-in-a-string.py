class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        i = len(s) - 1

        while i >= 0:
            if s[i] == " ":
                i -= 1
                continue

            end = i

            while i >= 0 and s[i] != " ":
                i -= 1

            res.append(s[i+1 : end+1])
            
        
        return ' '.join(res)