class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        
        if s1 == s2:
            return True 

        diff = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append(i)
                if len(diff) > 2: 
                    return False 

        if len(diff) != 2:
            return False

        i, j = diff 

        return s1[i] == s2[j] and s1[j] == s2[i]
        # if len(s1) != len(s2):
        #     return False

        # total = 0
        # for i, j in zip(s1, s2):
        #     if i != j:
        #         total += 1
            
        # return total == 0 or total == 2

