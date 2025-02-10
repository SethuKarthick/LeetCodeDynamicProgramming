class Solution:
    def clearDigits(self, s: str) -> str:
        res = []

        for ch in s:
            if "0" <= ch <= "9" and res:
                res.pop()
            else:
                res.append(ch)
        return "".join(res)
