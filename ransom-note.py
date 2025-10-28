class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_by_character: list[int] = [0] * 26
        for character in magazine:
            count_by_character[ord(character) - 97] += 1
        for character in ransomNote:
            index = ord(character) - 97
            if count_by_character[index] > 0:
                count_by_character[index] -= 1
            else:
                return False
        return True
