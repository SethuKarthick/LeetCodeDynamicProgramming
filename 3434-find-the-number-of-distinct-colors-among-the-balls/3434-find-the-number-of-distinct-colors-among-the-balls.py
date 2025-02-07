class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        
        added_color = {}
        freq = {}

        ans = []

        for ball, color in queries:
            if ball in added_color:
                old_color = added_color[ball]
                freq[old_color] -= 1
                if freq[old_color] == 0:
                    del freq[old_color]

            added_color[ball] = color
            freq[color] = freq.get(color, 0) + 1
            ans.append(len(freq))

        return ans