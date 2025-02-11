class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        result_stack = []
        target_length = len(part)
        target_end_char = part[-1]

        for currentChar in s:
            result_stack.append(currentChar)
            if currentChar == target_end_char and len(result_stack) >= target_length:
                if "".join(result_stack[-target_length:]) == part:
                    del result_stack[-target_length:]
                
        return "".join(result_stack)