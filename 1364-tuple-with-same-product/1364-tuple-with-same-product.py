class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count = defaultdict(lambda: 0)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                count[nums[i]*nums[j]] += 1

        res = 0
        for val in count.values():
            if val > 1:
                res += 4*val*(val -1)
        return res