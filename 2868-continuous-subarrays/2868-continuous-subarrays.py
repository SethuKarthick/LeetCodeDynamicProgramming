class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:


        n  = len(nums)
        window = {}
        
        start = 0
        totalSubArrays = 0


        for end in range(n):
            # if nums[end] not in window:
            window[nums[end]] = window.get(nums[end], 0) + 1
            while max(window) - min(window) > 2:
                window[nums[start]] -= 1
                if window[nums[start]] == 0:
                    del window[nums[start]]
                start += 1
            totalSubArrays += end - start + 1

        return totalSubArrays