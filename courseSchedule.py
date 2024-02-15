numCourses=2
prerequisites=[[1,0],[0,1]]

adj=[[] for _ in range(numCourses)]
inDeg=[0]*numCourses

ans=[]

q=[]

for u,v in prerequisites:
    adj[v].append(u)
    inDeg[u]+=1


for i in range(len(inDeg)):
    if inDeg[i]==0:
        q.append(i)

print(q)

while not q:
    cur=q.pop()
    ans.append(cur)
    for i in adj[cur]:
        inDeg[i]-=1
        if inDeg[i]==0:
            q.append(i)
if len(ans) == numCourses:
    print("trreue")
print("FALSE")