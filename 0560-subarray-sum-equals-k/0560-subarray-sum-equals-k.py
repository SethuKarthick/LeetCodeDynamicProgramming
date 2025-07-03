class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0: 1}

        sum = 0
        count = 0

        for i, num in enumerate(nums):
            sum += num

            if sum-k in prefixSum:
                count += prefixSum[sum-k]
            prefixSum[sum] = prefixSum.get(sum, 0) + 1
        
        return count