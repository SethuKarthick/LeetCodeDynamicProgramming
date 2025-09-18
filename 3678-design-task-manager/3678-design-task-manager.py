import heapq

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        
        self.task_map = {}
        self.heap = []

        for user_id, task_id, priority in tasks:
            self.add(user_id, task_id, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_map[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId in self.task_map:
            userId, _ = self.task_map[taskId]
            self.task_map[taskId] = (userId, newPriority)
            heapq.heappush(self.heap, (-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_map:
            del self.task_map[taskId]

    def execTop(self) -> int:
        while self.heap:
            currentPriority, tId, userId = heapq.heappop(self.heap)
            taskId = -tId
            currentPriority = -currentPriority

            if taskId in self.task_map:
                uId, priority = self.task_map[taskId]

                if uId == userId and priority == currentPriority:
                    del self.task_map[taskId]

                    return userId
        return -1



        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()