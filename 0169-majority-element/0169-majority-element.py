class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # res = {}

        # for num in nums:
        #     res[num] = res.get(num, 0) + 1
        
        # res = sorted(res.items(), key = lambda kv: kv[1], reverse=True)

        # return res
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num 
            count += 1 if num == candidate else -1
        return candidate 

        