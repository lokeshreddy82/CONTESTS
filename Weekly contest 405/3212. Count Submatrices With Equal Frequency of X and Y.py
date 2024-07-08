class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        res=0
        n=len(grid)
        m=len(grid[0])
        prefix=[[(0,0) for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                px=0
                py=0
                if i==0:
                    if j==0:
                        x,y=0,0
                        if grid[i][j]=="X":
                            x +=1
                        if grid[i][j]=="Y":
                            y +=1
                        prefix[i][j]=(x,y)
                    else:
                        px,py=prefix[i][j-1]
                        cx,cy=0,0
                        if grid[i][j]=="X":
                            cx +=1
                        if grid[i][j]=="Y":
                            cy +=1
                        px +=cx
                        py +=cy
                        if px!=0 and px==py:
                            res +=1
                        prefix[i][j]=(px,py)
                else:
                    if j==0:
                        px,py=prefix[i-1][j]
                        cx,cy=0,0
                        if grid[i][j]=="X":
                            cx +=1
                        if grid[i][j]=="Y":
                            cy +=1
                        px +=cx
                        py +=cy
                        if px!=0 and px==py:
                            res +=1
                        prefix[i][j]=(px,py)
                    else:
                        lx,ly=prefix[i][j-1]
                        tx,ty=prefix[i-1][j]
                        cx,cy=0,0
                        if grid[i][j]=="X":
                            cx +=1
                        if grid[i][j]=="Y":
                            cy +=1
                        cx,cy=lx+tx+cx,ly+ty+cy
                        xx,yy=prefix[i-1][j-1]
                        cx -=xx
                        cy -=yy
                        if cx!=0 and cx==cy:
                            res +=1
                        prefix[i][j]=(cx,cy)
        return res
