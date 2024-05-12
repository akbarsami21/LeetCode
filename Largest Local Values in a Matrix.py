class Solution(object):
    def largestLocal(self, grid):
        n=len(grid)
        res=[[0]*(n-2) for _ in range(n-2) ]
        for i in range(n-2):
            for j in range(n-2):
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        res[i][j]=max(res[i][j],grid[k][l])
        return res
    
obj=Solution()
print(obj.largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]))