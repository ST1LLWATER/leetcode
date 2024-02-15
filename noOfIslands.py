ans=0

q=[
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
# q=[[0,1],[0,1]]

count=0

def dfs(x,y):
    global count
    count+=1
    if x<0 or x>=len(q) or y<0 or y>=len(q[0]):
        return
    
    if q[x][y]==0:
        return
    
    if q[x][y]!=1:
        return
    
    q[x][y]=2
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)



def countIslands():
    for i in range(len(q)):
        for j in range(len(q[0])):
            if q[i][j]==1:
                dfs(i,j)
                global ans
                ans+=1

for i in q:
    print(i)

countIslands()
print()

for i in q:
    print(i)

print(ans)