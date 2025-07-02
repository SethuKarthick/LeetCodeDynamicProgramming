class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        non_increasing = True
        non_decreasing = True 
        idx = 0

        for idx in range(1, len(nums)):
            if nums[idx] < nums[idx-1]:
                non_increasing = False
            if nums[idx] > nums[idx-1]:
                non_decreasing = False

        return non_increasing or non_decreasing