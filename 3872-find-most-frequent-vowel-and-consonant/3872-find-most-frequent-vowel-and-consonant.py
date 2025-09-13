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

        vowels_max = 0

        for ch, count in vowels_freq.items():
            vowels_max = max(vowels_max, count)
        cons_max = 0
        for ch, count in cons_freq.items():
            cons_max = max(cons_max, count)

        return vowels_max + cons_max