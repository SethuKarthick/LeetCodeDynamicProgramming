class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = []
        prev_sorted_word = None

        for word in words:
            sorted_word = ''.join(sorted(word))
            if sorted_word != prev_sorted_word:
                result.append(word)
            prev_sorted_word = sorted_word  # Update the last seen sorted word

        return result