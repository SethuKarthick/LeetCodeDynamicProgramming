class Solution:
    def compress(self, chars: List[str]) -> int:
        encodedString = []

        current_length = 1

        for idx in range(1, len(chars)):
            current_char = chars[idx]
            prev_char = chars[idx-1]

            if current_char != prev_char:
                encodedString.append(prev_char)
                if current_length > 1:
                    for digit in str(current_length):
                        encodedString.append(digit)
                current_length = 1
            else:
                current_length += 1

        encodedString.append(chars[-1])
        if current_length > 1:
            for digit in str(current_length):
                encodedString.append(digit)
        for i in range(len(encodedString)):
            chars[i] = encodedString[i]

        return len(encodedString)
        

