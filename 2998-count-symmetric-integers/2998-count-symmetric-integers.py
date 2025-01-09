class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for n in range(low, high+1):
            if self.isSymmetric(n):
                count+=1
        return count

    def isSymmetric(self, n: int) -> bool:
        s = str(n)

        if len(s) % 2 != 0:
             return False

        mid = len(s) // 2
        firstHalf = s[:mid]
        secondHalf = s[mid:]

        firstHalfSum = sum([int(digit) for digit in firstHalf])
        secondHalfSum = sum([int(digit) for digit in secondHalf])

        return firstHalfSum == secondHalfSum

