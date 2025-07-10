class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        

        max_num = min_num = result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            prev_max = max_num

            max_num = max(num, max_num * num, min_num * num)
            min_num = min(num, max_num * num, min_num * num)

            result = max(max_num, result)

        return result