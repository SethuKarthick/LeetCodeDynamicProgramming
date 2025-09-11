class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("AEIOUaeiou")

        vowels_char = sorted([ch for ch in s if ch in vowels])
        result = []
        i = 0
        for ch in s:
            if ch in vowels:
                result.append(vowels_char[i])
                i+=1
            else:
                result.append(ch)
        return "".join(result)