class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        # Convert the list of string numbers to integers
        nums = [self.stringToInt(num) for num in nums]
        
        # Initialize the heap with the first k elements
        heap = Heap(nums[:k])  # We need to keep exactly k elements in the heap
        
        # Now, process the remaining elements in nums
        for idx in range(k, len(nums)):
            minValue = heap.peak()  # Get the smallest element (the root of the heap)
            if nums[idx] > minValue:
                heap.remove()  # Remove the smallest element
                heap.insert(nums[idx])  # Insert the current element

        # After processing all elements, the root of the heap contains the kth largest element
        return str(heap.peak())  # Return the root as a string


    def stringToInt(self, num: str) -> int:
        # Convert the string representation of a number to an integer
        res = 0
        for chr in num:
            res = res * 10 + (ord(chr) - ord('0'))
        return res


class Heap:
    
    def __init__(self, array):
        # Build the heap using the array
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # Build a heap from the array (min-heap)
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    def siftDown(self, currentIdx, endIdx, heap):
        # Move the element at currentIdx down to restore the heap property
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx

            # If the current node is larger than the smallest child, swap them
            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                return

    def siftUp(self, currentIdx, heap):
        # Move the element at currentIdx up to restore the heap property
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def peak(self):
        # Return the root of the heap (the smallest element)
        return self.heap[0]

    def remove(self):
        # Remove the root (the smallest element)
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    def insert(self, value):
        # Insert a new element into the heap
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        # Swap two elements in the heap
        heap[i], heap[j] = heap[j], heap[i]
