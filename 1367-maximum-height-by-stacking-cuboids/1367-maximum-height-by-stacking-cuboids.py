class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        disks = sorted([sorted(disk) for disk in cuboids], reverse=True)


        heights = [disk[2] for disk in disks]
        ans = max(heights)

        for i in range(1, len(disks)):
            currentDisk = disks[i]
            for j in range(0, i):
                otherDisk = disks[j]
                if self.areValidDimensions(otherDisk, currentDisk):
                    if heights[i] <= currentDisk[2] + heights[j]:
                        heights[i] = currentDisk[2] + heights[j]
            ans = max(ans, heights[i])

        return ans


    def areValidDimensions(self, o, c):
        return o[0] >= c[0] and o[1] >= c[1] and o[2] >= c[2]