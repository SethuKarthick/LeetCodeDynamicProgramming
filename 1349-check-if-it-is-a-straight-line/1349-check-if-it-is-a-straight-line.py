class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        

        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        def getSlopes(p1, p2):
            p1x, p1y = p1
            p2x, p2y = p2

            rise = p2y - p1y
            run = p2x - p1x

            if run == 0:
                return (float("inf"), 0)
            
            if rise == 0:
                return (0, float("inf"))

            g = gcd(rise, run)
            rise = rise // g
            run = run // g

            if run < 0:
                rise *= -1 
                run *= -1 

            return (rise, run)

        def createHash(rise, run):
            return str(rise) + ":" + str(run)

        rise, run = getSlopes(coordinates[0], coordinates[1])
        p1 = coordinates[0]

        for idx in range(2, len(coordinates)):
            new_rise, new_run = getSlopes(p1, coordinates[idx])
            if new_rise != rise or new_run != run:
                return False 
            
        return True 

        # for idx1, p1 in enumerate(coordinates):
        #     slope = {}

        #     for p2 in range(idx+1, len(coordinates)):
        #         rise, run = getSlopes(p1, p2)
        #         slopeKey = createHash(rise, run)
                 



        
