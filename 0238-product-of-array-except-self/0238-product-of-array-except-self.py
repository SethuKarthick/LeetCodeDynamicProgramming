class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in range(len(nums))]

        leftRunningLength = 1
        for i in range(len(nums)):
            result[i] = leftRunningLength
            leftRunningLength *= nums[i]

        rightRunningLength = 1
        for i in reversed(range(len(nums))):
            result[i] *= rightRunningLength
            rightRunningLength *= nums[i]

        return result