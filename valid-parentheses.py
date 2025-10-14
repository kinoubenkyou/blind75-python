class Solution:
    def isValid(self, s: str) -> bool:
        closing_bracket_by_opening_bracket: dict = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        stack: list = []
        for char in s:
            if char in closing_bracket_by_opening_bracket:
                stack.append(char)
            elif not stack:
                return False
            else:
                if not char == closing_bracket_by_opening_bracket[stack.pop()]:
                    return False
        return len(stack) == 0
