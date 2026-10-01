class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n, zero = len(matrix), len(matrix[0]), False

        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    matrix[0][j] = 0;
                    if i > 0:
                        matrix[i][0] = 0;

                    else:
                        zero = True

        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        if not matrix[0][0]:
            for i in range(m):
                matrix[i][0] = 0

        if zero:
            for j in range(n):
                matrix[0][j] = 0