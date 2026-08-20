class Solution:
    def __init__(self,matrix):
        row=len(matrix)
        col=len(matrix[0])
        self.prefix=[[0]*(col+1) for _ in range(row+1)]
        for r in range(row):
            for c in range(col):
                self.prefix[r+1][c+1]=self.prefix[r][c+1]+self.prefix[r+1][c]-self.prefix[r][c]+matrix[r][c]

    def sumRegion(self,row1,col1,row2,col2):
        return self.prefix[row2+1][col2+1]-self.prefix[row1][col2+1]-self.prefix[row2+1][col1]+self.prefix[row1][col1]


obj=Solution([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])
print(obj.sumRegion(2,1,4,3))   

