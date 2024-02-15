s="acccbaaacccbaac"

j=1
lps=[0]*len(s)
i=0
# print(s[3])


while(j<len(s)):
    print("i,j",i,j)
    if s[j] == s[i]:
            i+=1
            lps[j]=i
            j+=1
    elif(i==0):
         j+=1
    else:
        i=lps[i-1]

print(lps)
