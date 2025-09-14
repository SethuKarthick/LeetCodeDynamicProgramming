from typing import List
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(word: str) -> str:
            vowels = set('aeiou')
            return ''.join('*' if c in vowels else c for c in word.lower())

        exact = set(wordlist)  # O(N)
        lower_map = {}         # lowercase -> first word
        vowel_map = {}         # devoweled(lowercase) -> first word

        for word in wordlist:  # O(N * L)
            low = word.lower()
            dev = devowel(low)
            if low not in lower_map:
                lower_map[low] = word
            if dev not in vowel_map:
                vowel_map[dev] = word

        result = []

        for query in queries:  # O(Q * L)
            if query in exact:
                result.append(query)
            else:
                low = query.lower()
                dev = devowel(low)
                if low in lower_map:
                    result.append(lower_map[low])
                elif dev in vowel_map:
                    result.append(vowel_map[dev])
                else:
                    result.append("")
        
        return result