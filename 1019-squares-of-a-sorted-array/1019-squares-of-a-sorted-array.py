class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1

        result =  [0 for _ in range(n)]
        res_idx = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[res_idx] = nums[left] ** 2
                left += 1
            else:
                result[res_idx] = nums[right] ** 2
                right -= 1

            res_idx -= 1
        return result 