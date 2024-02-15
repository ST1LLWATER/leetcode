import math
n=13

print(int(math.sqrt(n)))

isPrime=[True]*(n+1)

print(isPrime[4])

print(isPrime)
ans=[]
for i in range(2,int(math.sqrt(n))+1):
    if isPrime[i]:
        for j in range(i*i,n+1,i):
            isPrime[j]=False
temp=n
print(isPrime)
for i in range(int(math.sqrt(n))+1,1,-1):
    print("i Is : ",i )
    if isPrime[i] and temp%i==0:
        while(temp%i==0):
            ans.append(i)
            temp=temp/i
if temp>0:
    print(1)

print(ans)

print(len(ans))