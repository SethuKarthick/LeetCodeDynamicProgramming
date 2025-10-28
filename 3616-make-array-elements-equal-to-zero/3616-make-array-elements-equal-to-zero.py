class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        total = sum(nums)
        ans = 0
        left_sum = 0
        
        for x in nums:
            if x != 0:
                left_sum += x
            else:
                # when nums[i] == 0 at current position
                # sum to left = left_sum
                # sum to right = total â left_sum
                right_sum = total - left_sum
                if left_sum == right_sum:
                    ans += 2  # both directions are valid
                elif abs(left_sum - right_sum) == 1:
                    ans += 1  # only one direction is valid
                # then continue, left_sum remains same (x==0 adds nothing)
        
        return ans
