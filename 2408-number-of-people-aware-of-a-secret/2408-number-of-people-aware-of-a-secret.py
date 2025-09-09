class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7

        dp = [0] * (n+1)
        dp[1] = 1

        shared = 0

        for day in range(2, n+1):

            if day - delay >= 1:

                shared += dp[day - delay]

            if day - forget >= 1:
                shared -= dp[day - forget]

            shared %= MOD 
            dp[day] = shared


        result = sum(dp[n - forget + 1 : n+1]) % MOD

        return result 



