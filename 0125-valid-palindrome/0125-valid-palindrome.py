class Solution:
    def isPalindrome(self, s: str) -> bool:
        sen = ""

        for char in s:
            if char.isalnum():
                sen += char
        
        sen = sen.lower()

        return sen == sen[::-1]