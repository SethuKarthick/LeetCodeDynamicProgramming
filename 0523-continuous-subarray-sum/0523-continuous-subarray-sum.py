class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        mod_map = {0: -1}
        currentSum = 0

        for i in range(len(nums)):
            currentSum += nums[i]

            if k != 0:
                currentSum %= k 

            if currentSum in mod_map:
                if i - mod_map[currentSum] >= 2:
                    return True
            else:
                mod_map[currentSum] = i

        return False
