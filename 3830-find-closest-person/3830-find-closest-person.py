class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        

        x_min = abs(x-z) 
        y_min = abs(y-z)

        if x_min < y_min:
            return 1
        elif x_min > y_min:
            return 2
        else:
            return 0 
        # return min(abs(x-z), abs(y-z))
        # # if x >= z <= y:
        # #     return min(abs(x-z), abs(y-z))
        # # if z >= x and z >= y:
        # #     return min(abs(x-z), abs(y-z))
        