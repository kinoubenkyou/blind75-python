class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        frequencies = [0] * 26
        for character in magazine:
            frequencies[ord(character) - 97] += 1
        for character in ransomNote:
            code_point = ord(character) - 97
            if frequencies[code_point] > 0:
                frequencies[code_point] -= 1
            else:
                return False
        return True
