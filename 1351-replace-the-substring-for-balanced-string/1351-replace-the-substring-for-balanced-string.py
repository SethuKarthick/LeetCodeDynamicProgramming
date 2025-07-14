class Solution:
    def balancedString(self, s: str) -> int:
        
        n = len(s)
        target = n //4
        freq = {}

        for c in s: freq[c] = freq.get(c, 0) + 1

        if all(freq[c] == target for c in "QWER"):
            return 0

        left = 0

        min_length = n

        for right in range(n):
            freq[s[right]] -= 1

            while all(freq.get(c, 0) <= target for c in "QWER"):

                min_length = min(min_length, right-left + 1)
                freq[s[left]] += 1
                left += 1

        return min_length 