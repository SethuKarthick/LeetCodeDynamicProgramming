class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            if num -1 not in nums_set:
                current = num
                current_longest = 1
                while current + 1 in nums_set:
                    current += 1
                    current_longest += 1
                if current_longest > longest:
                    longest = current_longest 
        return longest 

        # if not nums:
        #     return 0

        # nums_set = set(nums)  # O(1) lookups
        # visited = {num: False for num in nums}

        # longest = 0

        # best_range = []

        # for num in nums:
        #     if visited[num]: 
        #         continue 
        #     visited[num] = True 


        #     current_length = 1

        #     left = num - 1
        #     right = num + 1

        #     while left in nums and not visited[left]:
        #         visited[left] = True
        #         current_length += 1
        #         left -= 1
            
        #     while right in nums and not visited[right]:
        #         visited[right] = True 
        #         current_length += 1
        #         right += 1
            
        #     if current_length > longest:
        #         longest = current_length 

        # return longest 
