# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        pq = []

        for idx, value in enumerate(lists):
            if value:
                heapq.heappush(pq, (value.val, idx, value))
            
        dummy = ListNode()

        current = dummy 

        while(pq):
            val, idx, node = heapq.heappop(pq)
            current.next = node 
            current = current.next

            if node.next:
                heapq.heappush(pq, (node.next.val, idx, node.next))

        return dummy.next


        