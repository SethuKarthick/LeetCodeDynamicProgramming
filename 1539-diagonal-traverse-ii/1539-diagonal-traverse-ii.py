class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        # diagonals = {}

        # for i in range(len(nums)):
        #     for j in range(len(nums[i])):
        #         diagonalSum = i+j
        #         if diagonalSum not in diagonals:
        #             diagonals[diagonalSum] = []
        #         diagonals[diagonalSum].append(nums[i][j])

        # res = []

        # for diagonal in range(len(nums)+ len(nums[0]) - 1):
        #     res.extend(diagonals[diagonal][::-1])

        # return res
        r=len(nums)
        dic=defaultdict(list)
        for i in range(r):
            for j in range(len(nums[i])):
                dic[i+j].append(nums[i][j])
        ar=[]
        for i in dic.values():
            ar.extend(i[::-1])
        return ar

        