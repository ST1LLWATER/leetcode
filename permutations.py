nums=[1,2,3,4]
ans=[]

def findPerm(nums,ds,freq):
    if len(ds)==len(nums):
        print("APPENDING DS: ",ds)
        ans.append(ds)
        return
    
    for i in range(len(nums)):
        if not freq[i]:
            ds.append(nums[i])
            freq[i]=1
            findPerm(nums,ds,freq)
            freq[i]=0
            ds.pop()


freq=[0]*len(nums)

findPerm(nums,[],freq)

print(ans)
        
