import math 

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        while  k > 0:
            gifts = sorted(gifts)
            gifts[-1] = math.floor(math.sqrt(gifts[-1]))
            k -= 1
        

        return sum(gifts)

        