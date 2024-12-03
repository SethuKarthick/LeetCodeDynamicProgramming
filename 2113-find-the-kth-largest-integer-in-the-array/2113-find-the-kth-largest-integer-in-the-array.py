class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        # Step 1: Convert string numbers to integers
        nums = [self.stringToInt(num) for num in nums]
        
        # Step 2: Initialize the heap with the first `k` elements
        heap = Heap(nums[:k])  # Heap is a min-heap
        
        # Step 3: Process the rest of the elements in `nums`
        for idx in range(k, len(nums)):
            # Compare the current element with the root (smallest element in heap)
            minValue = heap.peak()
            if nums[idx] > minValue:
                # Remove the root of the heap and insert the new element
                heap.remove()
                heap.insert(nums[idx])

        # Step 4: The root of the heap now contains the kth largest number
        return str(heap.peak())  # Return it as a string

    def stringToInt(self, num: str) -> int:
        # Convert the string number to an integer
        res = 0
        for chr in num:
            res = res * 10 + (ord(chr) - ord('0'))
        return res


class Heap:
    
    def __init__(self, array):
        # Initialize the heap
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        # Build the min-heap by sifting down from the last parent index
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    def siftDown(self, currentIdx, endIdx, heap):
        # Ensure the heap property is maintained while moving down the heap
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            # Select the smaller of the two children
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx

            # If the smallest child is smaller than the current node, swap them
            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1  # Update childOneIdx to the next level
            else:
                return

    def siftUp(self, currentIdx, heap):
        # Ensure the heap property is maintained while moving up the heap
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def peak(self):
        # Return the root of the heap (smallest element in a min-heap)
        return self.heap[0]

    def remove(self):
        # Swap the root with the last element, pop it, and restore the heap property
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    def insert(self, value):
        # Add a new element and restore the heap property
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        # Swap two elements in the heap
        heap[i], heap[j] = heap[j], heap[i]
