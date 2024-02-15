import math

roads=[[0,1],[0,2],[0,3]]
seats=2

ans=0
adj=[]

for _ in range(len(roads) + 1):
    adj.append([])

print(adj)

for u,v in roads:
    adj[u].append(v)
    adj[v].append(u)

print(adj)

def findMinCost(cur,prev):
    global ans
    people=1


    print("CUR, PREV: ",cur,prev)
    for i in adj[cur]:
        if i==prev:
            continue
        people+=findMinCost(i,cur)

    if(cur!=0):
        ans+=math.ceil(people/2)

    return people


totalPeople=findMinCost(0,-1)
print(totalPeople)
print(ans)

