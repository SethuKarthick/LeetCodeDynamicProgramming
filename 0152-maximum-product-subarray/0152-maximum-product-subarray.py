class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        

        prev_max = prev_min = result = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            current_max = max(num, prev_max*num, prev_min*num)
            current_min = min(num, prev_max*num, prev_min*num)

            result = max(current_max, result)


            prev_max = current_max
            prev_min = current_min

        return result  