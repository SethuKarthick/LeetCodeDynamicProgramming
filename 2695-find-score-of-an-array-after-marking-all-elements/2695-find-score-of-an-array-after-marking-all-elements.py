class Solution:
    def findScore(self, nums: List[int]) -> int:

        n = len(nums)
        marked = [False] * n 
        sum = 0

        indexedNums = sorted((val, idx) for idx, val in enumerate(nums))

        for val, idx in indexedNums:
            if not marked[idx]:
                sum += val

                marked[idx] = True
                if idx > 0:
                    marked[idx-1] = True
                if idx < n -1:
                    marked[idx+1] = True

        return sum 
