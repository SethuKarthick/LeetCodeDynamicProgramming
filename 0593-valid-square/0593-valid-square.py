class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        pointsArray = [p1, p2, p3, p4]
        pointSet = set() 

        count = 0

        for point in pointsArray:
            pointSet.add(pointsToString(point))


        for pointA in pointsArray:
            for pointB in pointsArray:
                if pointA == pointB:
                    continue

                midpoint = [ (pointA[0]+pointB[0]) / 2, (pointA[1]+pointB[1]) / 2 ]
                xDistance = pointA[0] - midpoint[0]
                yDistance = pointA[1] - midpoint[1]

                pointC = [midpoint[0]+yDistance, midpoint[1]-xDistance]
                pointD = [midpoint[0]-yDistance, midpoint[1]+xDistance]

                if pointsToString(pointC) in pointSet and pointsToString(pointD) in pointSet:
                    count += 1

        return (count / 4) > 0
   
def pointsToString(point):
    if point[0] % 1 == 0 and point[1] % 1 == 0:
        point = [int(cordinate) for cordinate in point]
    return ",".join([str(cordinate) for cordinate in point])


        