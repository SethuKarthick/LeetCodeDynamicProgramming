class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        dict  = {}

        for num in banned:
            dict[num] = True


        sum, count, i = 0, 0, 1

        while i<=n:
            if i not in dict:
                if sum+i > maxSum: return count 

                sum += i
                count += 1
            i += 1
        
        return count
