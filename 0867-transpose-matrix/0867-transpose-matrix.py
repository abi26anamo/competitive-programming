class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n= len(matrix)
        m= len(matrix[0])
        res =[]
        for c in range(m):
            ans =[]
            for r in range(n):
                ans.append(matrix[r][c])
            res.append(ans)
        return res