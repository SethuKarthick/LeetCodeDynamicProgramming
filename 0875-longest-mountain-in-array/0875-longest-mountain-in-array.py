class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # longestPeak = 0
        
        # for i in range(1, len(arr)-1):
        #     isPeak = arr[i-1] < arr[i] > arr[i+1]
        #     if not isPeak:
        #         continue

        #     left = i - 1
        #     while left > 0 and arr[left] >  arr[left - 1]:
        #         left -= 1

        #     right = i + 1
            
        #     while right < len(arr) - 1 and arr[right] > arr[right+1]:
        #         right += 1

        #     currentPeak = right - left + 1
        #     if currentPeak > longestPeak:
        #         longestPeak = currentPeak

        # return longestPeak
        longestPeak = 0

        n = len(arr) - 1

        for i in range(1, n):
            isPeak =  arr[i-1] < arr[i] > arr[i+1]
            if not isPeak:
                continue

            left = right = i

            while left > 0 and arr[left] > arr[left-1]:
                left -= 1
            
            while right < n and arr[right] > arr[right+1]:
                right += 1

            longestPeak = max(longestPeak, right - left + 1)

        return longestPeak