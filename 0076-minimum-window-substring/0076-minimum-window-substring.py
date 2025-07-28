class Solution:
    def minWindow(self, s: str, t: str) -> str:
        targetCharCounts = self.get_target_char_counts(t)

        numUniqueChars = len(targetCharCounts)
        numUniqueCharsDone = 0
        substrings = [0, float("inf")]
        left_idx = 0
        currentWindow = {}

        for right_idx, char in enumerate(s):
            rightChar = s[right_idx]
            if char not in targetCharCounts:
                right_idx += 1
                continue
            currentWindow[char] = currentWindow.get(char, 0) + 1
            if currentWindow[char] == targetCharCounts[char]:
                numUniqueCharsDone +=1 
            while numUniqueCharsDone == numUniqueChars and left_idx <= right_idx:
                if (right_idx - left_idx) < (substrings[1] - substrings[0]):
                    substrings = [left_idx, right_idx]
                leftChar = s[left_idx]
                if leftChar not in targetCharCounts:
                    left_idx += 1
                    continue

                if currentWindow[leftChar] == targetCharCounts[leftChar]:
                    numUniqueCharsDone -= 1
                
                currentWindow[leftChar] -= 1
                left_idx += 1

        return "" if substrings[1] == float("inf") else s[substrings[0]: substrings[1]+1]






    def get_target_char_counts(self, t):
        targetCounts = {}

        for char in t:
            targetCounts[char] = targetCounts.get(char, 0) + 1

        return targetCounts

