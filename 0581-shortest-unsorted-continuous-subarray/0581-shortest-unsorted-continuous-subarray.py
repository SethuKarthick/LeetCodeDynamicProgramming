class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0  # Already sorted
            
        min_order = float("inf")
        max_order = float("-inf")


        for i in range(len(nums)):
            num = nums[i]
            if self.is_out_of_order(i, num, nums):
                min_order = min(min_order, num)
                max_order = max(max_order, num)

        if min_order == float("inf"):
            return 0

        left = 0
        while min_order >= nums[left]:
            left += 1
        right = len(nums) - 1
        while max_order <= nums[right]:
            right -= 1

        return right - left + 1

    def is_out_of_order(self, i, num, nums):

        # if i == 0:
        #     return num > nums[i+1]
        # elif i == len(nums) -1:
        #     return num < nums[i-1]
        
        # return  num < nums[i-1] or num > nums[i+1]

        if i == 0:
            return num > nums[i + 1]  # Only compare to right neighbor
        elif i == len(nums) - 1:
            return num < nums[i - 1]  # Only compare to left neighbor
        else:
            return num > nums[i + 1] or num < nums[i - 1]

