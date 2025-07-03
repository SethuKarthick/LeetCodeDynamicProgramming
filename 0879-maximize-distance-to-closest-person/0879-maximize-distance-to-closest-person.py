class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev = -1 

        maxDistance = 0

        for i, seat in enumerate(seats):
            if seat == 1:
                if prev == -1:
                    maxDistance = i
                else:
                    distance = (i - prev) // 2
                    maxDistance = max(maxDistance, distance)
                prev = i

        return max(maxDistance, len(seats)- 1 - prev)