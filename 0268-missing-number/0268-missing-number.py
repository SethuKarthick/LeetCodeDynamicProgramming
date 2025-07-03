class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums.sort()
        # if nums[0] != 0:
        #     return 0

        # for i in range(1, len(nums)):
        #     if nums[i] - nums[i-1] > 1:
        #         return nums[i] - 1

        # return nums[len(nums)-1] + 1
        missing = len(nums)

        for i, num in enumerate(nums):
            missing ^= i^num

        return missing