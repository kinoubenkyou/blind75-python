class Solution:
    def longestPalindrome(self, s: str) -> int:
        frequencies = [0] * 58
        for character in s:
            frequencies[ord(character) - 65] += 1
        length, middle_length = 0, 0
        for frequency in frequencies:
            if frequency == 0:
                continue
            elif frequency % 2 == 1:
                middle_length = 1
            length += frequency // 2
        return length * 2 + middle_length
