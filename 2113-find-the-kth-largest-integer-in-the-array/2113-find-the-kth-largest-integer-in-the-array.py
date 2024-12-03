class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [self.stringToInt(num) for num in nums]
        # nums = [self.stringToInt(num) for num in nums]
        
        heap = Heap(nums[:k])
        # heap = Heap(nums[:k])

        for idx in range(k, len(nums)):
            minValue = heap.peak()
            if nums[idx] > minValue:
                heap.remove()
                heap.insert(nums[idx])

        return f"{heap.peak()}"
        


    def stringToInt(self, num):
        res = 0
        for chr in num:
            res = res * 10 + (ord(chr) - ord('0'))
        return res


class Heap:
    
    def __init__(self, array):
        self.heap = self.buildHeap(array)


    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx+1)):
            self.siftDown(currentIdx, len(array)-1, array)
        return array


    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx 
            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return 



    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx -1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1 ) // 2

    def peak(self):
        return self.heap[0]


    def remove(self):
        self.swap(0, len(self.heap)-1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap)-1, self.heap)
        return valueToRemove
        

    
    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap)-1, self.heap)

    
    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]