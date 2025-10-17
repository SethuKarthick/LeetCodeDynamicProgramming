from functools import lru_cache

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)

        def popcount(x):
            return bin(x).count('1')

        @lru_cache(maxsize=None)
        def dp(i: int, mask: int, canChange: int) -> int:
            if i == n:
                return 0

            res = 0

            # Option 1: Don't change s[i]
            bit = 1 << (ord(s[i]) - ord('a'))
            new_mask = mask | bit
            if popcount(new_mask) <= k:
                res = dp(i + 1, new_mask, canChange)
            else:
                # Exceeds k distinct characters, must start new partition
                res = 1 + dp(i + 1, bit, canChange)

            # Option 2: Try changing s[i] to any other character (if change allowed)
            if canChange:
                for c in range(26):
                    if c == ord(s[i]) - ord('a'):
                        continue  # Skip changing to same character
                    bit2 = 1 << c
                    new_mask2 = mask | bit2
                    if popcount(new_mask2) <= k:
                        res = max(res, dp(i + 1, new_mask2, 0))
                    else:
                        res = max(res, 1 + dp(i + 1, bit2, 0))

            return res

        return dp(0, 0, 1) + 1  # Add 1 for the first partition
