class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        x = derived[0]

        for i in range(1, len(derived)):
            x ^= derived[i]
        return x == 0