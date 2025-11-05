class Solution:
    def addBinary(self, a: str, b: str) -> str:
        characters: list[str] = []
        index_a, index_b, carry = len(a) - 1, len(b) - 1, 0
        while index_a >= 0 or index_b >= 0 or carry > 0:
            if index_a >= 0:
                if a[index_a] == "1":
                    carry += 1
                index_a -= 1
            if index_b >= 0:
                if b[index_b] == "1":
                    carry += 1
                index_b -= 1
            if carry == 0:
                characters.append("0")
                carry = 0
            elif carry == 1:
                characters.append("1")
                carry = 0
            elif carry == 2:
                characters.append("0")
                carry = 1
            else:
                characters.append("1")
                carry = 1
        return "".join(characters[::-1])
