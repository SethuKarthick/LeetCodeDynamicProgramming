class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        sortedList = sorted(intervals, key = lambda x: x[0])

        mergedIntervals = []

        currentInterval = sortedList[0]
        mergedIntervals.append(currentInterval)

        for interval in sortedList:
            _, currentEnd = currentInterval[0], currentInterval[1]

            nextStart, nextEnd = interval[0], interval[1]

            if currentEnd >= nextStart:
                currentInterval[1] = max(currentEnd, nextEnd)
            else:
                currentInterval = interval 
                mergedIntervals.append(currentInterval)

        return mergedIntervals