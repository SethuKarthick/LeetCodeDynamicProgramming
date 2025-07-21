class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longest = [0, 1]

        for i in range(1, len(s)):
            odd = self.helper(s, i-1, i+1)
            even = self.helper(s, i-1, i)
            current_longest = max(odd, even, key= lambda x : x[1] - x[0])
            longest = max(longest, current_longest, key= lambda x: x[1] - x[0])
        return s[longest[0]: longest[1]]



    def helper(self, s: str, l:int, r:int):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return [l+1, r]