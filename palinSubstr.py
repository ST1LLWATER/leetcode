ans=0

s="aaa"


def checkPalin(i,j):
    if i>j:
        return True
    
    if s[i]==s[j]:
        return checkPalin(i+1,j-1)


def palinSubstr(s):
    global ans
    for i in range(len(s)):
        for j in range(i,len(s)):
            if(checkPalin(i,j)):
                ans+=1
            

palinSubstr(s)

print(ans)


        

