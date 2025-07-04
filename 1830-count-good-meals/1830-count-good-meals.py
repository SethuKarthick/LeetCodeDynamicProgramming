class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10**9 + 7

        powers = [1 << i for i in range(21)]
        count = {}
        res = 0

        for num in deliciousness:
            for power in powers:
                diff = power - num
                if diff in count:
                    res += count[diff]
            count[num] = count.get(num, 0) + 1

        return res % MOD
