from collections import deque, defaultdict
import bisect

class Router:

    def __init__(self, memoryLimit: int):
        self.memory = memoryLimit
        self.seen = set()
        self.queue = deque()
        self.destination = defaultdict(list)
        self.processed = defaultdict(int)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.seen:
            return False 
        if len(self.queue) == self.memory:
            self.evict()
        self.queue.append(key)
        self.seen.add(key)
        self.destination[destination].append(timestamp)
        return True

    def evict(self):
        source, destination, timestamp = self.queue.popleft()
        self.seen.remove((source, destination, timestamp))
        self.processed[destination] += 1



    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        source, destination, timestamp = self.queue.popleft()
        self.seen.remove((source, destination, timestamp))
        self.processed[destination] += 1
        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.destination.get(destination, [])
        to_skip = self.processed.get(destination, 0)
        valid_timestamps = timestamps[to_skip:]

        left = bisect.bisect_left(valid_timestamps, startTime)
        right = bisect.bisect_right(valid_timestamps, endTime)

        return right - left
        # count = 0
        # for i in range(to_skip, len(timestamps)):
        #     t = timestamps[i]
        #     if startTime <= t <= endTime:
        #         count += 1
        # return count



# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)