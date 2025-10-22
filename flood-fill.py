class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image
        stack: list[tuple[int, int]] = [(sr, sc)]
        max_row = len(image) - 1
        max_column = len(image[0]) - 1
        while stack:
            row, column = stack.pop()
            image[row][column] = color
            if row != 0 and image[row - 1][column] == original_color:
                stack.append((row - 1, column))
            if row != max_row and image[row + 1][column] == original_color:
                stack.append((row + 1, column))
            if column != 0 and image[row][column - 1] == original_color:
                stack.append((row, column - 1))
            if column != max_column and image[row][column + 1] == original_color:
                stack.append((row, column + 1))
        return image
