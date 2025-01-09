class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        n = len(words)

        # for i in range(n):
        #     for j in range(i+1, n):
        #         if self.isPrefixAndSuffixPairs(words[i], words[j]):
        #             count += 1
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
            # Check if words[i] is both a prefix AND a suffix of words[j]
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                # Yo, we found a match! Increment the count.
                    count += 1
        return count

    # def isPrefixAndSuffixPairs(self, str1, str2):
    #     n1 = len(str1)
    #     n2 = len(str2)

    #     if n1 > n2:
    #         return False

        return str2[:n1] == str1 and str2[-n1:] == str1