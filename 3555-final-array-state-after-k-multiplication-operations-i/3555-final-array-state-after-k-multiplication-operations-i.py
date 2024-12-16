class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        for _ in range(k):
            xIdxToMultiply = nums.index(min(nums))
            nums[xIdxToMultiply] *= multiplier
        return nums
        