class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        max_energy = float("-inf")

        for start in range(n-1, n-k-1, -1):
            total = 0
            i = start 
            while i >= 0:
                total += energy[i]
                max_energy = max(total, max_energy)

                i -= k
        return max_energy