class Solution:
    def minWindow(self, s: str, t: str) -> str:
        targetCharCounts = self.getCharCounts(t)
        subStringBounds = self.getSubStringBounds(s, targetCharCounts)
        return self.getStringFromBounds(subStringBounds, s)



    def getStringFromBounds(self, subStringBounds, s):
        start, end = subStringBounds[0], subStringBounds[1]
        if end == float("inf"):
            return ""
        return s[start: end+1]
        

    def getCharCounts(self, string: str):
        charCounts = {}
        for s in string:
            charCounts[s] = charCounts.get(s, 0) + 1
        
        return charCounts

    def getSubStringBounds(self, s: str, targetChars: dict):
        subStringBounds = [0, float("inf")]
        subStringCharCount = {}
        numUniqueChar = len(targetChars.keys())
        numUniqueCharDone = 0
        leftIdx = 0
        rightIdx = 0

        while rightIdx < len(s):
            rightChar = s[rightIdx]
            if rightChar not in targetChars:
                rightIdx += 1
                continue

            self.increaseCharCount(rightChar, subStringCharCount)
            if subStringCharCount[rightChar] == targetChars[rightChar]:
                numUniqueCharDone += 1
            while numUniqueCharDone == numUniqueChar and leftIdx <= rightIdx:
                subStringBounds = min([leftIdx, rightIdx], subStringBounds, key=lambda x: x[1]- x[0])
                leftChar = s[leftIdx]
                if leftChar not in targetChars:
                    leftIdx += 1
                    continue
                
                if subStringCharCount[leftChar] == targetChars[leftChar]:
                    numUniqueCharDone -= 1
                
                self.decreaseCharCount(leftChar, subStringCharCount)
                leftIdx += 1

            rightIdx += 1
        return subStringBounds



    def increaseCharCount(self, char, charCounts):
        charCounts[char] = charCounts.get(char, 0) + 1

    def decreaseCharCount(self, char, charCounts):
        charCounts[char] = charCounts.get(char, 0) - 1