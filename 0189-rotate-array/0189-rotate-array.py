class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        

        n = len(nums)
        k = k % n

        nums.reverse()

        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]

        return nums