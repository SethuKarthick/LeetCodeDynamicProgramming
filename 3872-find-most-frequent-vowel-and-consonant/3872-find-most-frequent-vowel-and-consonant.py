class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set("aeiou")

        vowels_freq = {}
        cons_freq = {}

        for ch in s:
            if ch in vowels:
                vowels_freq[ch] = vowels_freq.get(ch, 0) + 1
            else:
                cons_freq[ch] = cons_freq.get(ch, 0) + 1

        vowels_max = max(vowels_freq.values(), default=0)
        cons_max = max(cons_freq.values(), default=0)

        return vowels_max + cons_max