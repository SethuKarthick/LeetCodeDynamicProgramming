from collections import defaultdict

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        points_pair = defaultdict(list)

        n = len(points)
        pairs = [tuple(p) for p in points]


        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = pairs[i]
                x2, y2 = pairs[j]

                mx = (x1+x2) / 2
                my = (y1+y2) / 2

                d_squared = (x1 - x2) ** 2 + (y1-y2) **2

                points_pair[(mx, my, d_squared)].append((pairs[i], pairs[j]))

        minArea = float("inf")

        for pair in points_pair.values():
            L = len(pair)
            for i in range(L):
                for j in range(i+1, L):
                    (p1, p2) = pair[i]
                    (p3, p4) = pair[j]

                    v1 = (p3[0] - p1[0], p3[1] - p1[1])
                    v2 = (p4[0] - p1[0], p4[1] - p1[1])

                    cross_product = abs(v1[0]* v2[1] - v2[0]*v1[1])
                    # cross_product = abs(v1[0] * v2[1] - v1[1] * v2[0])
                    area = cross_product 

                    if area < minArea:
                        minArea = area

        return 0 if minArea == float("inf") else minArea        
