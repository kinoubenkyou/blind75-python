class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized: list[int] = []
        for char in s:
            code_point = ord(char)
            if 65 <= code_point <= 90:
                normalized.append(code_point + 32)
            elif 48 <= code_point <= 57 or 97 <= code_point <= 122:
                normalized.append(code_point)
        for index in range(0, len(normalized) // 2):
            if normalized[index] != normalized[len(normalized) - 1 - index]:
                return False
        return True
