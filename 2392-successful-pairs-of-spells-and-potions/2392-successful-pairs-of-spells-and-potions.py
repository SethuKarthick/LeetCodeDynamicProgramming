class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        result = []

        def binary_search(target):
            left, right = 0, m
            while left < right:
                mid = (left + right) // 2
                if potions[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        for spell in spells:
            # Compute ceiling division of success / spell without using math.ceil
            min_potion = (success + spell - 1) // spell
            index = binary_search(min_potion)
            result.append(m - index)

        return result



