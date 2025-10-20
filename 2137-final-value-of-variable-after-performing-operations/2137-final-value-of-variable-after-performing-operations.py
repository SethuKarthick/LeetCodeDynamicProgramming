class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0
        for opt in operations:
            if "-" in opt:
                count -= 1
            else:
                count += 1

        return count 
