class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        columns = initialiseColumns(points)

        
        sortedColumns = sorted(columns.keys())

        edgeArea = {}
        minArea = float("inf")

        for x in sortedColumns:
            yValuesInCurrentColumns = sorted(columns[x])

            for currentIdx, y2 in enumerate(yValuesInCurrentColumns):
                for previousIdx in range(currentIdx):
                    y1 = yValuesInCurrentColumns[previousIdx]
                    pointsToString = str(y1) + ":" + str(y2)
                    if pointsToString in edgeArea:
                        currentArea = (x - edgeArea[pointsToString]) * (y2-y1)
                        minArea = min(minArea, currentArea)
                    edgeArea[pointsToString] = x
            
        return minArea if minArea != float("inf") else 0 

def initialiseColumns(points):
    columns = {}

    for point in points:
        x, y = point
        if x not in columns:
            columns[x] = []

        columns[x].append(y)

    return columns
        