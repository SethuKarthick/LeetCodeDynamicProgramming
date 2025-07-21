class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for word in strs:
            count =  [0] * 26

            for ch in word:
                count[ord(ch) - ord("a")] += 1
            
            key = tuple(count)

            if key not in anagram_map:
                anagram_map[key] = []

            anagram_map[key].append(word)

        return list(anagram_map.values())