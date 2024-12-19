class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # maxSoFar = 0
        # chunks = 0

        # for i, num in enumerate(arr):
        #     maxSoFar = max(maxSoFar, num)
        #     if maxSoFar == i:
        #         chunks += 1
        # return chunks
        prefixSum, expectedSum, chunksCount = 0, 0, 0

        for i, num in enumerate(arr):
            prefixSum += num
            expectedSum += i

            if expectedSum == prefixSum:
                chunksCount += 1

        return chunksCount