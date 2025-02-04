class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        

        n = len(nums)

        currSum = nums[0]
        maxSum = currSum

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                currSum += nums[i]
            else:
                currSum = nums[i]
            maxSum = max(currSum, maxSum)

        return maxSum
                