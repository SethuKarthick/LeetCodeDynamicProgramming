class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        n = len(words)

        for i in range(n):
            for j in range(i+1, n):
                if self.isPrefixAndSuffixPairs(words[i], words[j]):
                    count += 1
        return count

    def isPrefixAndSuffixPairs(self, str1, str2):
        n1 = len(str1)
        n2 = len(str2)

        if n1 > n2:
            return False

        return str2[:n1] == str1 and str2[-n1:] == str1