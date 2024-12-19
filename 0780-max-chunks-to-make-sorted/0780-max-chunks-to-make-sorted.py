class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        maxSoFar = 0
        chunks = 0

        for i, num in enumerate(arr):
            maxSoFar = max(maxSoFar, num)
            if maxSoFar == i:
                chunks += 1
        return chunks