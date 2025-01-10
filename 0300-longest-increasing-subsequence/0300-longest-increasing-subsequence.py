class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        if not nums:
            return 0
        n = len(nums)
        
        sequences = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    sequences[i] = max(sequences[i], sequences[j]+1)

        return max(sequences)

    #     sums = nums[:]
    #     maxSumIdx = 0

    #     for i in range(n):
    #         for j in range(i):

    #             if nums[j] < nums[i] and sums[j] + nums[i] >= sums[i]:
    #                 sums[i] = sums[j] + nums[i]
    #                 sequences[i] = j

    #     if sums[i] >= sums[maxSumIdx]:
    #         maxSumIdx = i
    #     return self.buildSequence(nums, sequences, maxSumIdx)

    # def buildSequence(self, nums, sequences, currentIdx):
    #     sequence = []
    #     while currentIdx is not None:
    #         sequence.append(nums[currentIdx])
    #         currentIdx = sequences[currentIdx]
    #     return len(sequence)

    
        