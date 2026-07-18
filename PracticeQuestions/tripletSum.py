def tripletsSum(arr, n):
    result = []

    for i in range(0,n-1):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (arr[i]+arr[j]+arr[k]==0):
                    result.append([i,j,k])
    return result

arr = [0,-1,2,-3,1]
n = len(arr)

print(tripletsSum(arr,n))