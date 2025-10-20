class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        frequencies = [0] * 26
        for character in s:
            frequencies[ord(character) - 97] += 1
        for character in t:
            frequencies[ord(character) - 97] -= 1
        for frequency in frequencies:
            if frequency != 0:
                return False
        return True
