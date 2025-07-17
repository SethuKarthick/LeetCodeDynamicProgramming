class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq = {}
        for char in words[0]:
            freq[char] = freq.get(char, 0) + 1

        
        for word in words[1:]:
            temp = {}
            for char in word:
                temp[char] = temp.get(char, 0) + 1

            
            for char in list(freq.keys()):
                if char in temp:
                    freq[char] = min(freq[char], temp[char])
                else:
                    freq[char] = 0

        result = []
        for char, count in freq.items():
            result.extend([char] * count)

        return result
