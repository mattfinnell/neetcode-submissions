class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        visited, directions = set(), [(0, 1), (1, 0), (0, -1), (-1, 0)]

        i, j, d, result = 0, 0, 0, []
        
        while len(visited) < (m * n):
            result.append(matrix[i][j])
            visited.add((i, j))

            ni, nj = i + directions[d][0], j + directions[d][1]
            if not 0 <= ni < m or not 0 <= nj < n or (ni, nj) in visited:
                d = (d + 1) % 4
                ni, nj = i + directions[d][0], j + directions[d][1]

            i, j = ni, nj

        return result