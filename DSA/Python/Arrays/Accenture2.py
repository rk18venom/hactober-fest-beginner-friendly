def BooleanMatrix(arr):
    row=[]
    column=[]
    m=len(arr)
    n=len(arr[0])
    for i in range(m):
        for j in range(n):
            if arr[i][j]==1:
                row.append(i)
                column.append(j)
    
    for i in range(m):
        for j in range(n):
            if i in row:
                arr[i][j]=1
            elif i not in row and j in column:
                arr[i][j]=1
    
    return arr


m=int(input())
n=int(input())
arr=[[int(x) for x in input().split()] for row in range(m)]

ans=BooleanMatrix(arr)
print(ans)
