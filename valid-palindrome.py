class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized: str = "".join(char for char in s if char.isalnum()).lower()
        length = len(normalized)
        half_length = length // 2
        return normalized[:half_length] == normalized[length - 1:length - 1 - half_length:-1]
