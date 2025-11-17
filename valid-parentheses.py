class Solution:
    def isValid(self, s: str) -> bool:
        closing_bracket_by_opening_bracket: dict = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        stack: list = []
        for character in s:
            if character in closing_bracket_by_opening_bracket:
                stack.append(character)
            elif not stack or character != closing_bracket_by_opening_bracket[stack.pop()]:
                return False
        return len(stack) == 0
