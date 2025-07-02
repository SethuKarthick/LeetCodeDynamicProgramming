class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # left = 0
        # right = len(nums) - 1 

        # while left < right:
        #     while left < right and nums[right] == 0:
        #         right -= 1
        #     if nums[left] == 0:
        #         nums[left], nums[right] = nums[right], nums[left]
        #         right -= 1
        #     left += 1
        # return nums

        left = 0 
        right = 0

        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

        return nums