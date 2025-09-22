class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        if not nums:
            return 0
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        max_freq = 0
        result = 0

        for freq_value in freq.values():
            if freq_value > max_freq:
                max_freq = freq_value
                result = freq_value

            elif freq_value == max_freq:
                result += freq_value

        return result 