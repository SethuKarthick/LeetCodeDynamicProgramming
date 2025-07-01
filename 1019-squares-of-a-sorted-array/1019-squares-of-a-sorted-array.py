class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = [0] * len(nums)
        idx = len(nums) - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[idx] = nums[left] ** 2
                left += 1
            else:
                result[idx] = nums[right] ** 2
                right -= 1
            idx -= 1

        return result