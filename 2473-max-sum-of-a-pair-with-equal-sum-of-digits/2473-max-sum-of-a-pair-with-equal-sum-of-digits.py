class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digitSum(n):
            return sum([int(digit) for digit in str(n)])


        similarSum = defaultdict(list)

        for i in nums:
            similarSum[digitSum(i)].append(i)

        res, ans = -1, []

        for pair in similarSum.values():
            if len(pair) >= 2:
                ans.append(pair)

        for val in ans:
            val.sort(reverse= True)
            res = max(res, val[0]+ val[1])

        return res