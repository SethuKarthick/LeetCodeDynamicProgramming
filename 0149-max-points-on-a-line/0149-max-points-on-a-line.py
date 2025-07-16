class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        

        max_points = 1

        for idx1, p1 in enumerate(points):
            slopes = {}

            for idx2 in range(idx1+1, len(points)):
                p2 = points[idx2]

                rise, run = self.getSlopes(p1, p2)

                slopeKeys = self.createHashableKey(rise, run)

                slopes[slopeKeys] = slopes.get(slopeKeys, 1) + 1

            max_points = max(max_points, max(slopes.values(), default=0))

        return max_points

    def getSlopes(self, p1, p2):
        p1x, p1y = p1
        p2x, p2y = p2

        slope = [1, 0]

        if p1x != p2x:
            xdiff = p1x - p2x
            ydiff = p1y - p2y
            divisor = self.gcd(abs(xdiff), abs(ydiff))
            xdiff //= divisor
            ydiff //= divisor 

            if xdiff < 0:
                xdiff *= -1
                ydiff *= -1
            
            slope = [ydiff, xdiff]

        return slope

    def createHashableKey(self, x, y):
        return str(x) + ":" + str(y)

    def gcd(self, a, b):
        while True:
            if a == 0:
                return b 
            if b == 0:
                return a 

            a, b = b, a%b
