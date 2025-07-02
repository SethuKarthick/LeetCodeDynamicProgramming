class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dup = {}

        for num in nums:
            dup[num] = dup.get(num, 0) + 1
            if dup[num] == 2:
                return num 
        