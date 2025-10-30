class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = [0] * 58
        for character in s:
            counts[ord(character) - 65] += 1
        length, middle_length = 0, 0
        for count in counts:
            if count == 0:
                continue
            elif count % 2 == 1:
                middle_length = 1
            length += count // 2
        return length * 2 + middle_length
