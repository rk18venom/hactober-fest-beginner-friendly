def getGreatestElements(arr,k):

    n=len(arr)
    ans=[]
    for i in range(k,n+1):
        arr2=arr[0:i].copy()
        arr2.sort(reverse=True)
        print(arr2)
        ans.append(arr2[k-1])
    return ans


arr=[int(x) for x in input().split()]
k=int(input())
print(getGreatestElements(arr,k))


