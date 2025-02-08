class NumberContainers:

    def __init__(self):
        self.index_num = {}
        self.num_indices = {}

    def change(self, index: int, number: int) -> None:
        self.index_num[index] = number

        if number not in self.num_indices:
            self.num_indices[number] = []
        heapq.heappush(self.num_indices[number], index)

    def find(self, number: int) -> int:
        if number not in self.num_indices:
            return -1

        pos_indices = self.num_indices[number]
        while pos_indices:
            min_index = pos_indices[0]

            if self.index_num[min_index] == number:
                return min_index

            heapq.heappop(pos_indices)

        return -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)