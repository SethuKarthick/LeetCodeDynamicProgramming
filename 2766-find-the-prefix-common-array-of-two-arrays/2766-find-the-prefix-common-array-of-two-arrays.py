class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        arr = [0] * (n+1)
        res = [0] * (n)
        count = 0

        for i in range(n):
            arr[A[i]] += 1
            if arr[A[i]] == 2:
                count +=1 
            arr[B[i]] += 1
            if arr[B[i]] == 2:
                count += 1
            
            res[i] = count

        return res 