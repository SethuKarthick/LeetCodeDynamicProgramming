class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(1, n):
            b = n - a
            if self.check_zero(a) and self.check_zero(b):
                return [a, b]
            

    def check_zero(self, num):
        if "0" in str(num):
            return False 
        return True