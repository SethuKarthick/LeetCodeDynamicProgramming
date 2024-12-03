class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:

        l = sorted([int(i) for i in nums])
        return str(l[-k])
        
#         nums = [self.stringToInt(chr) for chr in nums]
#         heap = Heap(nums)

#         kth_largest = 0
#         for _ in range(k):
#             kth_largest = heap.remove()
#         return f"{kth_largest}"

#     def stringToInt(self, num):
#         res = 0
#         for chr in num:
#             res = res * 10 + (ord(chr) - ord('0'))
#         return res


# class Heap:
    
#     def __init__(self, array):
#         self.heap = self.buildHeap(array)


#     def buildHeap(self, array):
#         firstParentIdx = (len(array) - 2) // 2
#         for currentIdx in reversed(range(firstParentIdx+1)):
#             self.siftDown(currentIdx, len(array)-1, array)
#         return array


#     def siftDown(self, currentIdx, endIdx, heap):
#         childOneIdx = currentIdx * 2 + 1
#         while childOneIdx <= endIdx:
#             childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
#             if childTwoIdx != -1 and heap[childOneIdx] > heap[childTwoIdx]:
#                 idxToSwap = childOneIdx
#             else:
#                 idxToSwap = childTwoIdx if childTwoIdx != -1 else childOneIdx
#             if heap[idxToSwap] > heap[currentIdx]:
#                 self.swap(currentIdx, idxToSwap, heap)
#                 currentIdx = idxToSwap
#                 childOneIdx = currentIdx * 2 + 2
#             else:
#                 return 



#     def siftUp(self, currentIdx, heap):
#         parentIdx = (currentIdx -1) // 2
#         if currentIdx > 0 and heap[currentIdx] > heap[parentIdx]:
#             self.swap(currentIdx, parentIdx, heap)
#             currentIdx = parentIdx
#             parentIdx = (currentIdx -1 ) // 2


#     def remove(self):
#         self.swap(0, len(self.heap)-1, self.heap)
#         valueToRemove = self.heap.pop()
#         self.siftDown(0, len(self.heap)-1, self.heap)
#         return valueToRemove
        

    
#     def insert(self, value):
#         self.heap.append(value)
#         self.siftUp(len(self.heap)-1, self.heap)

    
#     def swap(self, i, j, heap):
#         heap[i], heap[j] = heap[j], heap[i]