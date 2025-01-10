class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        globalFreq = {}
        for word in words2:
            word2Freq = {}
            self.updateFreq(word, word2Freq)

            for char, updateFreq in word2Freq.items():
                if char in globalFreq:
                    globalFreq[char] = max(updateFreq, globalFreq[char])
                else:
                    globalFreq[char] = updateFreq

        result = []
        for word in words1:
            word1Freq = {}
            self.updateFreq(word, word1Freq)

            isUniversal = True

            for char, requiredFreq in globalFreq.items():
                if word1Freq.get(char, 0) < requiredFreq:
                    isUniversal = False
                    break 
            if isUniversal:
                result.append(word)
        
        return result 
        

    def updateFreq(self, word, freqCount):
        for char in word:
            freqCount[char] = freqCount.get(char, 0) + 1
    

    # def wordSubsets(words1, words2):
    # # Step 1: Find the global character frequency requirement from words2
    # global_count = {}

    # # For each word in words2, count the frequency of each character
    # for word in words2:
    #     word_count = {}
    #     for char in word:
    #         word_count[char] = word_count.get(char, 0) + 1
        
    #     # Update global_count to hold the maximum frequency for each character
    #     for char, freq in word_count.items():
    #         if char in global_count:
    #             global_count[char] = max(global_count[char], freq)
    #         else:
    #             global_count[char] = freq
    
    # # Step 2: Check each word in words1 if it satisfies the global frequency count
    # result = []
    
    # for word in words1:
    #     word_count = {}
    #     for char in word:
    #         word_count[char] = word_count.get(char, 0) + 1
        
    #     # Check if word_count has at least the frequency of each character in global_count
    #     is_universal = True
    #     for char, required_freq in global_count.items():
    #         if word_count.get(char, 0) < required_freq:
    #             is_universal = False
    #             break
        
    #     if is_universal:
    #         result.append(word)
    
    # return result
