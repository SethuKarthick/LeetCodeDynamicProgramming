class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        for i, num in enumerate(nums):
            potential_match = target - num
            if potential_match in seen:
                return [i, seen[potential_match]]
            seen[num] = i

        return [-1, -1]