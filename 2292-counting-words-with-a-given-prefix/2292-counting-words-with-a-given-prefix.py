class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        # for word in words:
        #     if word.startswith(pref):
        #         count += 1
        # return count

        n = len(pref)

        for word in words:
            if len(word) >= n and word[:n] == pref:
                count += 1
        return count 
        