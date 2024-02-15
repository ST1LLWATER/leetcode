nums=[1,2,3]


def subsequences(idx,arr):
    if idx>=2:
        return
    
    print(arr)
    arr.append(nums[idx])
    subsequences(idx+1,arr)
    arr.pop()
    subsequences(idx+1,arr)

subsequences(0,[])
