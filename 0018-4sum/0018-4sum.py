class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quads = []
        nums.sort()

        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i -1]:
                continue

            for j in range(i+1, len(nums)-2):
                if j > i + 1 and nums[j] == nums [j -1 ]:
                    continue

                left, right = j+1, len(nums) -1
                while left < right:
                    currentSum = nums[i] + nums[j] + nums[left] + nums[right]
                    if currentSum == target:
                        quads.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif currentSum > target:
                        right -= 1
                    else:
                        left += 1

        return quads
                    

        # all_pair_sums = {}
        # quadruplets = []

        # for i in range(1, len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         current_sum = nums[i] + nums[j]
        #         difference = target - current_sum
        #         if difference in all_pair_sums:
        #             for pair in all_pair_sums[difference]:
        #                 quadruplets.append(pair + [nums[i], nums[j]])
            
        #     for k in range(0, i):
        #         current_sum = nums[i] + nums[k]
        #         if current_sum not in all_pair_sums:
        #             all_pair_sums[current_sum] = [[nums[i], nums[k]]]
        #         else:
        #             all_pair_sums[current_sum].append([nums[i], nums[k]])

        # return quadruplets
        
        # quads = []

        # allPairs = {}

        # for i in range(1, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         currentSum = nums[i] + nums[j]
        #         diff = target - currentSum
        #         if diff in allPairs:
        #             for pair in allPairs[diff]:
        #                 quads.append(pair + [nums[i], nums[j]])



        #     for k in range(0, i):
        #         currentSum = nums[k] + nums[i]
        #         if currentSum not in allPairs:
        #             allPairs[currentSum] = [[nums[k], nums[i]]]
        #         else:
        #             allPairs[currentSum].append([nums[k], nums[i]])

        
        # return quads
