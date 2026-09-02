class Solution(object):
    def matrixBlockSum(self, mat, K):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        rows = len(mat)
        cols = len(mat[0])

        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            for c in range(cols):
                prefix[r + 1][c + 1] = (
                    mat[r][c]
                    + prefix[r][c + 1]
                    + prefix[r + 1][c]
                    - prefix[r][c]
                )

        ans = [[0] * cols for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                r1 = max(0, r - K)
                c1 = max(0, c - K)
                r2 = min(rows - 1, r + K)
                c2 = min(cols - 1, c + K)

                ans[r][c] = (
                    prefix[r2 + 1][c2 + 1]
                    - prefix[r1][c2 + 1]
                    - prefix[r2 + 1][c1]
                    + prefix[r1][c1]
                )

        return ans
obj=Solution()
mat=[[1,2,3],[4,5,6],[7,8,9]]
K=1
print(obj.matrixBlockSum(mat,K))