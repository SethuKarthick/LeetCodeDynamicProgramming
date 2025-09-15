class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_set = set(brokenLetters)

        count = 0

        word_list = text.split()

        for word in word_list:
            if all(ch not in broken_set for ch in word):
                count += 1
        return count 
