class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n, res, inc, dec = len(nums), 1, 1, 1

        if n == 1: return 1

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                inc += 1
                dec = 1
            elif nums[i] < nums[i-1]:
                dec += 1
                inc = 1
            else:
                inc = dec = 1
            res = max(inc, dec, res)

        return res